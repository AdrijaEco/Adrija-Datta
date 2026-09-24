#!/usr/bin/env python3
"""Refresh additional publications using an ORCID-matched OpenAlex author."""
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ORCID = "0000-0002-1971-229X"
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "publications.json"
FEATURED_DOIS = {"10.1038/s41467-026-72636-w", "10.1038/s43247-025-02924-8"}


def get_json(url):
    request = Request(url, headers={"User-Agent": "AdrijaDattaAcademicSite/1.0 (public research metadata)", "Accept": "application/json"})
    with urlopen(request, timeout=25) as response:
        return json.load(response)


def collect(fetch=get_json):
    # Resolve an author by exact ORCID, then use the OpenAlex author identifier.
    author = fetch("https://api.openalex.org/authors/https://orcid.org/" + ORCID)
    author_id = author.get("id", "").rsplit("/", 1)[-1]
    if not author_id.startswith("A") or author.get("orcid", "").rsplit("/", 1)[-1] != ORCID:
        raise ValueError("OpenAlex did not return the expected ORCID author")
    params = urlencode({"filter": "author.id:" + author_id, "per-page": "100", "sort": "publication_date:desc"})
    results = fetch("https://api.openalex.org/works?" + params).get("results", [])
    works, seen = [], set()
    for item in results:
        doi = (item.get("doi") or "").removeprefix("https://doi.org/").lower()
        if doi in FEATURED_DOIS or (doi and doi in seen):
            continue
        title = item.get("display_name") or item.get("title")
        year = item.get("publication_year")
        if not title or not isinstance(year, int) or year < 2020:
            continue
        if doi:
            seen.add(doi)
        venue = (((item.get("primary_location") or {}).get("source") or {}).get("display_name") or "Research output")
        link = item.get("doi") or item.get("primary_location", {}).get("landing_page_url") or item.get("id")
        if not link or not str(link).startswith("https://"):
            continue
        works.append({"title": title.strip(), "year": year, "venue": venue, "url": link})
    # An empty API result is likely a temporary indexing or API issue: do not erase the page.
    if not works:
        raise ValueError("No additional works found; preserving existing publications.json")
    return works[:20]


def main():
    works = collect()
    previous = json.loads(OUTPUT.read_text()) if OUTPUT.exists() else {}
    if previous.get("works") == works:
        print("No publication changes")
        return
    payload = {"source": "OpenAlex, author matched by ORCID " + ORCID, "updated": datetime.now(timezone.utc).date().isoformat(), "works": works}
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(f"Saved {len(works)} additional works")


if __name__ == "__main__":
    main()
