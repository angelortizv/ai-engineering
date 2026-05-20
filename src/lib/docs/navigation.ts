import { docsConfig } from './config.js';
import { getDocsByDirectory, getAllDocs, getDoc } from './content.js';
import type { NavItem } from './types.js';
import { base } from '$app/paths';

function localizedSidebarLabel(
	label: string,
	href: string | undefined,
	locale?: string
): string {
	const defaultLocale = docsConfig.i18n?.defaultLocale ?? 'en';
	if (!href || !locale || locale === defaultLocale) return label;
	const slug = href.replace(/^\/docs\//, '').replace(/\/$/, '');
	const doc = getDoc(slug, locale);
	return doc?.meta.title ?? label;
}

function localizeHref(href: string, locale?: string): string {
	const normalized = href.startsWith(base) ? href : `${base}${href}`;
	if (!locale) return normalized;
	const defaultLocale = docsConfig.i18n?.defaultLocale ?? 'en';
	if (locale === defaultLocale) return normalized;
	if (!normalized.startsWith(`${base}/docs`)) return normalized;
	return normalized.replace(`${base}/docs`, `${base}/docs/${locale}`);
}

export function generateNavigation(locale?: string): NavItem[] {
	const nav: NavItem[] = [];

	for (const section of docsConfig.sidebar) {
		if (section.autogenerate) {
			const docs = getDocsByDirectory(section.autogenerate.directory, locale);
			const items: NavItem[] = docs.map((doc) => ({
				title: doc.meta.sidebar?.label ?? doc.meta.title,
				href: doc.href,
				order: doc.meta.order
			}));

			items.sort((a, b) => (a.order ?? 999) - (b.order ?? 999));

			nav.push({
				title: section.label,
				icon: section.icon,
				items
			});
		} else if (section.items) {
			nav.push({
				title: section.label,
				icon: section.icon,
				items: section.items.map((item) => ({
					title: item.label,
					href: localizeHref(item.href, locale)
				}))
			});
		} else if (section.href) {
			nav.push({
				title: localizedSidebarLabel(section.label, section.href, locale),
				icon: section.icon,
				href: localizeHref(section.href, locale)
			});
		}
	}

	return nav;
}

export function getNavigation(locale?: string): NavItem[] {
	return generateNavigation(locale);
}

export function getPrevNext(
	currentSlug: string,
	locale?: string
): { prev?: NavItem; next?: NavItem } {
	const allDocs = getAllDocs(locale);
	const index = allDocs.findIndex((doc) => doc.slug === currentSlug);
	if (index === -1) return {};

	return {
		prev:
			index > 0
				? { title: allDocs[index - 1].meta.title, href: allDocs[index - 1].href }
				: undefined,
		next:
			index < allDocs.length - 1
				? { title: allDocs[index + 1].meta.title, href: allDocs[index + 1].href }
				: undefined
	};
}
