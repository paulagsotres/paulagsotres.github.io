---
title: "Neurocuriously"
layout: splash
permalink: /scientificcomm/
author_profile: true
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital@0;1&family=Poppins:wght@400;500;600;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

* { margin: 0; padding: 0; box-sizing: border-box; }

.scicomm-wrapper {
  display: grid;
  grid-template-columns: 380px 1fr;
  gap: 0;
  height: 100vh;
  overflow: hidden;
}

.scicomm-sidebar {
  position: relative;
  width: 380px;
  background: #000000;
  border-right: 2px solid #B13BFF;
  padding: 0;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  height: 100vh;
  overflow: hidden;
}

.scicomm-banner-img {
  width: 80%;
  height: 80%;
  border-radius: 0;
  box-shadow: none;
  object-fit: cover;
}

.scicomm-main {
  padding: 60px 40px;
  overflow-y: auto;
  height: 100vh;
}

.neuro-text {
  font-family: 'Poppins', sans-serif;
  font-weight: 700;
  font-style: normal;
  color: #ffffff;
}

.forager-text {
  font-family: 'Fraunces', serif;
  font-weight: 700;
  font-style: italic;
  color: #B13BFF;
  display: inline;
}

.scicomm-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 20px;
}

.scicomm-about {
  margin-bottom: 80px;
  margin-top: 0;
}

.scicomm-about h1 {
  color: #ffffff;
  font-size: 3rem;
  margin: 0 0 8px 0;
  font-weight: 700;
  letter-spacing: -0.5px;
  line-height: 1.1;
}

.scicomm-tagline {
  color: #c8c8c8;
  font-size: 1.1rem;
  margin: 0 0 32px 0;
  opacity: 0.95;
  letter-spacing: 0.5px;
}

.scicomm-about h2 {
  color: #ffffff;
  font-size: 1.5rem;
  margin: 24px 0 16px 0;
  font-weight: 700;
  letter-spacing: -0.3px;
  margin-top: 32px;
}

.scicomm-about p {
  color: #c8c8c8;
  font-size: 0.95rem;
  line-height: 1.8;
  margin: 0;
}

.story-intro {
  max-width: 700px;
  margin: 0 auto 60px;
}

.story-intro p {
  color: #d8d8d8;
  font-size: 1rem;
  line-height: 1.8;
  margin-bottom: 20px;
}

.story-intro strong {
  color: #B13BFF;
  font-weight: 700;
}

.story-toggle {
  background: none;
  border: 2px solid #B13BFF;
  color: #B13BFF;
  padding: 12px 24px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  border-radius: 8px;
  transition: all 0.3s ease;
  font-family: 'Poppins', sans-serif;
  letter-spacing: 0.5px;
}

.story-toggle:hover {
  background: rgba(177, 59, 255, 0.1);
  border-color: #39FF14;
  color: #39FF14;
}

.story-popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  z-index: 2000;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.story-popup-overlay.active {
  display: flex;
}

.story-popup {
  background: #1a1a1a;
  border: 2px solid #B13BFF;
  border-radius: 16px;
  padding: 40px;
  max-width: 700px;
  max-height: 85vh;
  overflow-y: auto;
  position: relative;
  animation: popupSlideIn 0.3s ease;
}

@keyframes popupSlideIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.story-popup-close {
  position: absolute;
  top: 20px;
  right: 20px;
  background: none;
  border: none;
  color: #B13BFF;
  font-size: 28px;
  cursor: pointer;
  transition: color 0.2s;
}

.story-popup-close:hover {
  color: #39FF14;
}

.story-popup h2 {
  color: #B13BFF;
  font-size: 1.4rem;
  margin: 0 0 16px 0;
  font-weight: 700;
  font-family: 'Fraunces', serif;
  font-style: italic;
}

.story-popup h2:first-child {
  margin-top: 0;
}

.story-popup p {
  color: #d8d8d8;
  font-size: 0.95rem;
  line-height: 1.8;
  margin: 0 0 20px 0;
}

