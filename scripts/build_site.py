#!/usr/bin/env python3
"""Build the production WAKANDABOY100 static pages from shared templates."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://wakandaboy100.com"
OG = f"{SITE}/og-image.png?v=4"
MEDIA = json.loads((ROOT / "content/media.json").read_text(encoding="utf-8"))

SOCIALS = [
    ("YouTube", "https://www.youtube.com/@wakandaboy100"),
    ("Instagram", "https://www.instagram.com/wakandaboy100/"),
    ("Facebook", "https://www.facebook.com/WakandaBoy100"),
    ("X", "https://x.com/WakandaBoy100"),
    ("TikTok", "https://www.tiktok.com/@wakandaboy100"),
    ("SoundCloud", "https://soundcloud.com/user-684213263"),
]

NAV = [
    ("Home", "/", "home"),
    ("About", "/about/", "about"),
    ("Videos", "/videos/", "videos"),
    ("Music", "/music/", "music"),
    ("Booking", "/booking/", "booking"),
    ("Merch", "/merch/the-ultimate-cardio/", "merch"),
]

PERSON = {
    "@type": "Person",
    "@id": f"{SITE}/#collins-wewa",
    "name": "Collins Wewa",
    "alternateName": ["WAKANDABOY100", "Collins Wewa TV"],
    "url": f"{SITE}/about/",
    "image": f"{SITE}/assets/images/wakandaboy100-dancer.svg",
    "description": "Collins Wewa, known as WAKANDABOY100, is an independent artist and performer working across music, dance, comedy, video, and live entertainment.",
    "sameAs": [url for _, url in SOCIALS] + [
        "https://open.spotify.com/artist/25qMYd4ZAObBWwLwT7K1Jy",
        "https://music.apple.com/us/artist/wakandaboy100/1559091732",
        "https://audiomack.com/wakandaboy100/song/how-it-used-to-be",
        "https://www.pandora.com/artist/wakandaboy100/dance-with-me-single/dance-with-me/TRpqqpvXfdcJp3J",
    ],
}


def header(active: str) -> str:
    links = []
    for label, url, key in NAV:
        current = ' aria-current="page"' if key == active else ""
        links.append(f'<a href="{url}"{current}>{label}</a>')
    return f"""
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="nav-shell">
    <a class="brand" href="/" aria-label="WAKANDABOY100 home">
      <span class="brand-mark"><img src="/assets/images/wakandaboy100-dancer.svg" alt="" width="31" height="36"></span>
      <span class="brand-name">WAKANDABOY100</span>
    </a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" data-menu-toggle>Menu</button>
    <nav class="site-nav" id="site-nav" aria-label="Primary navigation" data-site-nav>
      {''.join(links)}
      <a class="watch-link" href="https://www.youtube.com/watch?v=EUQzS9nLWl8" target="_blank" rel="noopener">Watch</a>
    </nav>
  </div>
</header>"""


def footer() -> str:
    social_links = "".join(
        f'<a href="{url}" target="_blank" rel="noopener">{label}</a>' for label, url in SOCIALS
    )
    return f"""
<footer class="site-footer">
  <div class="shell footer-shell">
    <img class="footer-art" src="/assets/images/wakandaboy100-dancer.svg" alt="" aria-hidden="true">
    <p class="eyebrow">Independent artist portfolio</p>
    <h2 class="display">WAKANDABOY<span style="color:transparent;-webkit-text-stroke:2px #e9e9ea">100</span></h2>
    <p class="artist-line">Collins Wewa · Comedy · Music · Dance</p>
    <div class="footer-links">{social_links}</div>
    <div class="footer-base"><span>© <span data-year></span> WAKANDABOY100. All rights reserved.</span><span class="mono">wakandaboy100.com</span></div>
  </div>
