import requests
import os
import re

ORCID_ID = "0000-0002-1755-673X"
OUT_DIR = "_publications"

os.makedirs(OUT_DIR, exist_ok=True)

HEADERS = {"Accept": "application/json"}


# -------------------------
# SAFE GET
# -------------------------
def safe_get(d, *keys):
    for key in keys:
        if not isinstance(d, dict):
            return "NA"
        d = d.get(key)
        if d is None:
            return "NA"
    return d


# -------------------------
# ORCID WORK LIST
# -------------------------
def get_work_list():
    url = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"
    r = requests.get(url, headers=HEADERS)
    data = r.json()

    works = []

    for group in data.get("group", []):
        for item in group.get("work-summary", []):

            title = safe_get(item, "title", "title", "value")
            put_code = item.get("put-code")

            if title != "NA" and put_code:
                works.append((title, put_code))

    return works


# -------------------------
# PUBMED AUTHORS FALLBACK
# -------------------------
def get_pubmed_authors_from_doi(doi):
    if not doi or doi == "NA":
        return "NA"

    try:
        # 1. search PMID
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": doi,
            "retmode": "json"
        }

        r = requests.get(url, params=params)
        data = r.json()

        ids = data.get("esearchresult", {}).get("idlist", [])
        if not ids:
            return "NA"

        pmid = ids[0]

        # 2. fetch details
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        params = {"db": "pubmed", "id": pmid, "retmode": "json"}

        r = requests.get(url, params=params)
        data = r.json()

        result = data.get("result", {}).get(pmid, {})
        authors = result.get("authors", [])

        names = [a.get("name") for a in authors if a.get("name")]

        return "; ".join(names) if names else "NA"

    except:
        return "NA"


# -------------------------
# WORK DETAILS (ORCID)
# -------------------------
def get_work_details(put_code):
    url = f"https://pub.orcid.org/v3.0/{ORCID_ID}/work/{put_code}"
    r = requests.get(url, headers=HEADERS)

    if r.status_code != 200:
        return {
            "title": "NA",
            "date": "NA",
            "journal": "NA",
            "authors": "NA",
            "doi": "NA"
        }

    data = r.json()
    work = data.get("work", data)

    # TITLE
    title = safe_get(work, "title", "title", "value")

    # JOURNAL
    journal = safe_get(work, "journal-title", "value")

    # DOI
    doi = "NA"
    ext_ids = safe_get(work, "external-ids", "external-id")
    if isinstance(ext_ids, list):
        for e in ext_ids:
            if isinstance(e, dict) and e.get("external-id-type", "").lower() == "doi":
                doi = e.get("external-id-value", "NA")

    # AUTHORS (ORCID)
    authors = []
    contributors = safe_get(work, "contributors", "contributor")
    if isinstance(contributors, list):
        for c in contributors:
            name = safe_get(c, "credit-name", "value")
            if name != "NA":
                authors.append(name)

    authors = "; ".join(authors) if authors else "NA"

    # FALLBACK PUBMED IF NO AUTHORS
    if authors == "NA":
        authors = get_pubmed_authors_from_doi(doi)

    # DATE
    # DATE (Jekyll-safe ALWAYS)
    # -------------------------
    pub_date = work.get("publication-date")

    year = safe_get(pub_date, "year", "value") if pub_date else "NA"
    month = safe_get(pub_date, "month", "value") if pub_date else "NA"
    day = safe_get(pub_date, "day", "value") if pub_date else "NA"

    if year != "NA":
        year = str(year)

        # default month/day if missing
        month = str(month).zfill(2) if month != "NA" else "01"
        day = str(day).zfill(2) if day != "NA" else "01"

        date = f"{year}-{month}-{day}"
    else:
        date = "NA"

    return {
        "title": title,
        "date": date,
        "journal": journal,
        "authors": authors,
        "doi": doi
    }


# -------------------------
# SLUG
# -------------------------
def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text[:80].strip("-") or "paper"


# -------------------------
# BUILD
# -------------------------
def build():
    works = get_work_list()

    print(f"\nTOTAL WORKS FOUND: {len(works)}\n")

    for title, put_code in works:

        details = get_work_details(put_code)

        print("\n----------------------")
        print("TITLE:", details["title"])
        print("DATE:", details["date"])
        print("JOURNAL:", details["journal"])
        print("AUTHORS:", details["authors"])
        print("DOI:", details["doi"])

        content = f"""---
title: "{details['title']}"
date: {details['date']}
authors: "{details['authors']}"
journal: "{details['journal']}"
doi: "{details['doi']}"
excerpt: ""
---
"""

        filename = slugify(details["title"])
        path = os.path.join(OUT_DIR, filename + ".md")

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        print("✔ saved:", path)


if __name__ == "__main__":
    build()