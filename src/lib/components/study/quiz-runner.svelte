<script lang="ts">
	import type { StudyQuestion } from '$lib/study/types.js';
	import { chapterReadHref } from '$lib/study/load-study.js';
	import { initStudyProgress, saveQuizScore } from '$lib/study/study-progress.svelte.js';
	import CheckIcon from '@lucide/svelte/icons/check';
	import XIcon from '@lucide/svelte/icons/x';
	import ExternalLinkIcon from '@lucide/svelte/icons/external-link';

	let {
		questions,
		chapter,
		locale = 'en'
	}: {
		questions: StudyQuestion[];
		chapter: string;
		locale?: string;
	} = $props();

	const ui = $derived(
		locale === 'es'
			? {
					submit: 'Comprobar',
					next: 'Siguiente',
					finish: 'Ver resultado',
					correct: 'Correcto',
					incorrect: 'Incorrecto',
					score: 'Puntuación',
					retry: 'Repetir quiz',
					readSection: 'Leer en el capítulo',
					of: 'de',
					empty: 'No hay preguntas en este módulo.'
				}
			: {
					submit: 'Check answer',
					next: 'Next',
					finish: 'See results',
					correct: 'Correct',
					incorrect: 'Incorrect',
					score: 'Score',
					retry: 'Retry quiz',
					readSection: 'Read in chapter',
					of: 'of',
					empty: 'No questions in this quiz.'
				}
	);

	let index = $state(0);
	let selected = $state<number | null>(null);
	let revealed = $state(false);
	let answers = $state<(number | null)[]>([]);
	let finished = $state(false);

	const current = $derived(questions[index]);
	const score = $derived(
		answers.filter((a, i) => a === questions[i]?.correctIndex).length
	);

	$effect(() => {
		initStudyProgress(locale, chapter);
	});

	$effect(() => {
		questions;
		index = 0;
		selected = null;
		revealed = false;
		answers = questions.map(() => null);
		finished = false;
	});

	function sectionLink(q: StudyQuestion): string {
		const base = chapterReadHref(chapter, locale);
		return q.sectionHash ? `${base}${q.sectionHash}` : base;
	}

	function check() {
		if (selected === null) return;
		answers[index] = selected;
		revealed = true;
	}

	function advance() {
		if (index < questions.length - 1) {
			index += 1;
			selected = null;
			revealed = false;
		} else {
			const finalScore = answers.filter(
				(a, i) => a === questions[i]?.correctIndex
			).length;
			finished = true;
			saveQuizScore('main', finalScore, questions.length);
		}
	}

	function retry() {
		index = 0;
		selected = null;
		revealed = false;
		answers = questions.map(() => null);
		finished = false;
	}
</script>

{#if questions.length === 0}
	<p class="text-muted-foreground text-sm">{ui.empty}</p>
{:else if finished}
	<div class="border-border bg-muted/40 mx-auto max-w-xl rounded-lg border p-6 text-center">
		<p class="text-foreground m-0 text-2xl font-semibold">
			{ui.score}: {score}/{questions.length}
		</p>
		<p class="text-muted-foreground mt-2 text-sm">
			{Math.round((score / questions.length) * 100)}%
		</p>
		<button
			type="button"
			class="bg-primary text-primary-foreground hover:bg-primary/90 mt-4 rounded-md px-4 py-2 text-sm font-medium"
			onclick={retry}
		>
			{ui.retry}
		</button>
	</div>
{:else}
	<p class="text-muted-foreground mb-4 text-sm">
		{index + 1} {ui.of} {questions.length}
	</p>

	<fieldset class="border-border mx-auto max-w-xl rounded-lg border p-4">
		<legend class="text-foreground px-1 text-base font-medium">{current.prompt}</legend>
		<div class="mt-3 space-y-2">
			{#each current.choices as choice, i (i)}
				<label
					class="hover:bg-muted/80 flex cursor-pointer items-start gap-2 rounded-md border border-transparent px-3 py-2 text-sm transition-colors
						{selected === i ? 'border-primary bg-muted/50' : ''}
						{revealed && i === current.correctIndex ? 'border-green-600/50 bg-green-500/10' : ''}
						{revealed && selected === i && i !== current.correctIndex ? 'border-red-600/50 bg-red-500/10' : ''}"
				>
					<input
						type="radio"
						name="quiz-choice"
						class="mt-0.5"
						value={i}
						checked={selected === i}
						disabled={revealed}
						onchange={() => (selected = i)}
					/>
					<span>{choice}</span>
					{#if revealed && i === current.correctIndex}
						<CheckIcon class="text-green-600 ms-auto size-4 shrink-0" />
					{:else if revealed && selected === i && i !== current.correctIndex}
						<XIcon class="text-red-600 ms-auto size-4 shrink-0" />
					{/if}
				</label>
			{/each}
		</div>
	</fieldset>

	{#if revealed}
		<div class="border-border bg-muted/40 mx-auto mt-4 max-w-xl rounded-lg border p-4">
			<p class="m-0 text-sm font-medium">
				{selected === current.correctIndex ? ui.correct : ui.incorrect}
			</p>
			<p class="text-muted-foreground mt-2 m-0 text-sm">{current.explanation}</p>
			{#if current.sectionHash}
				<a
					href={sectionLink(current)}
					class="text-primary mt-2 inline-flex items-center gap-1 text-sm hover:underline"
				>
					<ExternalLinkIcon class="size-3.5" />
					{ui.readSection}
				</a>
			{/if}
		</div>
	{/if}

	<div class="mx-auto mt-6 flex max-w-xl justify-center">
		{#if !revealed}
			<button
				type="button"
				class="bg-primary text-primary-foreground hover:bg-primary/90 rounded-md px-4 py-2 text-sm font-medium disabled:opacity-50"
				disabled={selected === null}
				onclick={check}
			>
				{ui.submit}
			</button>
		{:else}
			<button
				type="button"
				class="bg-primary text-primary-foreground hover:bg-primary/90 rounded-md px-4 py-2 text-sm font-medium"
				onclick={advance}
			>
				{index < questions.length - 1 ? ui.next : ui.finish}
			</button>
		{/if}
	</div>
{/if}
