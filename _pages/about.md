---
title: "Home"
layout: splash
permalink: /
author_profile: true
---

<!-- ================= HERO ================= -->
<div class="hero-banner">
  <div class="hero-content">
    <img src="/images/white.png" class="hero-logo" alt="logo">
    <h1 class="hero-title">Paula Gómez-Sotres</h1>
    <p class="hero-subtitle">
      Social Behavior · Systems Neuroscience · Science Communication
    </p>
  </div>
</div>


<!-- ================= ABOUT + PUBLICATIONS LAYOUT ================= -->
<div class="about-pubs-wrapper">
  <div class="about-pubs-container">
    
    <!-- LEFT COLUMN: PHOTO + ABOUT TEXT -->
    <div class="about-left">
      
      <!-- PHOTO + SOCIALS -->
      <div class="about-sidebar">
        <div class="about-photo hover-image">
          <img src="/images/me.jpg" class="img-base" alt="me">
          <img src="/images/me2.jpg" class="img-hover" alt="me2">
        </div>
        
        <!-- SOCIAL LINKS BELOW PHOTO -->
        <div class="about-socials">
          {% assign author = site.author %}
          {% if author.twitter or author.linkedin or author.github %}
          <div class="social-icons-about">
            {% if author.twitter %}
              <a href="https://x.com/{{ author.twitter }}" class="social-icon-about" title="X (Twitter)" aria-label="X (Twitter)">
                <i class="fab fa-fw fa-x-twitter"></i>
              </a>
            {% endif %}
            {% if author.linkedin %}
              <a href="https://www.linkedin.com/in/{{ author.linkedin }}" class="social-icon-about" title="LinkedIn" aria-label="LinkedIn">
                <i class="fab fa-fw fa-linkedin"></i>
              </a>
            {% endif %}
            {% if author.github %}
              <a href="https://github.com/{{ author.github }}" class="social-icon-about" title="GitHub" aria-label="GitHub">
                <i class="fab fa-fw fa-github"></i>
              </a>
            {% endif %}
          </div>
          {% endif %}
        </div>
      </div>

      <!-- ABOUT TEXT -->
      <div class="about-text">
        <h2>About me</h2>

        <p>
          I'm a postdoctoral researcher exploring a central question: <em>why do animals need to be social?</em> My work focuses on the neural mechanisms that shape social behavior—from how animals respond to one another to how they extract social information and use it to guide their own actions. I primarily work with mice, using electrophysiology, behavioral tracking, and computational approaches to understand social circuits at the network level.
        </p>

        <p>
          This journey began in <a href="https://nin.nl/research-groups/keysers/" target="_blank">Christian Keysers' lab</a> in Amsterdam, where I investigated emotional contagion. During my PhD co-supervised by <a href="https://neurocentre-magendie.fr/" target="_blank">Giovanni Marsicano</a> and <a href="https://stressynomicslab.ca/" target="_blank">Jaideep Bains</a>, I discovered that social signals can impair memory through astrocytic mechanisms. Now at <a href="https://neucomplab.com/" target="_blank">NeuCompLab</a> in Barcelona, I'm investigating how hippocampal representations of a social partner evolve during bonding formation.
        </p>

        <p>
          Beyond the bench, I care deeply about making science more accessible and supporting the researchers coming up behind me. This drives much of my outreach and mentoring work.
        </p>
      </div>

    </div>

    <!-- RIGHT COLUMN: LATEST PUBLICATIONS -->
    <div class="publications-floating">
      <h3 class="pubs-title">Latest Publications</h3>
      
      <div class="publications-floating-grid">
        <article class="pub-floating-card">
          <p class="pub-floating-name">Endocannabinoid-dopamine interactions mediate incidental associations in the hippocampus</p>
          <p class="pub-floating-authors">Fundazuri, Barrera-Conde, Rampini, Gomez-Sotres, et al.</p>
          <p class="pub-floating-meta">bioRxiv, 2026 · <a href="https://www.biorxiv.org/content/10.64898/2026.08.24.746680v1" target="_blank" class="pub-floating-link">DOI →</a></p>
        </article>

        <article class="pub-floating-card">
          <p class="pub-floating-name">Who sets the brakes on anxiety? A role for astrocytic histamine 3 receptors</p>
          <p class="pub-floating-authors">Gomez-Sotres & Mederos</p>
          <p class="pub-floating-meta">Neuron Preview, 2026 · <a href="https://doi.org/10.1016/j.neuron.2026.05.011" target="_blank" class="pub-floating-link">DOI →</a></p>
        </article>
      </div>
    <div class="publications-footer">
    <a href="/publications/" class="btn-read-more">Read All Publications →</a>
    </div>
