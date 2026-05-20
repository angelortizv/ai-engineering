import { browser } from '$app/environment';

export type StudyProgressData = {
	knownCards: Record<string, boolean>;
	wrongCards: Record<string, boolean>;
	quizScores: Record<string, { score: number; total: number; at: string }>;
};

const STORAGE_VERSION = 1;

function storageKey(locale: string, chapter: string): string {
	return `aie-study:v${STORAGE_VERSION}:${locale}:${chapter}`;
}

function empty(): StudyProgressData {
	return { knownCards: {}, wrongCards: {}, quizScores: {} };
}

let locale = $state('en');
let chapter = $state('');
let data = $state<StudyProgressData>(empty());

export function initStudyProgress(loc: string, ch: string): void {
	locale = loc;
	chapter = ch;
	if (!browser) {
		data = empty();
		return;
	}
	try {
		const raw = localStorage.getItem(storageKey(loc, ch));
		if (!raw) {
			data = empty();
			return;
		}
		const parsed = JSON.parse(raw) as StudyProgressData;
		data = {
			knownCards: parsed.knownCards ?? {},
			wrongCards: parsed.wrongCards ?? {},
			quizScores: parsed.quizScores ?? {}
		};
	} catch {
		data = empty();
	}
}

export function getStudyProgress() {
	return {
		get data() {
			return data;
		}
	};
}

function persist(): void {
	if (browser && chapter) {
		localStorage.setItem(storageKey(locale, chapter), JSON.stringify(data));
	}
}

export function markCardKnown(cardId: string, known: boolean): void {
	if (known) {
		data = {
			...data,
			knownCards: { ...data.knownCards, [cardId]: true },
			wrongCards: { ...data.wrongCards, [cardId]: false }
		};
	} else {
		const { [cardId]: _, ...knownCards } = data.knownCards;
		data = { ...data, knownCards };
	}
	persist();
}

export function markCardWrong(cardId: string): void {
	data = {
		...data,
		wrongCards: { ...data.wrongCards, [cardId]: true },
		knownCards: { ...data.knownCards, [cardId]: false }
	};
	persist();
}

export function saveQuizScore(quizId: string, score: number, total: number): void {
	data = {
		...data,
		quizScores: {
			...data.quizScores,
			[quizId]: { score, total, at: new Date().toISOString() }
		}
	};
	persist();
}

export function clearStudyProgress(): void {
	data = empty();
	persist();
}