.story-popup strong {
  color: #B13BFF;
  font-weight: 700;
}

.scicomm-mission {
  margin-bottom: 80px;
}

.aims-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.aim-card {
  background: rgba(177, 59, 255, 0.05);
  border: 1px solid rgba(177, 59, 255, 0.2);
  border-radius: 12px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  transition: all 0.3s ease;
}

.aim-card:hover {
  background: rgba(177, 59, 255, 0.12);
  border-color: #39FF14;
  box-shadow: 0 0 20px rgba(177, 59, 255, 0.1);
}

.aim-icon {
  font-size: 32px;
  height: 40px;
  display: flex;
  align-items: center;
}

.aim-text {
  color: #c8c8c8;
  font-size: 0.9rem;
  line-height: 1.6;
}

.aim-text strong {
  color: #B13BFF;
  font-weight: 700;
}

.scicomm-impact {
  margin-bottom: 60px;
  border-top: 1px solid rgba(177, 59, 255, 0.1);
  padding-top: 60px;
}

.scicomm-impact h2 {
  color: #ffffff;
  font-size: 2rem;
  margin-bottom: 40px;
  font-weight: 700;
  letter-spacing: -0.3px;
  text-align: center;
  line-height: 1.1;
}

.impact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 50px;
}

.impact-card {
  background: rgba(177, 59, 255, 0.08);
  border: 1px solid rgba(177, 59, 255, 0.2);
  border-radius: 12px;
  padding: 24px;
  text-align: center;
  transition: all 0.3s ease;
}

.impact-card:hover {
  background: rgba(177, 59, 255, 0.15);
  border-color: #39FF14;
  box-shadow: 0 0 20px rgba(177, 59, 255, 0.1);
}

.impact-stat {
  font-size: 48px;
  font-weight: 700;
  color: #B13BFF;
  font-family: 'Fraunces', serif;
  font-style: italic;
  margin-bottom: 8px;
}

.impact-label {
  font-size: 0.9rem;
  color: #c8c8c8;
  line-height: 1.5;
}

.impact-section h3 {
  color: #B13BFF;
  font-size: 1.3rem;
  margin-top: 40px;
  margin-bottom: 16px;
  font-weight: 700;
  font-family: 'Fraunces', serif;
  font-style: italic;
}

.impact-list {
  list-style: none;
  padding: 0;
}

.impact-list li {
  color: #d8d8d8;
  font-size: 0.95rem;
  line-height: 1.8;
  padding: 12px 0;
  padding-left: 24px;
  position: relative;
}

.impact-list li:before {
  content: "→";
  position: absolute;
  left: 0;
  color: #39FF14;
  font-weight: 700;
}

.impact-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 12px;
}

.social-link {
  color: #B13BFF;
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s;
  padding: 6px 0;
}

.social-link:hover {
  color: #39FF14;
  text-decoration: underline;
}

.social-link i {
  font-size: 0.9rem;
}

.impact-detail {
  font-size: 0.8rem;
  color: #888;
  margin-top: 8px;
  line-height: 1.4;
}

.impact-subsection-text {
  color: #888;
  font-size: 0.9rem;
  margin-bottom: 16px;
  font-style: italic;
}

.media-container {
  background: rgba(177, 59, 255, 0.05);
  border: 1px solid rgba(177, 59, 255, 0.1);
  border-radius: 12px;
  padding: 24px;
  margin-top: 16px;
}

.video-embed {
  position: relative;
  padding-bottom: 56.25%;
  height: 0;
  overflow: hidden;
  border-radius: 8px;
  margin-top: 16px;
}

.video-embed iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 8px;
}

.scicomm-activities {
  margin-bottom: 80px;
}

.scicomm-activities h2 {
  color: #ffffff;
  font-size: 2rem;
  margin-bottom: 12px;
  font-weight: 700;
  letter-spacing: -0.3px;
  text-align: center;
  line-height: 1.1;
}

.network-subtitle {
  font-size: 16px;
  color: #888;
  text-align: center;
  margin-bottom: 30px;
}

