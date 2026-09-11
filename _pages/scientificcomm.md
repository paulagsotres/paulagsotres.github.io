---
title: "Neurocuriously"
layout: splash
permalink: /scientificcomm/
author_profile: true
---

<!-- ================= HERO ================= -->
<div class="scicomm-wrapper">
  <aside class="scicomm-sidebar">
    <img src="/images/neurocuriously-banner.png" alt="Neurocuriously - Paula Gómez-Sotres" class="scicomm-banner-img">
  </aside>

  <main class="scicomm-main">

<!-- ================= ABOUT NEUROCURIOUSLY ================= -->
<div class="scicomm-about">
  <div class="scicomm-container">
    <h1>Neurocuriously</h1>
    <p class="scicomm-tagline">Making neuroscience accessible to everyone</p>
    
    <h2>What is Neurocuriously?</h2>
    <p>
      Neurocuriously is my commitment to making neuroscience accessible, engaging, and relevant. Through talks, workshops, and public engagement activities, I bridge the gap between cutting-edge brain research and broader audiences. Science communication isn't just about sharing knowledge—it's about inspiring curiosity and showing how neuroscience impacts our everyday lives.
    </p>
  </div>
</div>


<!-- ================= ACTIVITIES ================= -->
<div class="scicomm-activities">
  <div class="scicomm-container">
    <h2>Activities & Outreach</h2>
    
    <div class="activity-cards-grid">
      
      <!-- ACTIVITY 1 -->
      <article class="activity-card">
        <div class="activity-image">
          <img src="/images/activity-1.jpg" alt="Laboratory Visit">
        </div>
        <div class="activity-content">
          <h3>Laboratory Visits & Demonstrations</h3>
          <p>Bringing students and curious minds into the lab to experience neuroscience research firsthand. Hands-on demonstrations of electrophysiology, behavioral tracking, and neural imaging techniques.</p>
          <a href="https://www.linkedin.com/posts/paula-gómez-sotres-722242151_yesterday-i-had-the-pleasure-of-visiting-activity-7381714000541200384-rnPq" target="_blank" class="activity-link">Read More →</a>
        </div>
      </article>

      <!-- ACTIVITY 2 -->
      <article class="activity-card">
        <div class="activity-image">
          <img src="/images/activity-2.jpg" alt="Fête de la Science">
        </div>
        <div class="activity-content">
          <h3>Fête de la Science: Brain & Nutrition</h3>
          <p>How does your brain control what you eat? Exploring the neural mechanisms behind obesity and appetite regulation at France's largest science festival.</p>
          <a href="https://www.fetedelascience.fr/obesite-et-nutrition-role-du-cerveau" target="_blank" class="activity-link">Learn More →</a>
        </div>
      </article>

      <!-- ACTIVITY 3 - TEMPLATE FOR USER TO FILL -->
      <article class="activity-card">
        <div class="activity-image">
          <img src="/images/activity-3.jpg" alt="Coming Soon">
        </div>
        <div class="activity-content">
          <h3>Your Activity Title Here</h3>
          <p>Add description of your outreach activity here. Include what the event was about, who attended, and what key concepts were discussed.</p>
          <a href="#" class="activity-link">Learn More →</a>
        </div>
      </article>

      <!-- ACTIVITY 4 - TEMPLATE FOR USER TO FILL -->
      <article class="activity-card">
        <div class="activity-image">
          <img src="/images/activity-4.jpg" alt="Coming Soon">
        </div>
        <div class="activity-content">
          <h3>Another Activity Title</h3>
          <p>Add description of your outreach activity here. Include what the event was about, who attended, and what key concepts were discussed.</p>
          <a href="#" class="activity-link">Learn More →</a>
        </div>
      </article>

    </div>
  </div>
</div>


<!-- ================= FUTURE PROJECTS ================= -->
<div class="scicomm-future">
  <div class="scicomm-container">
    <h2>Future Projects</h2>
    
    <div class="future-projects-grid">
      
      <article class="future-project-card">
        <div class="future-project-icon">📚</div>
        <h3>Interactive Brain Workshops</h3>
        <p>Developing hands-on workshops for schools exploring how the brain processes social information and makes decisions.</p>
      </article>

      <article class="future-project-card">
        <div class="future-project-icon">🎬</div>
        <h3>Science Video Series</h3>
        <p>Creating short, engaging videos explaining key neuroscience concepts—from synaptic plasticity to social bonding mechanisms.</p>
      </article>

      <article class="future-project-card">
        <div class="future-project-icon">🎤</div>
        <h3>Science Communication Network</h3>
        <p>Building a community of neuroscientists committed to public engagement and accessible science communication.</p>
      </article>

    </div>
  </div>
</div>

  </main>
</div>


<!-- ================= STYLES ================= -->
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

