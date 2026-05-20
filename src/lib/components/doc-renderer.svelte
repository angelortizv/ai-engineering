<script lang="ts">
	import type { Component } from 'svelte';
	import type { DocMeta } from '$lib/docs/types.js';
	import { toc } from '$lib/docs/toc.svelte';
	import { docsConfig } from '$lib/docs/config.js';
	import MobileToc from '$lib/components/mobile-toc.svelte';
	import BackToTop from '$lib/components/nav/back-to-top.svelte';
	import CopyUrl from '$lib/components/nav/copy-url.svelte';
	import PencilIcon from '@lucide/svelte/icons/pencil';
	import CalendarIcon from '@lucide/svelte/icons/calendar';
	import ClockIcon from '@lucide/svelte/icons/clock';
	import { calculateReadingTime } from '$lib/docs/reading-time.js';
	import { renderMermaidIn, rerenderMermaidIn } from '$lib/docs/mermaid.js';
	import { mode } from 'mode-watcher';

	let {
		meta,
		component: Content,
		slug = '',
		rawContent = '',
		locale = 'en'
	}: {
		meta: DocMeta;
		component: Component;
		slug?: string;
		rawContent?: string;
		locale?: string;
	} = $props();

	let readingTime = $derived(rawContent ? calculateReadingTime(rawContent) : '');

	let ui = $derived(
		locale === 'es'
			? {
					editOnGitHub: 'Editar esta página en GitHub',
					lastUpdated: 'Última actualización:',
					dateLocale: 'es'
				}
			: {
					editOnGitHub: 'Edit this page on GitHub',
					lastUpdated: 'Last updated:',
					dateLocale: 'en-US'
				}
	);

	let contentEl: HTMLDivElement | undefined = $state();
	let lastMermaidTheme = $state<string | undefined>(undefined);

	let editUrl = $derived.by(() => {
		const github = docsConfig.site.social?.github;
		if (!github) return '';
		const defaultLocale = docsConfig.i18n?.defaultLocale ?? 'en';
		const contentDir =
			locale && locale !== defaultLocale ? `docs-${locale}` : 'docs';
		const filePath = slug
			? `src/content/${contentDir}/${slug}/index.md`
			: `src/content/${contentDir}/index.md`;
		return `${github}/edit/main/${filePath}`;
	});

	function enhanceContent(container: HTMLElement) {
		const headings = container.querySelectorAll<HTMLElement>('h2, h3, h4, h5, h6');
		for (const heading of headings) {
			if (!heading.id) {
				heading.id =
					heading.textContent
						?.trim()
						.toLowerCase()
						.replace(/[^a-z0-9]+/g, '-')
						.replace(/(^-|-$)/g, '') ?? '';
			}
			if (!heading.querySelector('.anchor-link')) {
				heading.classList.add('group', 'relative');
				const anchor = document.createElement('a');
				anchor.href = `#${heading.id}`;
				anchor.className =
					'anchor-link text-muted-foreground/0 group-hover:text-muted-foreground absolute -left-5 top-0 no-underline transition-colors';
				anchor.textContent = '#';
				anchor.setAttribute('aria-hidden', 'true');
				heading.prepend(anchor);
			}
		}

		// Mermaid before copy buttons — injected HTML breaks the parser.
		void renderMermaidIn(container);

		const codeBlocks = container.querySelectorAll<HTMLElement>('pre:not(.mermaid)');
		for (const pre of codeBlocks) {
			if (pre.querySelector('.copy-btn')) continue;
			pre.classList.add('relative', 'group/code');

			const btn = document.createElement('button');
			btn.className =
				'copy-btn absolute right-2 top-2 rounded-md border bg-background/80 px-2 py-1 text-xs text-muted-foreground opacity-0 transition-opacity hover:text-foreground group-hover/code:opacity-100';
			btn.textContent = 'Copy';
			btn.addEventListener('click', () => {
				const code = pre.querySelector('code');
				if (code) {
					navigator.clipboard.writeText(code.textContent ?? '');
					btn.textContent = 'Copied!';
					setTimeout(() => (btn.textContent = 'Copy'), 2000);
				}
			});
			pre.appendChild(btn);
		}

		// Add click-to-zoom on images
		const images = container.querySelectorAll<HTMLImageElement>('img');
		for (const img of images) {
			if (img.dataset.zoomEnabled) continue;
			img.dataset.zoomEnabled = 'true';
			img.classList.add('cursor-zoom-in', 'transition-transform');
			img.addEventListener('click', () => {
				const overlay = document.createElement('div');
				overlay.className = 'fixed inset-0 z-[100] flex items-center justify-center bg-black/80 cursor-zoom-out p-8';
				const clone = img.cloneNode() as HTMLImageElement;
				clone.className = 'max-h-full max-w-full rounded-lg object-contain';
				overlay.appendChild(clone);
				overlay.addEventListener('click', () => overlay.remove());
				document.addEventListener('keydown', function handler(e) {
					if (e.key === 'Escape') { overlay.remove(); document.removeEventListener('keydown', handler); }
				});
				document.body.appendChild(overlay);
			});
		}

		toc.extractHeadings(container);
	}

	$effect(() => {
		void Content;

		const timer = setTimeout(() => {
			if (contentEl) enhanceContent(contentEl);
		}, 0);

		return () => {
			clearTimeout(timer);
			toc.clear();
		};
	});

	// Re-render Mermaid when toggling light/dark (skip first run — initial render handles it).
	$effect(() => {
		const theme = mode.current;
		if (!contentEl) return;

		if (lastMermaidTheme === undefined) {
			lastMermaidTheme = theme;
			return;
		}
		if (lastMermaidTheme === theme) return;
		lastMermaidTheme = theme;

		const timer = setTimeout(() => {
			if (contentEl?.querySelector('.mermaid-chart')) {
				void rerenderMermaidIn(contentEl);
			}
		}, 50);

		return () => clearTimeout(timer);
	});
</script>

<article id="doc-content" class="doc-content mx-auto w-full max-w-4xl" data-pagefind-body>
	<header class="mb-8">
		<h1 class="text-3xl font-bold tracking-tight">{meta.title}</h1>
		{#if meta.description}
			<p class="text-muted-foreground mt-2 text-lg">{meta.description}</p>
		{/if}
		{#if readingTime}
			<div class="text-muted-foreground mt-3 flex items-center gap-1.5 text-sm">
				<ClockIcon class="size-3.5" />
				<span>{readingTime}</span>
			</div>
		{/if}
	</header>

	<MobileToc />

	<div class="prose dark:prose-invert max-w-none" bind:this={contentEl}>
		<Content></Content>
	</div>

	<footer class="mt-12 border-t pt-6">
		{#if meta.lastUpdated}
			<div class="mb-4">
				<span class="text-muted-foreground inline-flex items-center gap-1.5 text-sm">
					<CalendarIcon class="size-3.5" />
					{ui.lastUpdated} {new Date(meta.lastUpdated).toLocaleDateString(ui.dateLocale, { year: 'numeric', month: 'long', day: 'numeric' })}
				</span>
			</div>
		{/if}
		<div class="flex items-center justify-between">
			<div class="flex items-center gap-x-4">
				{#if editUrl}
					<a
						href={editUrl}
						target="_blank"
						rel="noopener noreferrer"
						class="text-muted-foreground hover:text-foreground inline-flex items-center gap-1.5 text-sm"
					>
						<PencilIcon class="size-3.5" />
						{ui.editOnGitHub}
					</a>
				{/if}
			</div>
			<div class="flex items-center gap-1">
				<CopyUrl />
				<BackToTop />
			</div>
		</div>
	</footer>
</article>