.bubble-network-wrapper {
  position: relative;
  max-width: 450px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 45px;
  padding: 20px 0;
  height: 380px;
}

.bubble-container {
  width: 150px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  justify-content: center;
}

.bubble-container-center {
  grid-column: 1 / -1;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.bubble-button {
  width: 130px;
  height: 130px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, rgba(177, 59, 255, 0.2), rgba(0, 0, 0, 0.6));
  border: 2px solid #B13BFF;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: all 0.3s ease;
  box-shadow: 0 0 30px rgba(177, 59, 255, 0.1);
  cursor: pointer;
  position: relative;
  overflow: visible;
  padding: 10px;
  text-align: center;
}

.bubble-button:hover {
  transform: scale(1.15);
  border-color: #39FF14;
  box-shadow: 0 0 50px rgba(57, 255, 20, 0.3);
}

.bubble-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
}

.bubble-emoji {
  font-size: 36px;
  height: 45px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.bubble-text {
  font-size: 10px;
  color: #B13BFF;
  font-weight: 600;
  text-transform: uppercase;
  white-space: normal;
  letter-spacing: 0.5px;
  line-height: 1.1;
  font-family: 'Fraunces', serif;
  font-style: italic;
}

svg.network-lines {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.card-popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #1a1a1a;
  border: 2px solid #B13BFF;
  border-radius: 20px;
  padding: 40px;
  width: 90%;
  max-width: 500px;
  z-index: 1000;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
  display: none;
}

.card-popup.active {
  display: block;
  animation: slideUp 0.3s ease;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translate(-50%, -45%);
  }
  to {
    opacity: 1;
    transform: translate(-50%, -50%);
  }
}

.card-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  z-index: 999;
  display: none;
}

.card-overlay.active {
  display: block;
}

.popup-close {
  position: absolute;
  top: 20px;
  right: 20px;
  background: none;
  border: none;
  color: #B13BFF;
  font-size: 24px;
  cursor: pointer;
  transition: color 0.2s;
}

.popup-close:hover {
  color: #39FF14;
}