</div>
  </div>
</div>


<!-- ================= CURRENT PROJECTS ================= -->
<div class="projects-section">
  <h2>Current Projects</h2>
  
  <div class="projects-grid">
    
    <!-- PROJECT 1 -->
    <article class="project-card-wrapper">
      <div class="project-header-top">
        <h3>Social Behavior</h3>
        <span class="project-status active">In development</span>
      </div>
      <div class="project-card">
        <img class="project-gif" src="/images/project-1.gif" alt="Social Behavior">
      </div>
      <div class="project-footer">
        <button class="know-more-btn">Know More</button>
        <div class="description-popup">
          <p>How are social interactions stored? What do we learn from other individuals? By investigating hippocampal computations, we are trying to unravel the basis of navigating a social space.</p>
        </div>
      </div>
    </article>

    <!-- PROJECT 2 -->
    <article class="project-card-wrapper">
      <div class="project-header-top">
        <h3>Cancer & Neural Circuits</h3>
        <span class="project-status in-progress">Active</span>
      </div>
      <div class="project-card">
        <img class="project-gif" src="/images/project-2.png" alt="Cancer & Neural Circuits">
      </div>
      <div class="project-footer">
        <button class="know-more-btn">Know More</button>
        <div class="description-popup">
          <p>In collaboration with the lab of Manuel Valiente (CNIO, Madrid), we are investigating how metastatic cancer affects cognition and hippocampal circuits recording the neuronal activity of mice during the progression of tumour development.</p>
        </div>
      </div>
    </article>

    <!-- PROJECT 3 -->
    <article class="project-card-wrapper">
      <div class="project-header-top">
        <h3>Astrocytic Endocannabinoids</h3>
        <span class="project-status active">In preparation</span>
      </div>
      <div class="project-card">
        <img class="project-gif" src="/images/project-3.gif" alt="Astrocytic endocannabinoids">
      </div>
      <div class="project-footer">
        <button class="know-more-btn">Know More</button>
        <div class="description-popup">
          <p>Together with Abel Eraso (corresponding author) and colleagues, we have discovered that astrocytes can produce 2-AG, which works as neuromodulator of neuronal activity and behavior, both in the somatosensory cortex and the olfactory bulb.</p>
        </div>
      </div>
    </article>

    <!-- PROJECT 4 -->
    <article class="project-card-wrapper">
      <div class="project-header-top">
        <h3>Neurocuriously</h3>
        <span class="project-status in-progress">Active</span>
      </div>
      <div class="project-card">
        <img class="project-gif" src="/images/project-4.gif" alt="Neurocuriously">
      </div>
      <div class="project-footer">
        <button class="know-more-btn">Know More</button>
        <div class="description-popup">
          <p><em>Science communication and outreach</em> bringing neuroscience to broader audiences. <strong>Talks, workshops, and public engagement</strong> activities.</p>
        </div>
      </div>
    </article>

  </div>
</div>


<!-- ================= STYLES ================= -->
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

* {
  font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

/* ================= HERO ================= */
.hero-banner {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  background: url("/files/banner.png") center/cover no-repeat;
  color: white;
  padding: 80px 40px;
  border-radius: 8px;
  overflow: hidden;
}

.hero-banner::before {
  content: "";
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.35);
}

.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
}

.hero-logo {
  width: 80px;
  display: block;
  margin: 0 auto 12px;
}

.hero-title {
  font-size: 2.8rem;
  margin: 0 0 12px 0;
  font-weight: 700;
  letter-spacing: -0.5px;
  line-height: 1.1;
}

.hero-subtitle {
  font-size: 0.8rem;
  opacity: 0.95;
  font-weight: 400;
  letter-spacing: 0.5px;
}


