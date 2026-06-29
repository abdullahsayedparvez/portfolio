from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Sayed Abdullah — SQL Developer</title>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet"/>
  <style>
    :root {
      --bg:       #0b0f1a;
      --surface:  #111827;
      --border:   #1e2d45;
      --accent:   #00d4ff;
      --accent2:  #0077ff;
      --text:     #e2e8f0;
      --muted:    #64748b;
      --white:    #ffffff;
      --mono:     'JetBrains Mono', monospace;
      --sans:     'Space Grotesk', sans-serif;
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      font-family: var(--sans);
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      overflow-x: hidden;
    }

    /* ── NAV ── */
    nav {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      display: flex; align-items: center; justify-content: space-between;
      padding: 1rem 2.5rem;
      background: rgba(11,15,26,0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
    }
    .nav-logo {
      font-family: var(--mono);
      font-size: 0.9rem;
      color: var(--accent);
      letter-spacing: 0.05em;
    }
    .nav-links { display: flex; gap: 2rem; list-style: none; }
    .nav-links a {
      font-size: 0.85rem;
      font-weight: 500;
      color: var(--muted);
      text-decoration: none;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      transition: color 0.2s;
    }
    .nav-links a:hover { color: var(--accent); }

    /* ── HERO ── */
    .hero {
      min-height: 100vh;
      display: flex; align-items: center;
      padding: 7rem 2.5rem 4rem;
      position: relative;
      overflow: hidden;
    }
    .hero::before {
      content: '';
      position: absolute; top: -200px; right: -200px;
      width: 700px; height: 700px;
      background: radial-gradient(circle, rgba(0,212,255,0.07) 0%, transparent 70%);
      pointer-events: none;
    }
    .hero::after {
      content: '';
      position: absolute; bottom: -100px; left: -100px;
      width: 500px; height: 500px;
      background: radial-gradient(circle, rgba(0,119,255,0.06) 0%, transparent 70%);
      pointer-events: none;
    }
    .hero-inner {
      max-width: 1100px; margin: 0 auto; width: 100%;
      display: grid; grid-template-columns: 1fr auto; gap: 4rem; align-items: center;
    }
    .hero-eyebrow {
      font-family: var(--mono);
      font-size: 0.8rem;
      color: var(--accent);
      letter-spacing: 0.15em;
      text-transform: uppercase;
      margin-bottom: 1.2rem;
    }
    .hero-name {
      font-size: clamp(2.8rem, 6vw, 5rem);
      font-weight: 700;
      color: var(--white);
      line-height: 1.05;
      letter-spacing: -0.02em;
      margin-bottom: 0.6rem;
    }
    .hero-name span {
      background: linear-gradient(90deg, var(--accent), var(--accent2));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero-role {
      font-family: var(--mono);
      font-size: 1.1rem;
      color: var(--muted);
      margin-bottom: 1.8rem;
    }
    .hero-bio {
      font-size: 1rem;
      color: #94a3b8;
      max-width: 540px;
      line-height: 1.75;
      margin-bottom: 2.5rem;
    }
    .hero-cta {
      display: flex; gap: 1rem; flex-wrap: wrap;
    }
    .btn {
      display: inline-flex; align-items: center; gap: 0.5rem;
      padding: 0.75rem 1.5rem;
      border-radius: 6px;
      font-family: var(--sans);
      font-size: 0.9rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s;
      cursor: pointer;
      border: none;
    }
    .btn-primary {
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      color: #000;
    }
    .btn-primary:hover { opacity: 0.85; transform: translateY(-1px); }
    .btn-ghost {
      background: transparent;
      color: var(--accent);
      border: 1px solid var(--border);
    }
    .btn-ghost:hover { border-color: var(--accent); background: rgba(0,212,255,0.05); }

    /* photo */
    .hero-photo {
      width: 240px; height: 240px;
      border-radius: 50%;
      border: 3px solid var(--border);
      object-fit: cover;
      box-shadow: 0 0 0 8px rgba(0,212,255,0.06), 0 0 60px rgba(0,212,255,0.12);
      position: relative;
      flex-shrink: 0;
    }

    /* ── QUERY TICKER ── */
    .ticker-wrap {
      background: var(--surface);
      border-top: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
      padding: 0.75rem 0;
      overflow: hidden;
      white-space: nowrap;
    }
    .ticker-inner {
      display: inline-flex; gap: 3rem;
      animation: ticker 25s linear infinite;
    }
    .ticker-item {
      font-family: var(--mono);
      font-size: 0.78rem;
      color: var(--accent);
      opacity: 0.7;
    }
    @keyframes ticker {
      0%   { transform: translateX(0); }
      100% { transform: translateX(-50%); }
    }

    /* ── SECTIONS ── */
    .section {
      max-width: 1100px;
      margin: 0 auto;
      padding: 5rem 2.5rem;
    }
    .section-label {
      font-family: var(--mono);
      font-size: 0.75rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 0.6rem;
    }
    .section-title {
      font-size: clamp(1.6rem, 3vw, 2.4rem);
      font-weight: 700;
      color: var(--white);
      letter-spacing: -0.02em;
      margin-bottom: 3rem;
    }
    .divider {
      border: none;
      border-top: 1px solid var(--border);
    }

    /* ── STATS ── */
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 1px;
      background: var(--border);
      border: 1px solid var(--border);
      border-radius: 10px;
      overflow: hidden;
      margin-bottom: 5rem;
    }
    .stat-card {
      background: var(--surface);
      padding: 2rem 1.5rem;
      text-align: center;
    }
    .stat-num {
      font-family: var(--mono);
      font-size: 2.4rem;
      font-weight: 700;
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      line-height: 1;
      margin-bottom: 0.4rem;
    }
    .stat-label {
      font-size: 0.78rem;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }

    /* ── SKILLS ── */
    .skills-grid {
      display: flex; flex-wrap: wrap; gap: 0.6rem;
    }
    .skill-tag {
      font-family: var(--mono);
      font-size: 0.8rem;
      padding: 0.4rem 0.9rem;
      border-radius: 4px;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text);
      transition: all 0.18s;
    }
    .skill-tag:hover {
      border-color: var(--accent);
      color: var(--accent);
      background: rgba(0,212,255,0.05);
    }
    .skill-tag.core {
      border-color: rgba(0,212,255,0.3);
      color: var(--accent);
      background: rgba(0,212,255,0.06);
    }

    /* ── EXPERIENCE ── */
    .timeline { display: flex; flex-direction: column; gap: 0; }
    .timeline-item {
      display: grid;
      grid-template-columns: 200px 1fr;
      gap: 2rem;
      padding: 2.5rem 0;
      border-bottom: 1px solid var(--border);
      position: relative;
    }
    .timeline-item:last-child { border-bottom: none; }
    .timeline-date {
      font-family: var(--mono);
      font-size: 0.78rem;
      color: var(--muted);
      padding-top: 0.2rem;
      line-height: 1.5;
    }
    .timeline-date strong {
      display: block;
      color: var(--accent);
      font-size: 0.82rem;
      margin-bottom: 0.25rem;
    }
    .timeline-content h3 {
      font-size: 1.15rem;
      font-weight: 600;
      color: var(--white);
      margin-bottom: 0.2rem;
    }
    .timeline-content .company {
      font-size: 0.85rem;
      color: var(--muted);
      margin-bottom: 1rem;
    }
    .timeline-content ul {
      list-style: none;
      display: flex; flex-direction: column; gap: 0.55rem;
    }
    .timeline-content ul li {
      font-size: 0.9rem;
      color: #94a3b8;
      padding-left: 1.2rem;
      position: relative;
    }
    .timeline-content ul li::before {
      content: '›';
      position: absolute; left: 0;
      color: var(--accent);
      font-weight: 700;
    }

    /* ── PROJECTS ── */
    .projects-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 1.5rem;
    }
    .project-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1.8rem;
      transition: border-color 0.2s, transform 0.2s;
      position: relative;
      overflow: hidden;
    }
    .project-card::before {
      content: '';
      position: absolute; top: 0; left: 0; right: 0; height: 2px;
      background: linear-gradient(90deg, var(--accent), var(--accent2));
      opacity: 0;
      transition: opacity 0.2s;
    }
    .project-card:hover { border-color: rgba(0,212,255,0.3); transform: translateY(-3px); }
    .project-card:hover::before { opacity: 1; }
    .project-icon {
      font-size: 1.6rem; margin-bottom: 1rem;
    }
    .project-card h3 {
      font-size: 1.05rem;
      font-weight: 600;
      color: var(--white);
      margin-bottom: 0.75rem;
    }
    .project-card p {
      font-size: 0.85rem;
      color: #94a3b8;
      line-height: 1.65;
      margin-bottom: 1rem;
    }
    .project-highlights {
      display: flex; flex-wrap: wrap; gap: 0.4rem;
    }
    .badge {
      font-family: var(--mono);
      font-size: 0.7rem;
      padding: 0.2rem 0.6rem;
      border-radius: 3px;
      background: rgba(0,212,255,0.08);
      color: var(--accent);
      border: 1px solid rgba(0,212,255,0.15);
    }

    /* ── EDUCATION ── */
    .edu-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
    }
    .edu-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1.8rem;
    }
    .edu-card .degree {
      font-size: 1rem;
      font-weight: 600;
      color: var(--white);
      margin-bottom: 0.3rem;
    }
    .edu-card .university {
      font-size: 0.85rem;
      color: var(--muted);
      margin-bottom: 0.8rem;
    }
    .edu-meta {
      display: flex; gap: 1rem; flex-wrap: wrap;
    }
    .edu-meta span {
      font-family: var(--mono);
      font-size: 0.78rem;
      color: var(--accent);
    }

    /* ── CONTACT ── */
    .contact-bar {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 2.5rem;
      display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap;
      gap: 1.5rem;
    }
    .contact-bar h3 {
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--white);
      margin-bottom: 0.4rem;
    }
    .contact-bar p {
      font-size: 0.9rem;
      color: var(--muted);
    }
    .contact-links {
      display: flex; gap: 0.75rem; flex-wrap: wrap;
    }

    /* ── FOOTER ── */
    footer {
      border-top: 1px solid var(--border);
      text-align: center;
      padding: 2rem;
      font-family: var(--mono);
      font-size: 0.75rem;
      color: var(--muted);
    }

    /* ── RESPONSIVE ── */
    @media (max-width: 768px) {
      nav { padding: 1rem 1.5rem; }
      .nav-links { display: none; }
      .hero { padding: 6rem 1.5rem 3rem; }
      .hero-inner { grid-template-columns: 1fr; text-align: center; }
      .hero-photo { width: 160px; height: 160px; justify-self: center; }
      .hero-cta { justify-content: center; }
      .section { padding: 3.5rem 1.5rem; }
      .timeline-item { grid-template-columns: 1fr; gap: 0.5rem; }
      .contact-bar { flex-direction: column; }
    }
  </style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="nav-logo">SA // SQL_DEV</div>
  <ul class="nav-links">
    <li><a href="#about">About</a></li>
    <li><a href="#experience">Experience</a></li>
    <li><a href="#projects">Projects</a></li>
    <li><a href="#education">Education</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>