</footer>
<script src="/script.js" defer></script>"""


def schema_for(path: str, page_type: str, title: str, description: str, extra: dict | None = None) -> dict:
    page_id = f"{SITE}{path}#webpage"
    website = {
        "@type": "WebSite",
        "@id": f"{SITE}/#website",
        "name": "WAKANDABOY100",
        "alternateName": "Collins Wewa",
        "url": f"{SITE}/",
        "publisher": {"@id": PERSON["@id"]},
    }
    page = {
        "@type": page_type,
        "@id": page_id,
        "url": f"{SITE}{path}",
        "name": title,
        "description": description,
        "isPartOf": {"@id": website["@id"]},
        "about": {"@id": PERSON["@id"]},
        "primaryImageOfPage": {"@type": "ImageObject", "url": OG},
    }
    if extra:
        page.update(extra)
    return {"@context": "https://schema.org", "@graph": [website, PERSON, page]}


def document(*, title: str, description: str, path: str, active: str, body: str, page_type: str = "WebPage", schema_extra: dict | None = None) -> str:
    canonical = f"{SITE}{path}"
    schema = schema_for(path, page_type, title, description, schema_extra)
    safe_title = html.escape(title, quote=True)
    safe_desc = html.escape(description, quote=True)
    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{safe_title}</title>
  <meta name="description" content="{safe_desc}">
  <meta name="theme-color" content="#15151a">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" type="image/png" href="/favicon.png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="preload" href="/assets/fonts/anton-400.ttf" as="font" type="font/ttf" crossorigin>
  <link rel="preload" href="/assets/fonts/barlow-condensed-700.ttf" as="font" type="font/ttf" crossorigin>
  <link rel="stylesheet" href="/style.css">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="WAKANDABOY100">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{safe_title}">
  <meta property="og:description" content="{safe_desc}">
  <meta property="og:image" content="{OG}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="WAKANDABOY100 — Collins Wewa, independent artist and performer">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{safe_title}">
  <meta name="twitter:description" content="{safe_desc}">
  <meta name="twitter:image" content="{OG}">
  <script type="application/ld+json">{json.dumps(schema, separators=(',', ':'))}</script>
</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
"""
    depth = len([part for part in path.strip("/").split("/") if part])
    prefix = "./" if depth == 0 else "../" * depth
    return page.replace('href="/', f'href="{prefix}').replace('src="/', f'src="{prefix}')


def media_cards(items: list[dict]) -> str:
    cards = []
    for item in items:
        title = html.escape(item["title"])
        platform = html.escape(item["platform"])
        url = html.escape(item["url"], quote=True)
        thumbnail = html.escape(item["thumbnail"], quote=True)
        description = html.escape(item.get("description", ""))
        cards.append(
            f'<a class="work-card" href="{url}" target="_blank" rel="noopener">'
            f'<img loading="lazy" src="{thumbnail}" alt="{title} comedy skit cover" width="1200" height="675">'
            f'<div class="card-body"><span class="kicker">{platform}</span><h3>{title}</h3><p>{description}</p></div></a>'
        )
    return "".join(cards)


