import { error } from '@sveltejs/kit';
import { getDoc } from '$lib/docs/index.js';
import { getStudy, getStudyChapters } from '$lib/study/load-study.js';
import type { PageLoad } from './$types.js';

export const prerender = true;

export function entries() {
	return getStudyChapters().map((chapter) => ({ chapter }));
}

export const load: PageLoad = ({ params }) => {
	const deck = getStudy(params.chapter, 'en');
	if (!deck) throw error(404, `Study not found: ${params.chapter}`);

	const chapterDoc = getDoc(params.chapter, 'en');

	return {
		locale: 'en',
		chapter: params.chapter,
		deck,
		chapterTitle: chapterDoc?.meta.title ?? params.chapter
	};
};
