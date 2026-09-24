# Adrija Datta — academic website

This is a static academic site for GitHub Pages, with a landscape cover, interactive collaborations, and separate journal, preprint, and conference presentation views.

## Review locally

Open `index.html` in a browser. The landscape cover is in `assets/landscape-cover.webp`. Some browsers do not allow `fetch()` of `publications.json` from a local file; the journal, preprint, conference, and collaboration views still work. The automated list works after publication on GitHub Pages.

## Add your portrait

Place a photo you have permission to publish at `assets/portrait.jpg`. Use a vertical crop near a 4:5 aspect ratio. The site will display it automatically; until then it shows an `AD` monogram in the portrait space. Keep the same filename or update both references to it at the end of `index.html`.

## Publish on GitHub Pages

1. In your own GitHub account, create a **public** repository named `YOUR-USERNAME.github.io`, replacing `YOUR-USERNAME` with your exact username.
2. Upload all files and folders from this package to the repository root, preserving `.github/workflows` and `scripts`. GitHub Desktop can preserve the folder structure.
3. Under **Settings → Pages**, choose **Deploy from a branch**, branch `main`, folder `/ (root)`, then save. The website address will be `https://YOUR-USERNAME.github.io/`.
4. Under **Actions → Refresh publications**, run the workflow manually once to check it. It also runs on the first day of each month. If blocked, enable Actions and grant the workflow token write permission under **Settings → Actions → General**.

The monthly update fetches an OpenAlex author matched to ORCID `0000-0002-1971-229X` and updates only the **More indexed works** tab. It does not change your curated journal articles, preprints, conference presentations, biography, position, or collaborators. Update those by editing `index.html` and committing. The Google Scholar link opens your profile, but no Scholar scraping is used. Review automatic records periodically for metadata errors.

The page includes an email address and named collaborators from the supplied CV; check them before publishing publicly. The landscape cover is an illustrative generated image, not a photograph of a documented research site.

## News, SDGs, and portrait

The News section contains verified coverage links as of September 2026. Add new coverage cards in `index.html` under `id="news"`. The SDG selector is an editorial mapping of research topics to relevant UN goals; update its descriptions and goal links in `sdgThemes`. The IUCN figure is specifically about wild bees in Europe, not a global pollinator estimate.

To add your own portrait, save a photo you own or have permission to use as `assets/portrait.jpg` and commit it. The page then displays it automatically. No third-party portrait is bundled because a reusable source and identity could not be verified.