HOME = """
<section class="shell hero" aria-labelledby="home-title">
  <div>
    <p class="eyebrow">Independent artist · Performer · Creator</p>
    <h1 class="display" id="home-title">WAKANDABOY<span class="outline">100</span></h1>
    <p class="artist-line">Collins Wewa / Comedy · Music · Dance</p>
    <p class="lede">WAKANDABOY100 is Collins Wewa—a high-energy independent performer turning music, movement, comedy, and personality into moments people replay.</p>
    <div class="actions">
      <a class="button primary" href="https://www.youtube.com/watch?v=EUQzS9nLWl8" target="_blank" rel="noopener">Watch “My Baby”</a>
      <a class="button" href="/merch/the-ultimate-cardio/">Explore the merch</a>
    </div>
    <dl class="stats" aria-label="Public catalog snapshot">
      <div><dt>316K+</dt><dd>Views on “My Baby”</dd></div>
      <div><dt>95+</dt><dd>YouTube uploads</dd></div>
      <div><dt>87</dt><dd>Short-form videos</dd></div>
    </dl>
  </div>
  <div class="hero-art" aria-label="WAKANDABOY100 dancer mark">
    <span class="ghost-number" aria-hidden="true">100</span>
    <img class="dancer" src="/assets/images/wakandaboy100-dancer.svg" alt="WAKANDABOY100 dancer mark" width="510" height="600">
    <span class="art-label">The Ultimate Cardio</span><span class="art-footer">Independent · Presented pro</span>
  </div>
</section>
<div class="marquee" aria-hidden="true"><div class="marquee-track"><span>Comedy <b>✦</b> Music <b>✦</b> Dance <b>✦</b> The Ultimate Cardio <b>✦</b> Comedy <b>✦</b> Music <b>✦</b> Dance <b>✦</b> The Ultimate Cardio <b>✦</b></span><span>Comedy <b>✦</b> Music <b>✦</b> Dance <b>✦</b> The Ultimate Cardio <b>✦</b> Comedy <b>✦</b> Music <b>✦</b> Dance <b>✦</b> The Ultimate Cardio <b>✦</b></span></div></div>
<section class="shell section" aria-labelledby="selected-work-title">
  <div class="section-head"><div><p class="eyebrow">Selected work</p><h2 class="display" id="selected-work-title">Music videos, sets<br>and short-form</h2></div><a class="button" href="/videos/">View all videos →</a></div>
  <article class="feature-card">
    <a class="video-poster" href="https://www.youtube.com/watch?v=EUQzS9nLWl8" target="_blank" rel="noopener" aria-label="Watch Collins Wewa — My Baby on YouTube"><img src="https://i.ytimg.com/vi/EUQzS9nLWl8/maxresdefault.jpg" alt="Collins Wewa — My Baby official music video" width="1280" height="720"><span class="play-badge">Play</span></a>
    <div class="feature-meta"><div><p class="eyebrow">Flagship release · 316K+ views</p><h3>My Baby</h3></div><a class="button primary" href="https://www.youtube.com/watch?v=EUQzS9nLWl8" target="_blank" rel="noopener">Watch on YouTube</a></div>
  </article>
  <div class="card-grid">
    <a class="work-card" href="https://www.youtube.com/watch?v=6dMGPwwr9bQ" target="_blank" rel="noopener"><img loading="lazy" src="https://i.ytimg.com/vi/6dMGPwwr9bQ/maxresdefault.jpg" alt="Heart Broken music video thumbnail" width="640" height="400"><div class="card-body"><span class="kicker">36K+ views</span><h3>Heart Broken</h3><p>Official music video with performance-driven storytelling.</p></div></a>
    <a class="work-card" href="https://www.youtube.com/watch?v=vwn4TQy9kw8" target="_blank" rel="noopener"><img loading="lazy" src="https://i.ytimg.com/vi/vwn4TQy9kw8/hqdefault.jpg" alt="Pull the Plug music video thumbnail" width="640" height="400"><div class="card-body"><span class="kicker">12K+ views</span><h3>Pull the Plug</h3><p>Produced and choreographed by WAKANDABOY100.</p></div></a>
    <a class="work-card" href="https://www.youtube.com/watch?v=XXKCSIO0yBc" target="_blank" rel="noopener"><img loading="lazy" src="https://i.ytimg.com/vi/XXKCSIO0yBc/maxresdefault.jpg" alt="Dance With Me live performance thumbnail" width="640" height="400"><div class="card-body"><span class="kicker">Live performance</span><h3>Dance With Me</h3><p>A stage-forward performance release.</p></div></a>
  </div>
</section>
<section class="shell section compact" aria-labelledby="stream-home-title"><div class="section-head"><div><p class="eyebrow">Listen everywhere</p><h2 class="display" id="stream-home-title">Stream the catalog</h2></div><a class="button" href="/music/">All platforms →</a></div><div class="platform-grid">
  <a class="platform-card" href="https://open.spotify.com/artist/25qMYd4ZAObBWwLwT7K1Jy" target="_blank" rel="noopener"><span>Spotify</span><span>→</span></a>
  <a class="platform-card" href="https://music.apple.com/us/artist/wakandaboy100/1559091732" target="_blank" rel="noopener"><span>Apple Music</span><span>→</span></a>
  <a class="platform-card" href="https://soundcloud.com/user-684213263" target="_blank" rel="noopener"><span>SoundCloud</span><span>→</span></a>
</div></section>
<section class="shop-band"><div class="shell section shop-grid">
  <div class="shop-image"><img loading="lazy" src="/assets/images/the-ultimate-cardio-campaign.webp" alt="The Ultimate Cardio shirt — front and back" width="1600" height="1200"><span class="drop-badge">Drop 001</span></div>
  <div class="shop-copy"><p class="eyebrow">WAKANDABOY100 merch</p><h2 class="display">The Ultimate<br>Cardio</h2><h3>Drop 001</h3><p>The first WAKANDABOY100 merchandise drop is taking shape. Full release details are coming soon.</p><span class="status-chip">Coming soon</span><div class="actions"><a class="button light" href="/merch/the-ultimate-cardio/">Preview the drop</a></div></div>
</div></section>
"""