<!-- HERO -->
<section class="hero" id="about">
  <div class="hero-inner">
    <div>
      <p class="hero-eyebrow">// Available for opportunities</p>
      <h1 class="hero-name">Sayed<br><span>Abdullah</span></h1>
      <p class="hero-role">SQL Developer &amp; Database Engineer</p>
      <p class="hero-bio">
        2+ years crafting performant relational databases in MySQL &amp; PostgreSQL.
        I turn messy data into clean schemas, slow queries into fast ones, and business
        requirements into rock-solid database architecture.
      </p>
      <div class="hero-cta">
        <a href="mailto:abdullahsyed940@gmail.com" class="btn btn-primary">Get in Touch</a>
        <a href="https://www.linkedin.com/in/-sayed-abdullah-work/" target="_blank" class="btn btn-ghost">LinkedIn →</a>
        <a href="https://github.com/abdullahsayedparvez" target="_blank" class="btn btn-ghost">GitHub →</a>
      </div>
    </div>
    <img
      src="https://avatars.githubusercontent.com/u/122341379?v=4"
      onerror="this.src='https://ui-avatars.com/api/?name=Sayed+Abdullah&background=111827&color=00d4ff&size=240&font-size=0.35&bold=true'"
      alt="Sayed Abdullah"
      class="hero-photo"
    />
  </div>
