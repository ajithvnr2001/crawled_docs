#!/usr/bin/env python3
"""Shared guard used by every crawler in this monorepo.

Two things every corpus must agree on:

* a CAPTCHA / OAuth / anti-bot interstitial or a 404 page must **never** be
  written as documentation — raise instead so the page stays in the failed
  table and is retried later;
* root-relative or document-relative image URLs are rewritten to absolute
  URLs at save time so GitHub's Markdown renderer can display them.
"""
from __future__ import annotations

import re
from urllib.parse import urljoin

# Strong anti-bot markers. Deliberately not the bare word "captcha": Turnstile
# and reCAPTCHA product docs mention it legitimately thousands of times. We also
# avoid generic fragments such as "cf-chl-" or "attention required" on their own,
# because Cloudflare's own challenge-product docs contain them in examples.
BLOCK_MARKERS = (
    re.compile(
        r"our systems have detected unusual traffic|"
        r"please type the characters|please enable images|"
        r"google\.com/sorry/image|ai\.google\.dev/oauth2authorize|"
        r"request unsuccessful\. incapsula",
        re.I,
    ),
    re.compile(r"sorry, you have been blocked", re.I),
    re.compile(r"please enable cookies\.", re.I),
    re.compile(r"checking if the site connection is secure", re.I),
    re.compile(r"just a moment\.\.\.", re.I),
    re.compile(r"verify you are human", re.I),
    re.compile(r"complete the security check", re.I),
    re.compile(r"before you continue to google", re.I),
    re.compile(r"enable javascript and cookies to continue", re.I),
)
BLOCK_TITLES = re.compile(
    r"^\s*(attention required!?\s*\|\s*cloudflare|just a moment\.{0,3}|"
    r"sign in - google accounts|redirecting\.{0,3}|"
    r"please wait\.{0,3}|access denied)\s*$",
    re.I,
)
NOTFOUND_TITLE = re.compile(
    r"^\s*(404 not found|page not found|not found|404)\s*$", re.I
)
NOTFOUND_BODY = re.compile(
    r"was not found on this server|"
    r"the page you requested could not be found|"
    r"this page could not be found|"
    r"sorry, we couldn't find that page",
    re.I,
)
IMG_MD = re.compile(r"(!\[[^\]]*\]\()\s*<?([^)\s>]+)")
IMG_HTML = re.compile(r"(<img\b[^>]*\bsrc=[\"'])([^\"']+)", re.I)


def _text_len(text: str) -> int:
    plain = re.sub(r"<[^>]+>", " ", text or "")
    plain = re.sub(r"\s+", " ", plain)
    return len(plain.strip())


def is_block_page(html: str = "", title: str = "") -> bool:
    """True only for a real anti-bot / login interstitial."""
    if BLOCK_TITLES.match(title or ""):
        return True
    t = (title or "").strip().lower()
    if t in {"redirecting...", "sign in - google accounts"}:
        return True
    text = html or ""
    strong = BLOCK_MARKERS[0].search(text[:300000])
    if strong:
        return True
    # Cloudflare / hCaptcha interstitials pair two of the softer markers.
    soft = sum(1 for rx in BLOCK_MARKERS[1:] if rx.search(text[:300000]))
    if soft >= 2:
        return True
    if soft >= 1 and _text_len(text) < 4000:
        return True
    return False


def is_404_page(html: str = "", title: str = "") -> bool:
    if NOTFOUND_TITLE.match((title or "").strip()):
        return True
    if not html:
        return False
    head = html[:30000]
    if re.search(r"<h1[^>]*>\s*404\b", head, re.I):
        return True
    if NOTFOUND_BODY.search(head) and _text_len(head) < 4000:
        return True
    return False


def check_document(html: str, title: str, markdown: str, url: str) -> None:
    """Raise when a fetch produced a block/404 page instead of a document."""
    if is_block_page(html, title) or is_block_page(markdown, title):
        raise RuntimeError(f"blocked page (captcha/oauth/anti-bot): {url}")
    if is_404_page(html, title) or is_404_page(markdown, title):
        raise RuntimeError(f"404 page served with 200: {url}")


def absolutize_images(markdown: str, page_url: str) -> str:
    """Rewrite relative/root-relative image URLs to absolute page-host URLs.

    Fenced code blocks and inline code spans are left untouched so examples that
    literally show ``![alt](image.png)`` are not modified.
    """
    if not markdown or not page_url:
        return markdown

    protected: list[str] = []

    def stash(match: re.Match) -> str:
        protected.append(match.group(0))
        return f"\x00{len(protected) - 1}\x00"

    work = re.sub(r"```.*?```", stash, markdown, flags=re.S)
    work = re.sub(r"~~~.*?~~~", stash, work, flags=re.S)
    work = re.sub(r"`[^`\n]*`", stash, work)

    def fix(raw: str) -> str:
        raw = raw.strip()
        if not raw or raw.startswith(("http://", "https://", "//", "data:", "#")):
            return raw
        # malformed nested markdown: [path](https://...)
        m = re.search(r"\]\((https?://[^)\s]+)\)", raw)
        if m:
            return m.group(1)
        try:
            return urljoin(page_url, raw)
        except Exception:
            return raw

    work = IMG_HTML.sub(lambda m: m.group(1) + fix(m.group(2)), work)
    work = IMG_MD.sub(lambda m: m.group(1) + fix(m.group(2)), work)

    def restore(match: re.Match) -> str:
        return protected[int(match.group(1))]

    return re.sub(r"\x00(\d+)\x00", restore, work)


def strip_tracking(text: str, url: str) -> str:
    """Placeholder for future normalisation hooks."""
    return text