.popup-image {
  width: 100%;
  height: 220px;
  border-radius: 12px;
  background: rgba(177, 59, 255, 0.1);
  border: 1px solid rgba(177, 59, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 80px;
  margin-bottom: 24px;
  overflow: hidden;
}

.popup-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.popup-title {
  font-size: 22px;
  font-weight: 700;
  color: #B13BFF;
  margin-bottom: 16px;
  font-family: 'Fraunces', serif;
  font-style: italic;
}

.popup-description {
  font-size: 14px;
  color: #c8c8c8;
  line-height: 1.8;
  margin-bottom: 20px;
}

.popup-link {
  display: inline-block;
  color: #39FF14;
  text-decoration: none;
  font-weight: 600;
  font-size: 13px;
  border-bottom: 1px solid rgba(57, 255, 20, 0.3);
  transition: all 0.2s;
}

.popup-link:hover {
  color: #B13BFF;
  border-bottom-color: #B13BFF;
}

@media (max-width: 1024px) {
  .scicomm-wrapper {
    grid-template-columns: 1fr;
  }

  .scicomm-sidebar {
    position: relative;
    width: 100%;
    height: 400px;
    border-right: none;
    border-bottom: 2px solid #B13BFF;
    margin-bottom: 40px;
    padding: 0;
  }

  .scicomm-banner-img {
    height: 100%;
  }

  .scicomm-main {
    padding: 40px 20px;
  }

  .bubble-network-wrapper {
    gap: 30px;
    height: auto;
  }

  .aims-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .scicomm-about h2 {
    font-size: 1.6rem;
  }

  .scicomm-activities h2 {
    font-size: 1.6rem;
  }

  .scicomm-impact h2 {
    font-size: 1.6rem;
  }

  .scicomm-about p {
    font-size: 0.9rem;
  }

  .scicomm-main {
    padding: 30px 15px;
  }

  .bubble-network-wrapper {
    grid-template-columns: 1fr;
    gap: 30px;
    height: auto;
  }

  .bubble-button {
    width: 120px;
    height: 120px;
  }

  .bubble-emoji {
    font-size: 32px;
    height: 40px;
  }

  .bubble-text {
    font-size: 9px;
  }

  .aims-grid {
    grid-template-columns: 1fr;
  }

  .impact-grid {
    grid-template-columns: 1fr;
  }

  .impact-stat {
    font-size: 40px;
  }

  .story-popup {
    padding: 30px;
    border-radius: 12px;
  }

  .story-popup h2 {
    font-size: 1.2rem;
  }

  .story-popup p {
    font-size: 0.9rem;
  }
  .impact-grid {
    grid-template-columns: 1fr;
  }

  .impact-stat {
    font-size: 40px;
  }

  .media-container {
    padding: 16px;
  }
}

@media (max-width: 480px) {
  .scicomm-sidebar {
    height: 300px;
  }

  .scicomm-main {
    padding: 20px 15px;
  }

  .bubble-button {
    width: 110px;
    height: 110px;
  }

  .bubble-emoji {
    font-size: 28px;
    height: 35px;
  }

  .bubble-text {
    font-size: 8px;
  }

  .bubble-network-wrapper {
    gap: 20px;
    height: 350px;
  }

  .story-intro {
    margin-bottom: 40px;
  }

  .story-toggle {
    padding: 10px 16px;
    font-size: 0.85rem;
  }

  .aims-grid {
    grid-template-columns: 1fr;
  }

  .aim-card {
    padding: 16px;
  }

  .impact-stat {
    font-size: 32px;
  }

  .impact-card {
    padding: 16px;
  }

  .media-container {
    padding: 12px;
  }

  .social-link {
    font-size: 0.8rem;
  }

  .impact-links {
    gap: 8px;
  }

  .story-popup {
    padding: 20px;
    max-width: 90vw;
  }

  .story-popup h2 {
    font-size: 1.1rem;
    margin-top: 16px;
  }

  .story-popup p {
    font-size: 0.85rem;
  }

  .story-popup-close {
    font-size: 24px;
  }
}
</style>

<div class="scicomm-wrapper">
  <aside class="scicomm-sidebar">
    <img src="/images/neurocuriously-banner.png" alt="Neurocuriously - Paula Gómez-Sotres" class="scicomm-banner-img">
  </aside>

  <main class="scicomm-main">

<div class="scicomm-about">
  <div class="scicomm-container">
    <h1><span class="neuro-text">neuro</span><span class="forager-text">curiously</span></h1>
    <p class="scicomm-tagline">Bridging cutting-edge brain science with curious minds</p>
    
    <div class="story-intro">
      <p>
        Neurocuriously is my commitment to making neuroscience accessible, engaging, and relevant to everyone. Adapting my communication across languages and across diverse formats, I aim to bridge the gap between cutting-edge brain research and diverse audiences: from high school students to neighbors. Because science communication isn't just about sharing knowledge; it's about meeting people where they are and inspiring curiosity in their own language and through their preferred medium.
      </p>
      <button class="story-toggle" onclick="toggleStoryPopup()">
        Know the full story here →
      </button>
    </div>

  </div>
</div>

<!-- MISSION SECTION -->
<div class="scicomm-mission">
  <div class="scicomm-container">
    <h2 style="color: #ffffff; font-size: 2rem; margin-bottom: 40px; font-weight: 700; letter-spacing: -0.3px; text-align: center; line-height: 1.1;">
      <span class="neuro-text">the</span> <span class="forager-text">mission</span>
    </h2>
    
    <div class="aims-grid">
      <div class="aim-card">
        <div class="aim-icon">🔬</div>
        <div class="aim-text">
          <strong>Basic science matters.</strong> Help the general public understand why fundamental research is essential—it's the bridge to clinically relevant breakthroughs.
        </div>
      </div>
      <div class="aim-card">
        <div class="aim-icon">✨</div>
        <div class="aim-text">
          <strong>Inspire the next generation.</strong> Show young people that science is a rewarding, accessible career path worth pursuing.
        </div>
      </div>
    </div>
  </div>
</div>

<div class="scicomm-activities">
  <div class="scicomm-container">
    <h2><span class="neuro-text">what we</span> <span class="forager-text">do</span></h2>
    <p class="network-subtitle">Multiple formats to reach diverse audiences</p>
    
    <div class="bubble-network-wrapper">
      <svg class="network-lines" id="network-lines"></svg>
      
      <div class="bubble-container">
        <button class="bubble-button" data-id="0">
          <div class="bubble-content">
            <div class="bubble-emoji">🔬</div>
            <div class="bubble-text">Lab Visits</div>
          </div>
        </button>
      </div>
      
      <div class="bubble-container">
        <button class="bubble-button" data-id="1">
          <div class="bubble-content">
            <div class="bubble-emoji">🎓</div>
            <div class="bubble-text">Workshops</div>
          </div>
        </button>
      </div>
      
      <div class="bubble-container">
        <button class="bubble-button" data-id="2">
          <div class="bubble-content">
            <div class="bubble-emoji">📺</div>
            <div class="bubble-text">Video Series</div>
          </div>
        </button>
      </div>
      
      <div class="bubble-container">
        <button class="bubble-button" data-id="3">
          <div class="bubble-content">
            <div class="bubble-emoji">🎤</div>
            <div class="bubble-text">Public Talks</div>
          </div>
        </button>
      </div>
      
      <div class="bubble-container-center">
        <button class="bubble-button" data-id="4">
          <div class="bubble-content">
            <div class="bubble-emoji">🧬</div>
            <div class="bubble-text">Online Content</div>
          </div>
        </button>
      </div>
    </div>
  </div>
</div>

<div class="scicomm-impact">
  <div class="scicomm-container">
    <h2><span class="neuro-text">reach &</span> <span class="forager-text">impact</span></h2>
    
    <div class="impact-grid">
      <div class="impact-card">
        <div class="impact-stat">3K</div>
        <div class="impact-label">Followers across Twitter & LinkedIn</div>
        <div class="impact-links">
          <a href="https://x.com/Neurocuriously" target="_blank" rel="noopener noreferrer" class="social-link">
            <i class="fab fa-x-twitter"></i> @Neurocuriously
          </a>
          <a href="https://www.linkedin.com/in/paula-g%C3%B3mez-sotres-722242151/" target="_blank" rel="noopener noreferrer" class="social-link">
            <i class="fab fa-linkedin"></i> LinkedIn
          </a>
        </div>
      </div>
      <div class="impact-card">
        <div class="impact-stat">~200</div>
        <div class="impact-label">Students reached across 4 highschools</div>
        <div class="impact-detail">IES La Serna, IES Isaac Albéniz, + 2 French institutes (INSERM)</div>
      </div>
      <div class="impact-card">
        <div class="impact-stat">>300</div>
        <div class="impact-label">Citizens reached in Science Week events</div>
        <div class="impact-detail">Interactive workshops, EEG demonstrations, all ages</div>
      </div>
    </div>

    <div class="impact-section">
      <h3>Outreach Publications & Media</h3>
      <p class="impact-subsection-text">Featured in peer-reviewed science communication:</p>
      <ul class="impact-list">
        <li><strong>Neuron Preview</strong> co-author (with Sara Mederos) — 2024</li>
        <li><strong>Spanish Cannabinoid Society</strong> newsletter — featured (multiple times)</li>
        <li><strong>2 book chapters</strong> on science communication & public engagement</li>
        <li>Speaking to diverse audiences: teenagers, high schoolers, retirees, families</li>
      </ul>
    </div>

    <div class="impact-section">
      <h3>Featured Media</h3>
      <div class="media-container">
        <p class="impact-subsection-text">Science communication in action:</p>
        <div class="video-embed">
          <iframe width="100%" height="315" src="https://www.youtube.com/embed/cVDPOtPTADY" title="Neurocuriously - Science Communication" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
      </div>
    </div>

  </div>
</div>

  </main>
</div>

<div class="story-popup-overlay" id="storyPopupOverlay">
  <div class="story-popup">
    <button class="story-popup-close" onclick="toggleStoryPopup()">×</button>
    
    <h2>The Beginning</h2>
    <p>
      My passion for science communication was ignited at a particular event in 2012: "Universidad en la Calle" in Madrid, where a neuroscientist gave a talk on the street about the topic of endocannabinoids. That spark led me to create bioUAMcabreada on Twitter: a biology humor account that grew to nearly 3,000 followers. At university, everyone knew my "party trick" was talking about science. </p>
    <p>
      At the beginning of my doctoral research in France, I realized something crucial: I could do science communication, but a language barrier was holding me back from reaching French audiences. So during by visits back home in Spain I visited two high schools (IES La Serna and IES Isaac Albéniz) where I gave talks blending my career path with my ongoing research. But here's what mattered: I spoke in Spanish. About my Erasmus journey (both undergraduate and Erasmus Mundus for my master's). About my research. About why science matters. And the connection was immediate. Students leaned in. Eyes lit up. These visits were crucial: they taught me that language is not a barrier—it's a bridge. When I communicated in Spanish, my native language, everything felt more authentic, more accessible, more real. 
    </p>
    <p>
      Back in France, I invested heavily in improving my communication skills. I took a Public Speaking course at the Université de Bordeaux and competed in "Ma Thèse en 180," where I was a finalist. These experiences built my confidence from the ground up. Once I felt ready, I reached out to INSERM's science communication team. to participate in the outreach activities they organized. With INSERM's support, I gave seminars at French institutes for teenagers, explaining how the brain processes smell and emotion. I also participated in Fête de la Science with an interactive workshop at the Merignac public library where I explained emotions and odors go hand-in-hand (or better said, nose-to-nose) to audiences ranging from children to retirees. Every interaction taught me something new about how to adapt my message to different audiences. 
    </p>
    <p>
      Today, I'm in Barcelona, improving my Catalan to serve my local community in yet another language. I'm developing a cycle of talks with Centro Cívico Pou de la Figuera (Born neighborhood) with activities for all audiences about topics like emotions, endocannabinoids, and memory. I also help NeuCompLab members with our  workshops during Science Week, where we show the public how we use brain measurements in our mouse research. Each event, each audience, each moment is an opportunity to adapt, translate, and connect. 
    </p>

    <h2>The Through-Line</h2>
    <p>
      What ties all of this together? <strong>Adaptation.</strong> Language was never a barrier—it became my superpower. Spanish for students in Madrid. French for French teenagers. English for international collaborations. And now Catalan for my Barcelona community. But it's not just about languages. It's also about <strong>formats</strong>. Social media posts, formal talks, interactive workshops, scientific previews, book chapters, community events. Every person learns differently, connects differently, gets inspired differently.
    </p>
    <p>
      That's what Neurocuriously is really about: <strong>meeting people where they are</strong>—in their language, through their preferred medium. And that's why I'll keep learning, keep adapting, and keep finding new ways to make science stick.
    </p>
  </div>
