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
      Social Behavior • Systems Neuroscience • Science Communication
    </p>

  </div>
</div>


<!-- ================= ABOUT ================= -->
<div class="about-container">

  <!-- HOVER IMAGE -->
  <div class="about-photo hover-image">
    <img src="/images/me.jpg" class="img-base" alt="me">
    <img src="/images/me2.jpg" class="img-hover" alt="me2">
  </div>

  <!-- TEXT -->
  <div class="about-text">
    <h2> About me </h2>

    <p>
      I am Paula, a postdoctoral researcher trying to find answers to a very broad question:
      <strong><span style="color:#39C2CF;">why do animals need to be social?</span></strong>. 
      My work looks for the mechanisms that shape social behavior, from the way animals (mice in particular) respond to one another to the information they extract from social experience and use to guide their own behavior.
    </p>

    <p>
      This line of work began during my internship in
      <a href="https://nin.nl/research-groups/keysers/" target="_blank">Christian Keysers’ lab</a>
      in Amsterdam, where I worked on emotional contagion, a key basis of empathic processes.
      During my PhD, which I carried out under the co-supervision of
      <a href="https://neurocentre-magendie.fr/recherche/Marsicano/descriptionTeam.php" target="_blank">Giovanni Marsicano</a>
      at the Neurocentre Magendie in Bordeaux and
      <a href="https://stressynomicslab.ca/" target="_blank">Jaideep Bains</a>
      at the Krembil Institute in Toronto, I studied the
      <strong><span style="color:#7c3aed;">social transmission of stress in mice</span></strong>
      and showed that the emotions of others can have cognitive consequences.
      I am now a postdoctoral researcher at the
      <a href="https://neucomplab.com/" target="_blank">NeuCompLab</a>
      in Barcelona, led by Manuel Valero, where I am trying to understand
      <strong><span style="color:#7c3aed;">how mice use others to navigate space</span></strong>.
    </p>

    <p>
      Along the way, I have worked across different levels of analysis, from cannabinoid receptors and subcellular mechanisms to astrocytes and, more recently, neurons.
      What drives me now is building a more integrative view of the brain, moving toward network-level dynamics to better understand behavior from the top down.
    </p>

  </div>
</div>


<!-- ================= RESEARCH HIGHLIGHTS ================= -->
<div class="highlights-section">

  <div class="highlights-inner">

    <h2>Research Highlights</h2>

    <div class="media-grid">

      <!-- CARD 1 -->
      <div class="media-card">
        <img src="/images/exp1.jpg" alt="Astrocytes experiment">

        <h3>Astrocyte function in neural circuits</h3>
        <p>
          Investigating how astrocytes modulate synaptic activity and contribute to information processing in the brain.
        </p>
      </div>

      <!-- CARD 2 (VIDEO) -->
      <div class="media-card">
        <video autoplay muted loop playsinline>
          <source src="/images/video1.mp4" type="video/mp4">
        </video>

        <h3>Behavioral neuroscience</h3>
        <p>
          Analyzing decision-making and spatial navigation using rodent behavioral paradigms and trajectory tracking.
        </p>
      </div>

      <!-- CARD 3 -->
      <div class="media-card">
        <img src="/images/exp2.jpg" alt="Calcium imaging">

        <h3>Calcium imaging & data analysis</h3>
        <p>
          Developing pipelines for processing in vivo imaging data and linking neural activity to behavior.
        </p>
      </div>

    </div>

  </div>
</div>


<!-- ================= CSS ================= -->
<style>

/* ================= HERO ================= */

.hero-banner {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;

  background: url("/files/banner.png") center/cover no-repeat;
  color: white;

  padding: 90px 40px;
  border-radius: 14px;
  overflow: hidden;
}

.hero-banner::before {
  content: "";
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.45);
}

.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  transform: translateY(-20px);
}

.hero-logo {
  width: 90px;
  display: block;
  margin: 0 auto 5px;
}

.hero-title {
  font-size: 3rem;
}

.hero-subtitle {
  font-size: 1.2rem;
  opacity: 0.9;
}


/* ================= ABOUT ================= */

.about-container {
  display: flex;
  gap: 30px;
  margin-top: 20px;
}

.about-photo {
  width: 20%;
  position: relative;
}

/* hover swap images */
.hover-image img {
  width: 100%;
  border-radius: 14px;
  display: block;
  transition: opacity 0.4s ease, transform 0.3s ease;
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


/* ABOUT TEXT */
.about-text {
  width: 70%;
  background: rgba(0,0,0,0.55);
  backdrop-filter: blur(10px);

  border-radius: 14px;
  padding: 14px 16px;

  border: 3px solid rgba(255,255,255,0.08);
  border-left: 7px solid #603287;

  color: #d8d8d8;
}

.about-text p {
  font-size: 0.95rem;
  line-height: 1.75;
}


/* ================= RESEARCH FULL WIDTH ================= */

.highlights-section {
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  padding: 70px 40px;

  background: rgba(0,0,0,0.35);

  border-top: 1px solid rgba(255,255,255,0.06);
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.highlights-inner {
  max-width: 1100px;
  margin: 0 auto;
}

.highlights-section h2 {
  color: #fff;
  margin-bottom: 25px;
}


/* ================= MEDIA CARDS ================= */

.media-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 22px;
}

.media-card {
  background: rgba(0,0,0,0.55);
  backdrop-filter: blur(10px);

  border-radius: 16px;
  overflow: hidden;

  border: 1px solid rgba(255,255,255,0.08);

  transition: transform 0.25s ease, border 0.25s ease;
}

.media-card:hover {
  transform: translateY(-6px);
  border: 1px solid #39C2CF;
}

.media-card img,
.media-card video {
  width: 100%;
  height: 200px;
  object-fit: cover;
  display: block;

  transition: transform 0.4s ease;
}

.media-card:hover img,
.media-card:hover video {
  transform: scale(1.03);
}

.media-card h3 {
  color: #fff;
  font-size: 1.05rem;
  margin: 12px 12px 6px;
}

.media-card p {
  color: #cfcfcf;
  font-size: 0.9rem;
  margin: 0 12px 14px;
}


/* ================= RESPONSIVE ================= */

@media (max-width: 900px) {

  .about-container {
    flex-direction: column;
  }

  .about-photo,
  .about-text {
    width: 100%;
  }

  .media-grid {
    grid-template-columns: 1fr;
  }

  .highlights-section {
    width: 100%;
    margin-left: 0;
  }
}

.page__content {
  padding-top: 0 !important;
}

.initial-content {
  padding-top: 0 !important;
}

.splash .page__content {
  padding-top: 0 !important;
}

</style>

