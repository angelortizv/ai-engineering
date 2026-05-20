<script lang="ts">
	import { base } from '$app/paths';
	import { getDoc } from '$lib/docs/index.js';
	import {
		TRACKED_CHAPTER_SLUGS,
		chapterHref,
		getStats
	} from '$lib/docs/reading-progress.js';
	import {
		getReadingProgress,
		toggleChapterCompleted,
		clearReadingProgress
	} from '$lib/docs/reading-progress.svelte.js';
	import CheckIcon from '@lucide/svelte/icons/check';
	import CircleIcon from '@lucide/svelte/icons/circle';
	import CircleCheckIcon from '@lucide/svelte/icons/circle-check';

	let { locale = 'en' }: { locale?: string } = $props();

	const ui = $derived(
		locale === 'es'
			? {
					title: 'Progreso de lectura',
					hint: 'Guardado en este navegador (localStorage).',
					visited: 'visitados',
					completed: 'completados',
					markComplete: 'Marcar capítulo como completado',
					markIncomplete: 'Quitar marca de completado',
					reset: 'Reiniciar progreso',
					next: '¿Terminaste el libro?',
					nextLink: 'Qué sigue después →',
					chPrefix: 'Cap.'
				}
			: {
					title: 'Reading progress',
					hint: 'Stored in this browser only (localStorage).',
					visited: 'visited',
					completed: 'completed',
					markComplete: 'Mark chapter complete',
					markIncomplete: 'Unmark chapter complete',
					reset: 'Reset progress',
					next: 'Finished the book?',
					nextLink: 'What comes next →',
					chPrefix: 'Ch.'
				}
	);

	const progress = $derived(getReadingProgress());
	const stats = $derived(getStats(progress.data));
	const percent = $derived(
		stats.total > 0 ? Math.round((stats.completed / stats.total) * 100) : 0
	);

	const epilogueHref = $derived(
		locale === 'es' ? `${base}/docs/es/epilogue` : `${base}/docs/epilogue`
	);
</script>

<section
	class="not-prose border-border bg-muted/40 mb-8 rounded-lg border p-4"
	data-pagefind-ignore
	aria-labelledby="reading-progress-heading"
>
	<div class="mb-3 flex flex-wrap items-end justify-between gap-2">
		<div>
			<h2 id="reading-progress-heading" class="text-foreground m-0 text-lg font-semibold">
				{ui.title}
			</h2>
			<p class="text-muted-foreground m-0 mt-1 text-xs">{ui.hint}</p>
		</div>
		<p class="text-muted-foreground m-0 text-sm">
			<span class="text-foreground font-medium">{stats.completed}</span>/{stats.total}
			{ui.completed}
			<span class="mx-1">·</span>
			<span class="text-foreground font-medium">{stats.visited}</span>
			{ui.visited}
		</p>
	</div>

	<div
		class="bg-muted mb-4 h-2 w-full overflow-hidden rounded-full"
		role="progressbar"
		aria-valuenow={percent}
		aria-valuemin={0}
		aria-valuemax={100}
		aria-label={ui.title}
	>
		<div
			class="bg-primary h-full rounded-full transition-[width] duration-300"
			style:width="{percent}%"
		></div>
	</div>

	<ul class="m-0 list-none space-y-1 p-0">
		{#each TRACKED_CHAPTER_SLUGS as slug, i (slug)}
			{@const doc = getDoc(slug, locale)}
			{@const done = progress.data.completed[slug]}
			{@const seen = progress.data.visited[slug]}
			<li>
				<div
					class="hover:bg-muted/80 flex items-center gap-2 rounded-md px-2 py-1.5 text-sm transition-colors"
				>
					<button
						type="button"
						class="text-muted-foreground hover:text-foreground shrink-0"
						aria-label={done ? ui.markIncomplete : ui.markComplete}
						aria-pressed={done}
						onclick={() => toggleChapterCompleted(slug)}
					>
						{#if done}
							<CircleCheckIcon class="text-primary size-4" />
						{:else if seen}
							<CircleIcon class="size-4" />
						{:else}
							<CircleIcon class="size-4 opacity-40" />
						{/if}
					</button>
					<a
						href={chapterHref(slug, locale)}
						class="text-foreground min-w-0 flex-1 truncate hover:underline"
					>
						<span class="text-muted-foreground">{ui.chPrefix} {i + 1}.</span>
						{doc?.meta.title ?? slug}
					</a>
					{#if done}
						<CheckIcon class="text-primary size-3.5 shrink-0" aria-hidden="true" />
					{/if}
				</div>
			</li>
		{/each}
	</ul>

	<div class="mt-4 flex flex-wrap items-center justify-between gap-2 border-t pt-3">
		<button
			type="button"
			class="text-muted-foreground hover:text-foreground text-xs underline-offset-2 hover:underline"
			onclick={() => clearReadingProgress()}
		>
			{ui.reset}
		</button>
		<p class="text-muted-foreground m-0 text-sm">
			{ui.next}
			<a href={epilogueHref} class="text-foreground font-medium hover:underline">{ui.nextLink}</a>
		</p>
	</div>
</section>
