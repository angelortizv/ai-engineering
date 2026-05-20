import { error } from '@sveltejs/kit';
import { docsConfig, getDoc } from '$lib/docs/index.js';
import { getStudy, getStudyChapters } from '$lib/study/load-study.js';
import type { PageLoad } from './$types.js';

export const prerender = true;

export function entries() {
	const locales = docsConfig.i18n?.locales ?? [];
	const defaultLocale = docsConfig.i18n?.defaultLocale ?? 'en';
	const results: { lang: string; chapter: string }[] = [];

	for (const locale of locales) {
		if (locale.code === defaultLocale) continue;
		for (const chapter of getStudyChapters()) {
			if (getStudy(chapter, locale.code)) {
				results.push({ lang: locale.code, chapter });
			}
		}
	}

	return results;
}

export const load: PageLoad = ({ params }) => {
	const deck = getStudy(params.chapter, params.lang);
	if (!deck) throw error(404, `Study not found: ${params.chapter}`);

	const chapterDoc = getDoc(params.chapter, params.lang);

	return {
		locale: params.lang,
		chapter: params.chapter,
		deck,
		chapterTitle: chapterDoc?.meta.title ?? params.chapter
	};
};