</section>

<!-- TICKER -->
<div class="ticker-wrap">
  <div class="ticker-inner">
    <span class="ticker-item">SELECT * FROM achievements WHERE impact = 'high'</span>
    <span class="ticker-item">CREATE INDEX idx_performance ON queries (execution_time ASC)</span>
    <span class="ticker-item">WITH cte AS (SELECT skill, years FROM experience) SELECT * FROM cte</span>
    <span class="ticker-item">ALTER TABLE career ADD COLUMN next_role VARCHAR(255)</span>
    <span class="ticker-item">SELECT * FROM achievements WHERE impact = 'high'</span>
    <span class="ticker-item">CREATE INDEX idx_performance ON queries (execution_time ASC)</span>
    <span class="ticker-item">WITH cte AS (SELECT skill, years FROM experience) SELECT * FROM cte</span>
    <span class="ticker-item">ALTER TABLE career ADD COLUMN next_role VARCHAR(255)</span>
  </div>
</div>

<!-- STATS -->
<div style="max-width:1100px;margin:0 auto;padding:4rem 2.5rem 0;">
  <div class="stats-grid">
    <div class="stat-card"><div class="stat-num">2+</div><div class="stat-label">Years Experience</div></div>
    <div class="stat-card"><div class="stat-num">40-60%</div><div class="stat-label">Query Speedup</div></div>
    <div class="stat-card"><div class="stat-num">1M+</div><div class="stat-label">Records Managed</div></div>
    <div class="stat-card"><div class="stat-num">30+</div><div class="stat-label">SQL Queries Built</div></div>
    <div class="stat-card"><div class="stat-num">25+</div><div class="stat-label">DB Tables Designed</div></div>
    <div class="stat-card"><div class="stat-num">9.1</div><div class="stat-label">GPA (BSc IT)</div></div>
  </div>
