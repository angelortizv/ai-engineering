import { TRACKED_CHAPTER_SLUGS } from '$lib/docs/reading-progress.js';

/** Chapters 1–10 with a `/study` route when JSON exists in `src/content/study/{locale}/`. */
export const STUDY_CHAPTERS = TRACKED_CHAPTER_SLUGS;

export type StudyChapterSlug = (typeof STUDY_CHAPTERS)[number];

export function isStudyChapter(slug: string): slug is StudyChapterSlug {
	return (STUDY_CHAPTERS as readonly string[]).includes(slug);
}

export function getStudyChapters(): StudyChapterSlug[] {
	return [...STUDY_CHAPTERS];
}