/* ================= ABOUT + PUBLICATIONS LAYOUT ================= */
.about-pubs-wrapper {
  margin: 30px 0;
}

.about-pubs-container {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 35px;
  align-items: flex-start;
}

.about-left {
  display: flex;
  gap: 25px;
}

.about-sidebar {
  width: 200px;
  flex-shrink: 0;
}

.about-photo {
  width: 100%;
  position: relative;
  margin-bottom: 18px;
  border: 1px solid rgba(70, 184, 184, 0.25);
  border-radius: 8px;
  overflow: hidden;
}

.hover-image img {
  width: 100%;
  border-radius: 7px;
  display: block;
  transition: opacity 0.4s ease;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
}

.img-hover {
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0;
}

.hover-image:hover .img-hover {
  opacity: 1;
}

.hover-image:hover .img-base {
  opacity: 0;
}

/* SOCIAL ICONS */
.about-socials {
  display: flex;
  justify-content: center;
}

.social-icons-about {
  display: flex;
  gap: 10px;
}

.social-icon-about {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(70, 184, 184, 0.1);
  color: #46b8b8 !important;
  transition: all 0.3s ease;
  font-size: 15px;
  text-decoration: none;
  border: 1px solid rgba(70, 184, 184, 0.25);
}

.social-icon-about:hover {
  background: #46b8b8;
  color: #000000 !important;
  border-color: #46b8b8;
  transform: translateY(-3px);
  box-shadow: 0 6px 16px rgba(70, 184, 184, 0.25);
}

/* ABOUT TEXT */
.about-text {
  flex: 1;
  background: #000000;
  border-radius: 8px;
  padding: 28px;
  border: 1px solid rgba(70, 184, 184, 0.15);
  border-left: 2px solid #46b8b8;
}

.about-text h2 {
  color: #ffffff;
  font-size: 2rem;
  margin-bottom: 18px;
  font-weight: 700;
  letter-spacing: -0.3px;
}

.about-text p {
  font-size: 0.85rem;
  line-height: 1.7;
  margin-bottom: 14px;
  color: #c8c8c8;
  font-weight: 400;
}

.about-text a {
  color: #46b8b8;
  text-decoration: none;
  border-bottom: 1px solid rgba(70, 184, 184, 0.3);
  transition: all 0.3s ease;
  font-weight: 500;
}

.about-text a:hover {
  color: #56d8d8;
  border-bottom-color: #56d8d8;
}

.about-text em {
  color: #46b8b8;
  font-style: italic;
  font-weight: 500;
}

.about-text strong {
  color: #9d4edd;
  font-weight: 700;
}

/* RESEARCH BADGES */
.research-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(70, 184, 184, 0.12);
}

.badge {
  display: inline-block;
  padding: 5px 11px;
  border-radius: 16px;
  font-size: 0.6rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  border: 1px solid;
  transition: all 0.3s ease;
}

.badge-teal {
  background: rgba(70, 184, 184, 0.1);
  color: #46b8b8;
  border-color: rgba(70, 184, 184, 0.25);
}

.badge-teal:hover {
  background: rgba(70, 184, 184, 0.15);
  border-color: #46b8b8;
  box-shadow: 0 3px 8px rgba(70, 184, 184, 0.15);
}


/* ================= PUBLICATIONS FLOATING (NO BOX) ================= */
.publications-floating {
  position: relative;
}

.pubs-title {
  color: #ffffff;
  font-size: 1.2rem;
  margin: 0 0 16px 0;
  font-weight: 700;
  letter-spacing: -0.2px;
}