</div>

<div class="card-overlay" id="cardOverlay"></div>
<div class="card-popup" id="cardPopup">
  <button class="popup-close" onclick="closeCard()">×</button>
  <div class="popup-image" id="popupImage"></div>
  <div class="popup-title" id="popupTitle"></div>
  <div class="popup-description" id="popupDescription"></div>
  <a href="#" class="popup-link" id="popupLink">Learn more →</a>
</div>

<script>
function toggleStoryPopup() {
  const overlay = document.getElementById('storyPopupOverlay');
  overlay.classList.toggle('active');
}

document.getElementById('storyPopupOverlay').addEventListener('click', (e) => {
  if (e.target.id === 'storyPopupOverlay') {
    toggleStoryPopup();
  }
});

const activities = [
  {
    id: 0,
    emoji: '🔬',
    imageUrl: null,
    title: 'Laboratory Visits',
    description: 'Take students on guided tours through our neuroscience lab. See real equipment, meet researchers, and understand what actually happens behind the scenes of cutting-edge science.',
    link: 'https://www.linkedin.com/posts/paula-gómez-sotres-722242151_yesterday-i-had-the-pleasure-of-visiting-activity-7381714000541200384-rnPq'
  },
  {
    id: 1,
    emoji: '🎓',
    imageUrl: null,
    title: 'Educational Workshops',
    description: 'Interactive hands-on sessions teaching neuroscience fundamentals through experiments, brain models, and live demonstrations for students of all ages.',
    link: '#'
  },
  {
    id: 2,
    emoji: '📺',
    imageUrl: null,
    title: 'Video Series',
    description: 'Engaging short-form videos breaking down complex neuroscience concepts into digestible, entertaining content for social media and online audiences.',
    link: '#'
  },
  {
    id: 3,
    emoji: '🎤',
    imageUrl: null,
    title: 'Public Talks',
    description: 'Engaging lectures and presentations at schools, libraries, and community events discussing the latest neuroscience discoveries in an accessible way.',
    link: '#'
  },
  {
    id: 4,
    emoji: '🧬',
    imageUrl: null,
    title: 'Online Content',
    description: 'Blog posts, podcasts, and interactive visualizations explaining neuroscience phenomena, research breakthroughs, and the brain in everyday life.',
    link: '#'
  }
];

