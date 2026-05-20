<script lang="ts">
	import type { ChapterStudy } from '$lib/study/types.js';
	import { chapterReadHref } from '$lib/study/load-study.js';
	import FlashcardDeck from './flashcard-deck.svelte';
	import QuizRunner from './quiz-runner.svelte';
	import ArrowLeftIcon from '@lucide/svelte/icons/arrow-left';
	import BookOpenIcon from '@lucide/svelte/icons/book-open';
	import LayersIcon from '@lucide/svelte/icons/layers';
	import ListChecksIcon from '@lucide/svelte/icons/list-checks';

	let {
		deck,
		locale = 'en',
		chapterTitle = ''
	}: {
		deck: ChapterStudy;
		locale?: string;
		chapterTitle?: string;
	} = $props();

	type Tab = 'cards' | 'quiz';
	let tab = $state<Tab>('cards');

	const ui = $derived(
		locale === 'es'
			? {
					study: 'Estudio',
					back: 'Volver al capítulo',
					cards: 'Flashcards',
					quiz: 'Quiz',
					hint: 'Progreso guardado en este navegador (localStorage).'
				}
			: {
					study: 'Study',
					back: 'Back to chapter',
					cards: 'Flashcards',
					quiz: 'Quiz',
					hint: 'Progress stored in this browser only (localStorage).'
				}
	);

	const readHref = $derived(chapterReadHref(deck.chapterSlug, locale));
</script>

<article id="doc-content" class="mx-auto w-full max-w-3xl" data-pagefind-ignore>
	<header class="mb-8">
		<a
			href={readHref}
			class="text-muted-foreground hover:text-foreground mb-4 inline-flex items-center gap-1.5 text-sm transition-colors"
		>
			<ArrowLeftIcon class="size-4" />
			{ui.back}
		</a>
		<p class="text-muted-foreground m-0 text-sm font-medium uppercase tracking-wide">
			{ui.study}
		</p>
		<h1 class="text-foreground mt-1 text-3xl font-bold tracking-tight">
			{chapterTitle || deck.chapterSlug}
		</h1>
		<p class="text-muted-foreground m-0 mt-2 text-sm">{ui.hint}</p>
	</header>

	<div
		class="border-border mb-6 flex gap-1 rounded-lg border p-1"
		role="tablist"
		aria-label={ui.study}
	>
		<button
			type="button"
			role="tab"
			aria-selected={tab === 'cards'}
			class="flex flex-1 items-center justify-center gap-2 rounded-md px-3 py-2 text-sm font-medium transition-colors
				{tab === 'cards' ? 'bg-primary text-primary-foreground' : 'text-muted-foreground hover:text-foreground'}"
			onclick={() => (tab = 'cards')}
		>
			<LayersIcon class="size-4" />
			{ui.cards}
			<span class="opacity-80">({deck.cards.length})</span>
		</button>
		<button
			type="button"
			role="tab"
			aria-selected={tab === 'quiz'}
			class="flex flex-1 items-center justify-center gap-2 rounded-md px-3 py-2 text-sm font-medium transition-colors
				{tab === 'quiz' ? 'bg-primary text-primary-foreground' : 'text-muted-foreground hover:text-foreground'}"
			onclick={() => (tab = 'quiz')}
		>
			<ListChecksIcon class="size-4" />
			{ui.quiz}
			<span class="opacity-80">({deck.questions.length})</span>
		</button>
	</div>

	{#if tab === 'cards'}
		<FlashcardDeck cards={deck.cards} chapter={deck.chapterSlug} {locale} />
	{:else}
		<QuizRunner questions={deck.questions} chapter={deck.chapterSlug} {locale} />
	{/if}

	<footer class="mt-12 border-t pt-6">
		<a
			href={readHref}
			class="text-muted-foreground hover:text-foreground inline-flex items-center gap-1.5 text-sm"
		>
			<BookOpenIcon class="size-4" />
			{ui.back}
		</a>
	</footer>
</article>
