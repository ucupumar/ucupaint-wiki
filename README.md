# Ucupaint Wiki

[Click here](https://ucupumar.github.io/ucupaint-wiki/) to read Ucupaint wiki.

## Build guide

The docs are built and deployed automatically using GitHub actions. However if you want to contribute and test changes locally, you can build the docs manually as such:

1. Get [Python](https://www.python.org/)
2. Enter the project folder
3. Run `pip install -r requirements.txt`
4. Run `mkdocs build` to build the docs
5. You can find the docs in a newly created folder called _"site"_

## Localization

English Markdown is the default source. Existing English URLs stay at the site root.

Add a Simplified Chinese page by creating a sibling file with a `.zh.md` suffix. Example: `docs/01.00.quick-setup.md` (English) and `docs/01.00.quick-setup.zh.md` (Chinese). Untranslated pages are built under `/zh/` from the English source.

Shared images, GIFs, and videos are the default. Ucupaint currently has no localized plugin UI, so the Chinese docs keep using those shared assets that show the English interface. Locale-specific images, GIFs, videos, or subtitles can still override a shared asset. Add an override only when the plugin ships a matching-language UI, or when localized media clearly improves correspondence with the text.

To override one asset for Chinese, add a locale-suffixed file next to it and keep the Markdown path unchanged:

- Shared: `docs/source/01.quick-setup.01.1.png`
- Chinese override: `docs/source/01.quick-setup.01.1.zh.png`
- Markdown (both languages): `./source/01.quick-setup.01.1.png`

The sidebar language control switches to the matching page in the other language.