.publications-floating-grid {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.pub-floating-card {
  padding: 8px 0;
  border-bottom: 1px solid rgba(70, 184, 184, 0.1);
  transition: all 0.3s ease;
}

.pub-floating-card:last-child {
  border-bottom: none;
}

.pub-floating-card:hover {
}

.pub-floating-name {
  color: #e8e8e8;
  font-size: 0.55rem;
  line-height: 1.2;
  margin: 0 0 2px 0;
  font-weight: 600;
}

.pub-floating-authors {
  color: #a0a0a0;
  font-size: 0.5rem;
  line-height: 1.15;
  margin: 0 0 1px 0;
  font-weight: 500;
}

.pub-floating-meta {
  color: #888888;
  font-size: 0.5rem;
  margin: 0 0 5px 0;
  display: inline;
}

.pub-floating-link {
  color: #46b8b8;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.75rem;
  transition: all 0.3s ease;
  display: inline;
  margin-left: 4px;
}

.pub-floating-link:hover {
  color: #56d8d8;
}


/* ================= PROJECTS SECTION ================= */
.projects-section {
  margin-top: 60px;
  padding: 0 0 60px 0;
  border-bottom: 1px solid rgba(70, 184, 184, 0.1);
}

.projects-section h2 {
  color: #ffffff;
  font-size: 2rem;
  margin-bottom: 28px;
  font-weight: 700;
  letter-spacing: -0.3px;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.project-card-wrapper {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.project-header-top {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.project-header-top h3 {
  color: #ffffff;
  font-size: 1rem;
  margin: 0;
  font-weight: 700;
  line-height: 1.3;
}

.project-status {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 0.55rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  white-space: nowrap;
  width: fit-content;
}

.project-status.active {
  background: rgba(70, 184, 184, 0.15);
  color: #46b8b8;
  border: 1px solid rgba(70, 184, 184, 0.3);
}

.project-status.in-progress {
  background: rgba(100, 200, 200, 0.15);
  color: #60c8c8;
  border: 1px solid rgba(100, 200, 200, 0.3);
}

.project-card {
  position: relative;
  border-radius: 8px;
  height: 250px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s ease;
}

.project-gif {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
}

.project-footer {
  display: flex;
  justify-content: center;
  position: relative;
}

.know-more-btn {
  padding: 6px 16px;
  border: 1px solid #46b8b8;
  background: transparent;
  color: #46b8b8;
  text-decoration: none;
  border-radius: 12px;
  font-weight: 600;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.2px;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
}

.know-more-btn:hover {
  background: #46b8b8;
  color: #000000;
  box-shadow: 0 3px 8px rgba(70, 184, 184, 0.2);
}

.description-popup {
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(-10px);
  background: #000000;
  border: 1px solid rgba(70, 184, 184, 0.25);
  border-radius: 8px;
  padding: 16px;
  width: 280px;
  opacity: 0;
  pointer-events: none;
  transition: all 0.3s ease;
  z-index: 10;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
}

.know-more-btn:hover + .description-popup,
.description-popup:hover {
  opacity: 1;
  pointer-events: auto;
  transform: translateX(-50%) translateY(-15px);
}

.description-popup p {
  color: #c8c8c8;
  font-size: 0.75rem;
  line-height: 1.5;
  margin: 0;
}

.description-popup em {
  color: #46b8b8;
  font-style: italic;
  font-weight: 500;
}

.description-popup strong {
  color: #9d4edd;
  font-weight: 700;
}


/* Override default page styles */
.page__content {
  padding-top: 0 !important;
}

/* RESPONSIVE */
@media (max-width: 1400px) {
  .about-pubs-container {
    gap: 25px;
  }

  .projects-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (max-width: 1200px) {
  .about-pubs-container {
    gap: 20px;
  }
  
  .projects-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .project-card {
    height: 200px;
  }
}

@media (max-width: 1024px) {
  .about-pubs-container {
    gap: 20px;
  }
  
  .projects-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .project-card {
    height: 200px;
  }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 1.6rem;
  }

  .about-pubs-container {
    grid-template-columns: 1fr;
  }

  .about-left {
    flex-direction: column;
  }

  .about-sidebar {
    width: 100%;
    display: flex;
    gap: 20px;
  }

  .about-photo {
    width: 170px;
    flex-shrink: 0;
  }

  .about-text {
    padding: 20px;
  }

  .about-text h2 {
    font-size: 1.4rem;
  }

  .about-text p {
    font-size: 0.75rem;
  }

  .projects-grid {
    grid-template-columns: 1fr;
  }
  
  .project-card {
    height: 250px;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 1.2rem;
  }

  .about-sidebar {
    flex-direction: column;
  }

  .about-photo {
    width: 140px;
  }
}

.initial-content {
  padding-top: 0 !important;
}

.splash .page__content {
  padding-top: 0 !important;
}

</style>