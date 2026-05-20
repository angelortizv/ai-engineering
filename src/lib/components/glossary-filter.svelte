<script lang="ts">
	import { applyGlossaryFilter } from '$lib/docs/glossary-filter.js';

	let { locale = 'en', container }: { locale?: string; container?: HTMLElement } = $props();

	let query = $state('');

	const ui = $derived(
		locale === 'es'
			? {
					placeholder: 'Buscar término…',
					hint: 'Filtra por nombre o definición.',
					empty: 'Ningún término coincide.'
				}
			: {
					placeholder: 'Search terms…',
					hint: 'Filter by term name or definition.',
					empty: 'No matching terms.'
				}
	);

	$effect(() => {
		if (container) applyGlossaryFilter(container, query, ui.empty);
	});
</script>

<div class="not-prose mb-6 space-y-2" data-pagefind-ignore>
	<label class="sr-only" for="glossary-filter">{ui.placeholder}</label>
	<input
		id="glossary-filter"
		type="search"
		bind:value={query}
		placeholder={ui.placeholder}
		class="border-input bg-background ring-offset-background placeholder:text-muted-foreground focus-visible:ring-ring w-full rounded-md border px-3 py-2 text-sm focus-visible:outline-none focus-visible:ring-2"
		autocomplete="off"
	/>
	<p class="text-muted-foreground text-xs">{ui.hint}</p>
</div>