</div>

<!-- SKILLS -->
<section class="section">
  <hr class="divider" style="margin-bottom:3.5rem;"/>
  <p class="section-label">// technical skills</p>
  <h2 class="section-title">What I Work With</h2>
  <div class="skills-grid">
    <span class="skill-tag core">MySQL</span>
    <span class="skill-tag core">PostgreSQL</span>
    <span class="skill-tag core">Window Functions</span>
    <span class="skill-tag core">CTEs</span>
    <span class="skill-tag core">Stored Procedures</span>
    <span class="skill-tag">Joins &amp; Subqueries</span>
    <span class="skill-tag">Indexing Strategies</span>
    <span class="skill-tag">Query Optimization</span>
    <span class="skill-tag">Functions &amp; Views</span>
    <span class="skill-tag">Triggers</span>
    <span class="skill-tag">Data Modeling</span>
    <span class="skill-tag">Normalization</span>
    <span class="skill-tag">Constraints</span>
    <span class="skill-tag">Execution Plans</span>
    <span class="skill-tag">ETL Support</span>
    <span class="skill-tag">Role-Based Access Control</span>
    <span class="skill-tag">Backup &amp; Recovery</span>
    <span class="skill-tag">AWS</span>
    <span class="skill-tag">Render Cloud</span>
    <span class="skill-tag">GitHub</span>
  </div>
</section>

<!-- EXPERIENCE -->
<section class="section" id="experience">
  <hr class="divider" style="margin-bottom:3.5rem;"/>
  <p class="section-label">// work experience</p>
  <h2 class="section-title">Career Timeline</h2>
  <div class="timeline">
    <div class="timeline-item">
      <div class="timeline-date">
        <strong>SQL Developer</strong>
        Freelance<br/>May 2025 – Present
      </div>
      <div class="timeline-content">
        <h3>SQL Developer</h3>
        <p class="company">Freelance · Remote</p>
        <ul>
          <li>Designed and managed 5+ relational database schemas using MySQL and PostgreSQL for client applications.</li>
          <li>Developed and optimized 15+ complex SQL queries for reporting, filtering, and business analytics.</li>
          <li>Improved query performance by 40–60% through indexing, restructuring, and execution plan analysis.</li>
          <li>Deployed and maintained 2+ cloud-hosted database applications on Render Cloud.</li>
          <li>Implemented role-based access control for 20+ database users ensuring security and compliance.</li>
        </ul>
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-date">
        <strong>Data Engineer</strong>
        Hikmah Technologies<br/>May 2024 – May 2025
      </div>
      <div class="timeline-content">
        <h3>Data Engineer</h3>
        <p class="company">Hikmah Technologies · Full-time</p>
        <ul>
          <li>Designed and maintained 25+ normalized database tables supporting business-critical applications.</li>
          <li>Created and modified tables, constraints, indexes, and relationships to improve data integrity.</li>
          <li>Conducted data quality checks on 1M+ records, ensuring high accuracy and consistency.</li>
          <li>Reduced report generation time by 50% through query optimization and indexing strategies.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- PROJECTS -->
