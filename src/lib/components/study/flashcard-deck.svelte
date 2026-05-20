<script lang="ts">
	import type { StudyCard } from '$lib/study/types.js';
	import { chapterReadHref } from '$lib/study/load-study.js';
	import {
		initStudyProgress,
		markCardKnown,
		markCardWrong,
		getStudyProgress,
		clearStudyProgress
	} from '$lib/study/study-progress.svelte.js';
	import ChevronLeftIcon from '@lucide/svelte/icons/chevron-left';
	import ChevronRightIcon from '@lucide/svelte/icons/chevron-right';
	import RotateCcwIcon from '@lucide/svelte/icons/rotate-ccw';
	import ExternalLinkIcon from '@lucide/svelte/icons/external-link';

	let {
		cards,
		chapter,
		locale = 'en'
	}: {
		cards: StudyCard[];
		chapter: string;
		locale?: string;
	} = $props();

	const ui = $derived(
		locale === 'es'
			? {
					flip: 'Voltear',
					again: 'Repasar',
					gotIt: 'Lo sé',
					prev: 'Anterior',
					next: 'Siguiente',
					shuffle: 'Barajar',
					reset: 'Reiniciar progreso',
					of: 'de',
					readSection: 'Leer en el capítulo',
					empty: 'No hay tarjetas en este módulo.'
				}
			: {
					flip: 'Flip',
					again: 'Again',
					gotIt: 'Got it',
					prev: 'Previous',
					next: 'Next',
					shuffle: 'Shuffle',
					reset: 'Reset progress',
					of: 'of',
					readSection: 'Read in chapter',
					empty: 'No cards in this deck.'
				}
	);

	let index = $state(0);
	let flipped = $state(false);
	let order = $state<number[]>([]);

	const progress = $derived(getStudyProgress());
	const current = $derived(
		order.length > 0 ? cards[order[index] ?? 0] : cards[0]
	);
	const knownCount = $derived(
		cards.filter((c) => progress.data.knownCards[c.id]).length
	);

	$effect(() => {
		initStudyProgress(locale, chapter);
	});

	$effect(() => {
		order = cards.map((_, i) => i);
		index = 0;
		flipped = false;
	});

	function go(delta: number) {
		flipped = false;
		index = (index + delta + order.length) % order.length;
	}

	function shuffle() {
		flipped = false;
		order = [...order].sort(() => Math.random() - 0.5);
		index = 0;
	}

	function sectionLink(card: StudyCard): string {
		const base = chapterReadHref(chapter, locale);
		return card.sectionHash ? `${base}${card.sectionHash}` : base;
	}
</script>

{#if cards.length === 0}
	<p class="text-muted-foreground text-sm">{ui.empty}</p>
{:else}
	<p class="text-muted-foreground mb-4 text-sm">
		<span class="text-foreground font-medium">{knownCount}</span>/{cards.length}
		{locale === 'es' ? 'dominadas' : 'mastered'}
	</p>

	<div
		class="border-border bg-card relative mx-auto mb-4 flex min-h-48 w-full max-w-xl cursor-pointer flex-col justify-center rounded-xl border p-6 shadow-sm transition-transform"
		role="button"
		tabindex="0"
		onclick={() => (flipped = !flipped)}
		onkeydown={(e) => {
			if (e.key === 'Enter' || e.key === ' ') {
				e.preventDefault();
				flipped = !flipped;
			}
		}}
		aria-pressed={flipped}
	>
		<p class="text-muted-foreground absolute top-3 end-3 text-xs">
			{index + 1} {ui.of} {order.length}
		</p>
		{#if flipped}
			<p class="text-foreground m-0 text-base leading-relaxed">{current.back}</p>
			{#if current.sectionHash}
				<a
					href={sectionLink(current)}
					class="text-primary mt-4 inline-flex items-center gap-1 text-sm hover:underline"
					onclick={(e) => e.stopPropagation()}
				>
					<ExternalLinkIcon class="size-3.5" />
					{ui.readSection}
				</a>
			{/if}
		{:else}
			<p class="text-foreground m-0 text-lg font-medium">{current.front}</p>
			<p class="text-muted-foreground mt-2 text-xs">{ui.flip}</p>
		{/if}
	</div>

	<div class="mx-auto flex max-w-xl flex-wrap items-center justify-center gap-2">
		<button
			type="button"
			class="border-border hover:bg-muted inline-flex items-center gap-1 rounded-md border px-3 py-1.5 text-sm"
			onclick={() => go(-1)}
		>
			<ChevronLeftIcon class="size-4" />
			{ui.prev}
		</button>
		<button
			type="button"
			class="border-border hover:bg-muted rounded-md border px-3 py-1.5 text-sm"
			onclick={shuffle}
		>
			<RotateCcwIcon class="me-1 inline size-3.5" />
			{ui.shuffle}
		</button>
		<button
			type="button"
			class="border-border hover:bg-muted inline-flex items-center gap-1 rounded-md border px-3 py-1.5 text-sm"
			onclick={() => go(1)}
		>
			{ui.next}
			<ChevronRightIcon class="size-4" />
		</button>
	</div>

	<div class="mx-auto mt-4 flex max-w-xl justify-center gap-3">
		<button
			type="button"
			class="bg-muted hover:bg-muted/80 rounded-md px-4 py-2 text-sm font-medium"
			onclick={() => {
				markCardWrong(current.id);
				go(1);
			}}
		>
			{ui.again}
		</button>
		<button
			type="button"
			class="bg-primary text-primary-foreground hover:bg-primary/90 rounded-md px-4 py-2 text-sm font-medium"
			onclick={() => {
				markCardKnown(current.id, true);
				go(1);
			}}
		>
			{ui.gotIt}
		</button>
	</div>

	<button
		type="button"
		class="text-muted-foreground hover:text-foreground mx-auto mt-6 block text-xs underline-offset-2 hover:underline"
		onclick={() => clearStudyProgress()}
	>
		{ui.reset}
	</button>
{/if}