function drawConnections() {
  const svg = document.getElementById('network-lines');
  svg.innerHTML = '';
  
  const wrapper = document.querySelector('.bubble-network-wrapper');
  const buttons = document.querySelectorAll('.bubble-button');
  
  const w = wrapper.clientWidth;
  const h = wrapper.clientHeight;
  
  svg.setAttribute('viewBox', `0 0 ${w} ${h}`);
  
  const positions = [];
  buttons.forEach((btn, idx) => {
    const rect = btn.getBoundingClientRect();
    const wrapperRect = wrapper.getBoundingClientRect();
    
    const x = ((rect.left - wrapperRect.left) + rect.width / 2) / w * 100;
    const y = ((rect.top - wrapperRect.top) + rect.height / 2) / h * 100;
    
    positions[idx] = { x, y };
  });
  
  const connections = [
    [0, 1], [0, 2], [0, 3], [0, 4],
    [1, 2], [1, 3], [1, 4],
    [2, 3], [2, 4],
    [3, 4]
  ];
  
  connections.forEach(([from, to]) => {
    if (positions[from] && positions[to]) {
      const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      line.setAttribute('x1', positions[from].x + '%');
      line.setAttribute('y1', positions[from].y + '%');
      line.setAttribute('x2', positions[to].x + '%');
      line.setAttribute('y2', positions[to].y + '%');
      line.setAttribute('stroke', 'rgba(177, 59, 255, 0.2)');
      line.setAttribute('stroke-width', '1.5');
      line.setAttribute('stroke-dasharray', '5,5');
      svg.appendChild(line);
    }
  });
}

function openCard(id) {
  const activity = activities[id];
  const imageContainer = document.getElementById('popupImage');
  
  if (activity.imageUrl) {
    imageContainer.innerHTML = `<img src="${activity.imageUrl}" alt="${activity.title}">`;
  } else {
    imageContainer.innerHTML = activity.emoji;
  }
  
  document.getElementById('popupTitle').textContent = activity.title;
  document.getElementById('popupDescription').textContent = activity.description;
  document.getElementById('popupLink').href = activity.link;
  
  document.getElementById('cardPopup').classList.add('active');
  document.getElementById('cardOverlay').classList.add('active');
}

function closeCard() {
  document.getElementById('cardPopup').classList.remove('active');
  document.getElementById('cardOverlay').classList.remove('active');
}

document.querySelectorAll('.bubble-button').forEach(btn => {
  btn.addEventListener('click', (e) => {
    openCard(parseInt(btn.dataset.id));
  });
});

document.getElementById('cardOverlay').addEventListener('click', closeCard);

setTimeout(() => {
  drawConnections();
  window.addEventListener('resize', drawConnections);
}, 100);
</script>