ABOUT = """
<section class="page-hero"><div class="shell page-hero-grid"><div><p class="eyebrow">The person behind the stage name</p><h1 class="display">Collins<br>Wewa</h1><p class="lede">Collins Wewa is WAKANDABOY100—an independent artist, dancer, performer, comedian, and creator building a public catalog across music, video, live performance, and short-form entertainment.</p></div><div class="page-mark"><img src="/assets/images/wakandaboy100-dancer.svg" alt="WAKANDABOY100 dancer mark" width="300" height="330"></div></div></section>
<section class="shell section split"><div class="prose"><p class="eyebrow">About WAKANDABOY100</p><h2>Performer first</h2><p>The WAKANDABOY100 identity is built around movement and presence. Music, comedy, choreography, creator videos, and private performances all lead back to the same idea: make the moment feel like a show.</p><h3>Independent by design</h3><p>The catalog is self-directed and public-facing, with official releases and performance proof available through YouTube, streaming services, and social platforms.</p><h3>One name, one entity</h3><p>Collins Wewa, Collins Wewa TV, and WAKANDABOY100 refer to the same artist. This official website is the home that connects those public identities.</p></div><aside class="fact-panel"><h2>Brand pillars</h2><ul class="fact-list"><li><strong>High energy</strong><span>Bold type, movement, physical performance, and immediate impact.</span></li><li><strong>Self-made</strong><span>An independent catalog built in public without waiting for permission.</span></li><li><strong>Playful</strong><span>Comedy and personality keep the work confident without becoming corporate.</span></li><li><strong>Replayable</strong><span>Music videos and short-form moments designed to earn another watch.</span></li></ul></aside></section>
"""

VIDEOS = f"""
<section class="page-hero"><div class="shell page-hero-grid"><div><p class="eyebrow">Official videos and performance proof</p><h1 class="display">Watch the<br>work</h1><p class="lede">Music videos, choreography, live performance, comedy, and short-form personality from Collins Wewa—WAKANDABOY100.</p></div><div class="page-mark"><img src="/assets/images/wakandaboy100-dancer.svg" alt="WAKANDABOY100 dancer mark" width="300" height="330"></div></div></section>
<section class="shell section"><article class="feature-card"><a class="video-poster" href="https://www.youtube.com/watch?v=EUQzS9nLWl8" target="_blank" rel="noopener"><img src="https://i.ytimg.com/vi/EUQzS9nLWl8/maxresdefault.jpg" alt="Collins Wewa — My Baby official music video" width="1280" height="720"><span class="play-badge">Play</span></a><div class="feature-meta"><div><p class="eyebrow">Flagship release · 316K+ views</p><h3>My Baby</h3></div><a class="button primary" href="https://www.youtube.com/watch?v=EUQzS9nLWl8" target="_blank" rel="noopener">Watch now</a></div></article>
<div class="card-grid">
<a class="work-card" href="https://www.youtube.com/watch?v=6dMGPwwr9bQ" target="_blank" rel="noopener"><img loading="lazy" src="https://i.ytimg.com/vi/6dMGPwwr9bQ/maxresdefault.jpg" alt="Heart Broken music video thumbnail" width="640" height="400"><div class="card-body"><span class="kicker">Official music video</span><h3>Heart Broken</h3><p>Performance-driven visual storytelling.</p></div></a>
<a class="work-card" href="https://www.youtube.com/watch?v=vwn4TQy9kw8" target="_blank" rel="noopener"><img loading="lazy" src="https://i.ytimg.com/vi/vwn4TQy9kw8/hqdefault.jpg" alt="Pull the Plug music video thumbnail" width="640" height="400"><div class="card-body"><span class="kicker">Produced and choreographed</span><h3>Pull the Plug</h3><p>A movement-led WAKANDABOY100 release.</p></div></a>
<a class="work-card" href="https://www.youtube.com/watch?v=XXKCSIO0yBc" target="_blank" rel="noopener"><img loading="lazy" src="https://i.ytimg.com/vi/XXKCSIO0yBc/maxresdefault.jpg" alt="Dance With Me performance thumbnail" width="640" height="400"><div class="card-body"><span class="kicker">Live performance</span><h3>Dance With Me</h3><p>A stage-forward performance available across streaming platforms.</p></div></a>
</div>
<div class="section-head" style="margin-top:64px"><div><p class="eyebrow">Comedy skits</p><h2 class="display">Laugh with<br>WAKANDABOY100</h2><p class="intro">Comedy clips stay hosted on their original social platforms while this official site organizes the catalog.</p></div><a class="button" href="https://www.instagram.com/wakandaboyofficial/" target="_blank" rel="noopener">More on Instagram →</a></div>
<div class="card-grid">{media_cards(MEDIA["comedy"])}</div>
<div class="contact-panel"><div><h2>More from Collins Wewa</h2><p>Browse the full long-form catalog or jump directly into short-form creator videos.</p></div><div class="actions"><a class="button primary" href="https://www.youtube.com/@wakandaboy100" target="_blank" rel="noopener">YouTube channel</a><a class="button" href="https://www.youtube.com/@wakandaboy100/shorts" target="_blank" rel="noopener">YouTube Shorts</a></div></div></section>
"""

