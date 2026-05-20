import { base } from '$app/paths';
import type { ChapterStudy } from './types.js';
import { isStudyChapter, getStudyChapters } from './chapters.js';

const studyModules = import.meta.glob<ChapterStudy>('/src/content/study/*/*.json', {
	eager: true,
	import: 'default'
});

function modulePath(locale: string, chapter: string): string {
	return `/src/content/study/${locale}/${chapter}.json`;
}

export function getStudy(chapter: string, locale: string): ChapterStudy | undefined {
	if (!isStudyChapter(chapter)) return undefined;
	return studyModules[modulePath(locale, chapter)];
}

export function hasStudy(chapter: string, locale: string): boolean {
	return getStudy(chapter, locale) !== undefined;
}

export { getStudyChapters };

export function studyHref(chapter: string, locale: string): string {
	const prefix = locale === 'en' ? `${base}/docs` : `${base}/docs/${locale}`;
	return `${prefix}/${chapter}/study`;
}

export function chapterReadHref(chapter: string, locale: string): string {
	const prefix = locale === 'en' ? `${base}/docs` : `${base}/docs/${locale}`;
	return `${prefix}/${chapter}`;
}
