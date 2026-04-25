<script lang="ts">
	import { base } from '$app/paths';
	import { page } from '$app/state';
	import { goto, afterNavigate } from '$app/navigation';
	import { onMount } from 'svelte';
	import { docsConfig } from '$lib/docs/config.js';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu/index.js';
	import LanguagesIcon from '@lucide/svelte/icons/languages';
	import CheckIcon from '@lucide/svelte/icons/check';

	const LOCALE_STORAGE_KEY = 'docs-locale';
	let i18n = docsConfig.i18n;

	function stripBase(pathname: string): string {
		if (!base) return pathname;
		if (!pathname.startsWith(base)) return pathname;
		return pathname.slice(base.length) || '/';
	}

	function buildPathForLocale(pathname: string, targetLocale: string): string {
		if (!i18n) return pathname;

		const localPath = stripBase(pathname);
		const defaultLocale = i18n.defaultLocale;
		const pathParts = localPath.split('/').filter(Boolean);
		const first = pathParts[0];
		const second = pathParts[1];

		if (first !== 'docs') return pathname;

		const hasLocalePrefix = !!second && i18n.locales.some((l) => l.code === second);
		const rest = hasLocalePrefix ? pathParts.slice(2) : pathParts.slice(1);
		const restPath = rest.length ? `/${rest.join('/')}` : '';

		if (targetLocale === defaultLocale) {
			return `${base}/docs${restPath}`;
		}

		return `${base}/docs/${targetLocale}${restPath}`;
	}

	function getCurrentLocale(): string {
		if (!i18n) return 'en';
		const pathParts = stripBase(page.url.pathname).split('/').filter(Boolean);
		// Check if first segment after /docs is a locale code
		if (pathParts[0] === 'docs' && pathParts[1]) {
			const match = i18n.locales.find((l) => l.code === pathParts[1]);
			if (match) return match.code;
		}
		return i18n.defaultLocale;
	}

	function switchLocale(code: string) {
		if (!i18n) return;
		localStorage.setItem(LOCALE_STORAGE_KEY, code);
		const newPath = buildPathForLocale(page.url.pathname, code);
		goto(newPath);
	}

	function syncLocaleWithStorage(replaceState = true) {
		if (!i18n) return;
		const pathname = page.url.pathname;
		if (!stripBase(pathname).startsWith('/docs')) return;

		const currentLocale = getCurrentLocale();
		const savedLocale = localStorage.getItem(LOCALE_STORAGE_KEY);

		// Seed storage with current locale when user has no preference yet.
		if (!savedLocale) {
			localStorage.setItem(LOCALE_STORAGE_KEY, currentLocale);
			return;
		}

		const isValidLocale = i18n.locales.some((locale) => locale.code === savedLocale);
		if (!isValidLocale || savedLocale === currentLocale) return;

		const targetPath = buildPathForLocale(pathname, savedLocale);
		if (targetPath === pathname) return;
		goto(targetPath, { replaceState });
	}

	onMount(() => {
		syncLocaleWithStorage(true);
		const unsubscribe = afterNavigate(() => {
			syncLocaleWithStorage(true);
		});
		return unsubscribe;
	});
</script>

{#if i18n && i18n.locales.length > 1}
	<DropdownMenu.Root>
		<DropdownMenu.Trigger>
			{#snippet child({ props })}
				<Button variant="ghost" size="icon" {...props} aria-label="Switch language">
					<LanguagesIcon class="size-4" />
				</Button>
			{/snippet}
		</DropdownMenu.Trigger>
		<DropdownMenu.Content align="end">
			{#each i18n.locales as locale (locale.code)}
				<DropdownMenu.Item onSelect={() => switchLocale(locale.code)}>
					{#if locale.flag}
						<span>{locale.flag}</span>
					{/if}
					{locale.label}
					{#if getCurrentLocale() === locale.code}
						<CheckIcon class="ms-auto size-4" />
					{/if}
				</DropdownMenu.Item>
			{/each}
		</DropdownMenu.Content>
	</DropdownMenu.Root>
{/if}
