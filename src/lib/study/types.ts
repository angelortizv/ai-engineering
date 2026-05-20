export type StudyCard = {
	id: string;
	front: string;
	back: string;
	/** Hash on the chapter page, e.g. #in-context-learning-icl */
	sectionHash?: string;
};

export type StudyQuestion = {
	id: string;
	prompt: string;
	choices: string[];
	correctIndex: number;
	explanation: string;
	sectionHash?: string;
};

export type ChapterStudy = {
	chapterSlug: string;
	cards: StudyCard[];
	questions: StudyQuestion[];
};