<section class="section" id="projects">
  <hr class="divider" style="margin-bottom:3.5rem;"/>
  <p class="section-label">// projects</p>
  <h2 class="section-title">Featured Work</h2>
  <div class="projects-grid">
    <div class="project-card">
      <div class="project-icon">📈</div>
      <h3>Automated Trading Strategy</h3>
      <p>Normalized relational database schema for managing trading data, user accounts, and transaction records with 30+ analytical SQL queries for trade performance reporting.</p>
      <div class="project-highlights">
        <span class="badge">CTEs</span>
        <span class="badge">Window Functions</span>
        <span class="badge">Joins</span>
        <span class="badge">Constraints</span>
      </div>
    </div>
    <div class="project-card">
      <div class="project-icon">💍</div>
      <h3>Mehram — Matrimonial Platform</h3>
      <p>Database architecture for profiles, preferences, and matchmaking. 25+ SQL queries for profile search with optimized search functionality improving response time by ~40%.</p>
      <div class="project-highlights">
        <span class="badge">Schema Design</span>
        <span class="badge">Normalization</span>
        <span class="badge">Backup &amp; Recovery</span>
        <span class="badge">40% faster</span>
      </div>
    </div>
    <div class="project-card">
      <div class="project-icon">🔍</div>
      <h3>AuditIsPro</h3>
      <p>Database structures for audit records, compliance tracking, and activity logs. Managed 250K+ audit records with reporting queries reducing execution time by up to 50%.</p>
      <div class="project-highlights">
        <span class="badge">250K+ Records</span>
        <span class="badge">SQL Scripts</span>
        <span class="badge">50% faster</span>
        <span class="badge">Compliance</span>
      </div>
    </div>
    <div class="project-card">
      <div class="project-icon">📊</div>
      <h3>ZCreation Dashboard</h3>
      <img
        src="https://raw.githubusercontent.com/abdullahsayedparvez/Data-analysis/main/zcreation_dashboard.png"
        alt="ZCreation Dashboard Preview"
        style="width:100%;border-radius:6px;margin:0.75rem 0 1rem;border:1px solid var(--border);object-fit:cover;"
        onerror="this.style.display='none'"
      />
      <p>Wrote SQL queries using JOINs, GROUP BY, aggregate functions, filtering, and data transformation to extract and clean raw database tables into a analysis-ready dataset. The processed data was then visualized in a Power BI dashboard.</p>
      <div class="project-highlights">
        <span class="badge">SQL</span>
        <span class="badge">JOINs &amp; Aggregates</span>
        <span class="badge">Data Cleaning</span>
        <span class="badge">Power BI</span>
        <span class="badge">Data Analysis</span>
      </div>
      <a href="https://github.com/abdullahsayedparvez/Data-analysis" target="_blank" class="btn btn-ghost" style="margin-top:1.1rem;font-size:0.8rem;padding:0.5rem 1rem;">View on GitHub →</a>
    </div>
  </div>
</section>

<!-- EDUCATION -->
<section class="section" id="education">
  <hr class="divider" style="margin-bottom:3.5rem;"/>
  <p class="section-label">// education</p>
  <h2 class="section-title">Academic Background</h2>
  <div class="edu-grid">
    <div class="edu-card">
      <div class="degree">Bachelor of Science in Information Technology</div>
      <div class="university">University of Mumbai</div>
      <div class="edu-meta">
        <span>GPA: 9.1</span>
        <span>Feb 2022 – Feb 2024</span>
      </div>
    </div>
    <div class="edu-card">
      <div class="degree">Diploma in Civil Engineering</div>
      <div class="university">MSBTE</div>
      <div class="edu-meta">
        <span>GPA: 7.8</span>
        <span>Jan 2019 – Feb 2022</span>
      </div>
    </div>
  </div>
</section>

<!-- CONTACT -->
<section class="section" id="contact">
  <hr class="divider" style="margin-bottom:3.5rem;"/>
  <div class="contact-bar">
    <div>
      <h3>Let's build something great</h3>
      <p>Open to full-time roles, freelance contracts, and collaborations.</p>
    </div>
    <div class="contact-links">
      <a href="mailto:abdullahsyed940@gmail.com" class="btn btn-primary">abdullahsyed940@gmail.com</a>
      <a href="tel:+919136786290" class="btn btn-ghost">+91 913 678 6290</a>
    </div>
  </div>
</section>

<footer>
  <p>© 2025 Sayed Abdullah · Built with Flask · Mumbai, Maharashtra</p>
</footer>

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def index():
    return HTML

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)