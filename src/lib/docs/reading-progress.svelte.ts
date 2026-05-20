import { browser } from '$app/environment';
import {
	loadProgress,
	saveProgress,
	isTrackedChapter,
	getStats,
	type ReadingProgressData
} from './reading-progress.js';

let locale = $state('en');
let data = $state<ReadingProgressData>({ visited: {}, completed: {} });

export function initReadingProgress(loc: string): void {
	locale = loc;
	if (browser) data = loadProgress(loc);
}

export function getReadingProgress() {
	return {
		get locale() {
			return locale;
		},
		get data() {
			return data;
		},
		get stats() {
			return getStats(data);
		}
	};
}

function persist(): void {
	if (browser) saveProgress(locale, data);
}

export function markChapterVisited(slug: string): void {
	if (!isTrackedChapter(slug)) return;
	if (data.visited[slug]) return;
	data = {
		...data,
		visited: { ...data.visited, [slug]: true }
	};
	persist();
}

export function toggleChapterCompleted(slug: string): void {
	if (!isTrackedChapter(slug)) return;
	const next = !data.completed[slug];
	data = {
		...data,
		visited: { ...data.visited, [slug]: true },
		completed: { ...data.completed, [slug]: next }
	};
	persist();
}

export function clearReadingProgress(): void {
	data = { visited: {}, completed: {} };
	persist();
}