* {
  font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

/* ================= LAYOUT ================= */
.scicomm-wrapper {
  display: grid;
  grid-template-columns: 380px 1fr;
  gap: 0;
  min-height: 100vh;
}

.scicomm-sidebar {
  position: sticky;
  top: 0;
  width: 380px;
  background: #000000;
  border-right: 2px solid #B13BFF;
  padding: 0;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  height: 100vh;
  overflow-y: auto;
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
}

/* ================= HERO ================= */
.scicomm-hero {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  background: linear-gradient(135deg, rgba(177, 59, 255, 0.1) 0%, rgba(0, 0, 0, 0.8) 100%);
  border: 1px solid rgba(177, 59, 255, 0.25);
  border-radius: 8px;
  color: white;
  padding: 80px 40px;
  margin-bottom: 60px;
  overflow: hidden;
}

.scicomm-hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
}

.scicomm-hero h1 {
  font-size: 3rem;
  margin: 0 0 12px 0;
  font-weight: 700;
  letter-spacing: -0.5px;
  line-height: 1.1;
}

.scicomm-subtitle {
  font-size: 1.1rem;
  opacity: 0.95;
  font-weight: 400;
  letter-spacing: 0.5px;
  color: #c8c8c8;
}

/* ================= CONTAINER ================= */
.scicomm-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 20px;
}

/* ================= ABOUT SECTION ================= */
.scicomm-about {
  margin-bottom: 80px;
  margin-top: 0;
}

.scicomm-about h1 {
  color: #B13BFF;
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

/* ================= ACTIVITIES ================= */
.scicomm-activities {
  margin-bottom: 80px;
}

.scicomm-activities h2 {
  color: #ffffff;
  font-size: 2rem;
  margin-bottom: 36px;
  font-weight: 700;
  letter-spacing: -0.3px;
}

.activity-cards-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 28px;
}

.activity-card {
  background: #000000;
  border: 1px solid rgba(177, 59, 255, 0.12);
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.3s ease;
}

.activity-card:hover {
  border-color: rgba(177, 59, 255, 0.25);
  background: rgba(177, 59, 255, 0.03);
  box-shadow: 0 6px 16px rgba(177, 59, 255, 0.1);
  transform: translateY(-3px);
}

.activity-image {
  width: 100%;
  height: 220px;
  overflow: hidden;
  background: #1a1a1a;
}

.activity-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.activity-card:hover .activity-image img {
  transform: scale(1.05);
}

.activity-content {
  padding: 24px;
}

.activity-card h3 {
  color: #ffffff;
  font-size: 1.1rem;
  margin: 0 0 12px 0;
  font-weight: 700;
  line-height: 1.3;
}

.activity-card p {
  color: #a8a8a8;
  font-size: 0.9rem;
  line-height: 1.6;
  margin: 0 0 14px 0;
}

.activity-link {
  color: #B13BFF;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.85rem;
  transition: all 0.3s ease;
  display: inline-block;
  border-bottom: 1px solid rgba(177, 59, 255, 0.3);
}

.activity-link:hover {
  color: #39FF14;
  border-bottom-color: #39FF14;
}

/* ================= FUTURE PROJECTS ================= */
.scicomm-future {
  margin-bottom: 40px;
}

.scicomm-future h2 {
  color: #ffffff;
  font-size: 2rem;
  margin-bottom: 36px;
  font-weight: 700;
  letter-spacing: -0.3px;
}

.future-projects-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.future-project-card {
  background: #000000;
  border: 1px solid rgba(177, 59, 255, 0.12);
  border-left: 3px solid #B13BFF;
  border-radius: 8px;
  padding: 28px 24px;
  text-align: center;
  transition: all 0.3s ease;
}

.future-project-card:hover {
  border-color: rgba(177, 59, 255, 0.25);
  background: rgba(177, 59, 255, 0.03);
  box-shadow: 0 6px 16px rgba(177, 59, 255, 0.1);
  transform: translateY(-3px);
}

.future-project-icon {
  font-size: 2.5rem;
  margin-bottom: 12px;
  display: block;
}

.future-project-card h3 {
  color: #ffffff;
  font-size: 1rem;
  margin: 0 0 12px 0;
  font-weight: 700;
  line-height: 1.3;
}

.future-project-card p {
  color: #a8a8a8;
  font-size: 0.85rem;
  line-height: 1.6;
  margin: 0;
}

/* ================= RESPONSIVE ================= */
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
}

@media (max-width: 768px) {
  .scicomm-hero h1 {
    font-size: 2rem;
  }

  .scicomm-about h2,
  .scicomm-activities h2,
  .scicomm-future h2 {
    font-size: 1.6rem;
  }

  .activity-cards-grid {
    grid-template-columns: 1fr;
  }

  .future-projects-grid {
    grid-template-columns: 1fr;
  }

  .scicomm-about p {
    font-size: 0.9rem;
  }

  .scicomm-main {
    padding: 30px 15px;
  }
}

@media (max-width: 480px) {
  .scicomm-hero {
    padding: 50px 20px;
  }

  .scicomm-hero h1 {
    font-size: 1.6rem;
  }

  .scicomm-subtitle {
    font-size: 0.95rem;
  }

  .scicomm-sidebar {
    height: 300px;
  }

  .scicomm-main {
    padding: 20px 15px;
  }
}

</style>