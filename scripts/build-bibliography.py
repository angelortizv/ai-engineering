#!/usr/bin/env python3
"""Regenerate bibliography/index.md from chapter ## References sections."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_SLUGS = {"bibliography", "book-map", "index"}

CHAPTER_ORDER = [
    "introduction-to-building-ai-applications-with-foundation-models",
    "understanding-foundation-models",
    "evaluation-methodology",
    "evaluating-modern-ai-systems",
    "prompt-engineering",
    "rag-and-agents",
    "finetuning",
    "dataset-engineering",
    "inference-optimization",
    "ai-engineering-architecture-and-user-feedback",
    "glossary",
    "epilogue",
]

INTRO = {
    "en": (
        "Aggregated links from each chapter's **## References** section. "
        "Edit the chapter pages first, then run `python scripts/build-bibliography.py`."
    ),
    "es": (
        "Enlaces agregados de la sección **## References** de cada capítulo. "
        "Edita primero las páginas de capítulo y luego ejecuta "
        "`python scripts/build-bibliography.py`."
    ),
}

TITLE = {"en": "Bibliography", "es": "Bibliografía"}
DESC = {
    "en": "Aggregated references from all chapter notes (Huyen, 2025).",
    "es": "Referencias agregadas de todas las notas por capítulo (Huyen, 2025).",
}
RELATED = {
    "en": "## Related\n\n- [Book map](/ai-engineering/docs/book-map) — reading order and prerequisites\n"
    "- [Overview](/ai-engineering/docs) — chapter index\n"
    "- [Glossary](/ai-engineering/docs/glossary) — key terms\n",
    "es": "## Relacionado\n\n- [Mapa del libro](/ai-engineering/docs/es/book-map) — orden y prerequisitos\n"
    "- [Overview](/ai-engineering/docs/es) — índice de capítulos\n"
    "- [Glosario](/ai-engineering/docs/es/glossary) — términos clave\n",
}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    fm: dict[str, str] = {}
    for line in text[3:end].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, text[end + 3 :].lstrip()


def extract_references(body: str) -> str | None:
    m = re.search(r"^## (?:References|Referencias)\s*$", body, re.MULTILINE)
    if not m:
        return None
    start = m.end()
    rest = body[start:]
    nxt = re.search(r"^## [^#]", rest, re.MULTILINE)
    block = rest[: nxt.start()].strip() if nxt else rest.strip()
    return block or None


def chapter_link(slug: str, locale: str) -> str:
    base = "/ai-engineering/docs"
    if locale == "es":
        return f"{base}/es/{slug}"
    return f"{base}/{slug}" if slug else f"{base}"


def build_locale(locale: str) -> str:
    content_dir = ROOT / "src/content/docs" if locale == "en" else ROOT / "src/content/docs-es"
    sections: list[str] = []

    for slug in CHAPTER_ORDER:
        path = content_dir / slug / "index.md"
        if not path.exists():
            continue
        raw = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(raw)
        refs = extract_references(body)
        if not refs:
            continue
        title = fm.get("title", slug)
        href = chapter_link(slug, locale)
        sections.append(f"### [{title}]({href})\n\n{refs}\n")

    order = 12
    lines = [
        "---",
        f'title: "{TITLE[locale]}"',
        f'description: "{DESC[locale]}"',
        f"order: {order}",
        "---",
        "",
        "## Introduction",
        "",
        INTRO[locale],
        "",
        "---",
        "",
        "## By chapter",
        "",
        *sections,
        "---",
        "",
        RELATED[locale],
    ]
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    en_path = ROOT / "src/content/docs/bibliography/index.md"
    es_path = ROOT / "src/content/docs-es/bibliography/index.md"
    en_path.parent.mkdir(parents=True, exist_ok=True)
    es_path.parent.mkdir(parents=True, exist_ok=True)
    en_path.write_text(build_locale("en"), encoding="utf-8")
    es_path.write_text(build_locale("es"), encoding="utf-8")
    print(f"Wrote {en_path.relative_to(ROOT)}")
    print(f"Wrote {es_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