MUSIC = """
<section class="page-hero"><div class="shell page-hero-grid"><div><p class="eyebrow">WAKANDABOY100 music</p><h1 class="display">Stream the<br>catalog</h1><p class="lede">Follow, save, and listen to Collins Wewa’s releases on the platform you already use.</p></div><div class="page-mark"><img src="/assets/images/wakandaboy100-dancer.svg" alt="WAKANDABOY100 dancer mark" width="300" height="330"></div></div></section>
<section class="shell section"><div class="platform-grid">
<a class="platform-card" href="https://open.spotify.com/artist/25qMYd4ZAObBWwLwT7K1Jy" target="_blank" rel="noopener"><span>Spotify</span><span>→</span></a>
<a class="platform-card" href="https://music.apple.com/us/artist/wakandaboy100/1559091732" target="_blank" rel="noopener"><span>Apple Music</span><span>→</span></a>
<a class="platform-card" href="https://soundcloud.com/user-684213263" target="_blank" rel="noopener"><span>SoundCloud</span><span>→</span></a>
<a class="platform-card" href="https://audiomack.com/wakandaboy100/song/how-it-used-to-be" target="_blank" rel="noopener"><span>Audiomack</span><span>→</span></a>
<a class="platform-card" href="https://www.pandora.com/artist/wakandaboy100/dance-with-me-single/dance-with-me/TRpqqpvXfdcJp3J" target="_blank" rel="noopener"><span>Pandora</span><span>→</span></a>
<a class="platform-card" href="https://www.youtube.com/@wakandaboy100" target="_blank" rel="noopener"><span>YouTube</span><span>→</span></a>
</div><div class="contact-panel"><div><h2>Official artist identity</h2><p>Look for WAKANDABOY100 or Collins Wewa. This page links only to the public artist profiles connected to this official site.</p></div><a class="button primary" href="/about/">About the artist</a></div></section>
"""

BOOKING = """
<section class="page-hero"><div class="shell page-hero-grid"><div><p class="eyebrow">Booking and private events</p><h1 class="display">Bring the<br>energy</h1><p class="lede">Request Collins Wewa—WAKANDABOY100—for birthdays, parties, private events, and performance opportunities.</p></div><div class="page-mark"><img src="/assets/images/wakandaboy100-dancer.svg" alt="WAKANDABOY100 dancer mark" width="300" height="330"></div></div></section>
<section class="shell section"><div class="section-head"><div><p class="eyebrow">Start with the details</p><h2 class="display">Make the request clear</h2></div></div><div class="booking-grid"><article class="booking-card"><span class="num">01</span><h2>Date and city</h2><p>Share the requested date, city, venue, and the time window for the appearance.</p></article><article class="booking-card"><span class="num">02</span><h2>Room and audience</h2><p>Include the event type, expected audience size, age range, and venue format.</p></article><article class="booking-card"><span class="num">03</span><h2>Performance fit</h2><p>Explain whether you are requesting music, comedy, dance, an appearance, or a custom combination.</p></article></div>
<div class="contact-panel"><div><h2>Request through Instagram</h2><p>Send the event date, city, venue, audience size, budget range, and requested performance type. A dedicated booking email can be connected after Wewa’s owner mailbox is verified.</p></div><a class="button primary" href="https://www.instagram.com/wakandaboy100/" target="_blank" rel="noopener">Message @wakandaboy100</a></div></section>
"""

