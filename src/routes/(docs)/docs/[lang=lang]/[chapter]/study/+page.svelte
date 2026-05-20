<script lang="ts">
	import ChapterStudy from '$lib/components/study/chapter-study.svelte';
	import SeoHead from '$lib/components/seo-head.svelte';

	let { data } = $props();

	const title = $derived(
		data.locale === 'es'
			? `Estudio: ${data.chapterTitle}`
			: `Study: ${data.chapterTitle}`
	);
	const description = $derived(
		data.locale === 'es'
			? `Flashcards y quiz del capítulo ${data.chapterTitle}.`
			: `Flashcards and quiz for ${data.chapterTitle}.`
	);
</script>

<SeoHead {title} description={description} />

<ChapterStudy deck={data.deck} locale={data.locale} chapterTitle={data.chapterTitle} />
