import { browser } from '$app/environment';
import { base } from '$app/paths';

/** Chapters 1–10 — progress % is based on these only. */
export const TRACKED_CHAPTER_SLUGS = [
	'introduction-to-building-ai-applications-with-foundation-models',
	'understanding-foundation-models',
	'evaluation-methodology',
	'evaluating-modern-ai-systems',
	'prompt-engineering',
	'rag-and-agents',
	'finetuning',
	'dataset-engineering',
	'inference-optimization',
	'ai-engineering-architecture-and-user-feedback'
] as const;

export type TrackedChapterSlug = (typeof TRACKED_CHAPTER_SLUGS)[number];

export type ReadingProgressData = {
	visited: Record<string, boolean>;
	completed: Record<string, boolean>;
};

const STORAGE_VERSION = 1;

function storageKey(locale: string): string {
	return `aie-reading-progress:v${STORAGE_VERSION}:${locale}`;
}

export function isTrackedChapter(slug: string): slug is TrackedChapterSlug {
	return (TRACKED_CHAPTER_SLUGS as readonly string[]).includes(slug);
}

export function loadProgress(locale: string): ReadingProgressData {
	if (!browser) return { visited: {}, completed: {} };
	try {
		const raw = localStorage.getItem(storageKey(locale));
		if (!raw) return { visited: {}, completed: {} };
		const parsed = JSON.parse(raw) as ReadingProgressData;
		return {
			visited: parsed.visited ?? {},
			completed: parsed.completed ?? {}
		};
	} catch {
		return { visited: {}, completed: {} };
	}
}

export function saveProgress(locale: string, data: ReadingProgressData): void {
	if (!browser) return;
	localStorage.setItem(storageKey(locale), JSON.stringify(data));
}

export function getStats(data: ReadingProgressData) {
	const total = TRACKED_CHAPTER_SLUGS.length;
	const visited = TRACKED_CHAPTER_SLUGS.filter((s) => data.visited[s]).length;
	const completed = TRACKED_CHAPTER_SLUGS.filter((s) => data.completed[s]).length;
	return { total, visited, completed };
}

export function slugFromNavHref(href: string | undefined): string | null {
	if (!href) return null;
	let path = href;
	if (base && path.startsWith(base)) path = path.slice(base.length);
	const esMatch = path.match(/^\/docs\/es\/([^/]+)\/?$/);
	if (esMatch) return esMatch[1];
	const enMatch = path.match(/^\/docs\/([^/]+)\/?$/);
	if (enMatch && enMatch[1] !== 'es') return enMatch[1];
	return null;
}

export function chapterHref(slug: string, locale: string): string {
	const prefix = locale === 'en' ? `${base}/docs` : `${base}/docs/${locale}`;
	return `${prefix}/${slug}`;
}