MERCH = """
<section class="page-hero"><div class="shell page-hero-grid"><div><p class="eyebrow">WAKANDABOY100 merchandise</p><h1 class="display">The Ultimate<br>Cardio</h1><p class="lede">Drop 001 from WAKANDABOY100. Full release details are coming soon.</p></div><div class="page-mark"><img src="/assets/images/wakandaboy100-dancer.svg" alt="WAKANDABOY100 dancer mark" width="300" height="330"></div></div></section>
<section class="shell section merch-detail"><div class="shop-image"><img src="/assets/images/the-ultimate-cardio-campaign.webp" alt="The Ultimate Cardio shirt — front and back" width="1600" height="1200"><span class="drop-badge">Drop 001</span></div><div class="prose"><p class="eyebrow">WAKANDABOY100 merch</p><h2>The Ultimate<br>Cardio</h2><p>The first WAKANDABOY100 merchandise drop is taking shape. Launch details and availability will be announced here.</p><div class="actions"><span class="button" aria-disabled="true">Coming soon</span></div></div></section>
<section class="shell section compact" aria-labelledby="drop-gallery-title"><div class="section-head"><div><p class="eyebrow">Drop 001 preview</p><h2 class="display" id="drop-gallery-title">Front / Back</h2></div></div><div class="merch-gallery"><figure><img loading="lazy" src="/assets/images/the-ultimate-cardio-front.webp" alt="Front view of The Ultimate Cardio shirt" width="1200" height="1200"><figcaption>Front</figcaption></figure><figure><img loading="lazy" src="/assets/images/the-ultimate-cardio-back.webp" alt="Back view of The Ultimate Cardio shirt" width="1200" height="1200"><figcaption>Back</figcaption></figure></div></section>
"""

PAGES = [
    ("index.html", dict(title="WAKANDABOY100 (Collins Wewa) | Artist, Performer & Creator", description="Official home of WAKANDABOY100—Collins Wewa. Watch music videos, stream the catalog, request performances, and explore The Ultimate Cardio merchandise.", path="/", active="home", body=HOME, page_type="ProfilePage")),
    ("about/index.html", dict(title="Collins Wewa | About WAKANDABOY100", description="Meet Collins Wewa, the independent artist and performer known as WAKANDABOY100 across music, dance, comedy, video, and live entertainment.", path="/about/", active="about", body=ABOUT, page_type="ProfilePage", schema_extra={"mainEntity": {"@id": PERSON["@id"]}})),
    ("videos/index.html", dict(title="WAKANDABOY100 Videos | Collins Wewa", description="Watch WAKANDABOY100 music videos and performance work by Collins Wewa, including My Baby, Heart Broken, Pull the Plug, and Dance With Me.", path="/videos/", active="videos", body=VIDEOS, page_type="CollectionPage")),
    ("music/index.html", dict(title="WAKANDABOY100 Music | Stream Collins Wewa", description="Stream WAKANDABOY100 music by Collins Wewa on Spotify, Apple Music, SoundCloud, Audiomack, Pandora, and YouTube.", path="/music/", active="music", body=MUSIC, page_type="CollectionPage")),
    ("booking/index.html", dict(title="Book WAKANDABOY100 | Collins Wewa Performances", description="Request Collins Wewa—WAKANDABOY100—for birthdays, parties, private events, appearances, and performance opportunities.", path="/booking/", active="booking", body=BOOKING, page_type="ContactPage")),
    ("merch/the-ultimate-cardio/index.html", dict(title="The Ultimate Cardio by WAKANDABOY100 | Merch", description="Preview The Ultimate Cardio, Drop 001 from Collins Wewa and WAKANDABOY100. Launch details and availability are coming soon.", path="/merch/the-ultimate-cardio/", active="merch", body=MERCH, page_type="CollectionPage")),
]


def main() -> None:
    for relative, kwargs in PAGES:
        target = ROOT / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(document(**kwargs), encoding="utf-8")
        print(relative)


if __name__ == "__main__":
    main()
