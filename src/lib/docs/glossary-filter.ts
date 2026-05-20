/** Client-side filter for glossary term paragraphs (strong-led definitions). */
export function applyGlossaryFilter(
	container: HTMLElement,
	query: string,
	emptyMessage: string
): void {
	const needle = query.trim().toLowerCase();
	const paragraphs = container.querySelectorAll<HTMLElement>('p');
	let visible = 0;

	for (const p of paragraphs) {
		const text = p.textContent?.toLowerCase() ?? '';
		const show = !needle || text.includes(needle);
		p.style.display = show ? '' : 'none';
		if (show && p.querySelector('strong')) visible += 1;
	}

	for (const h2 of container.querySelectorAll<HTMLElement>('h2')) {
		if (
			h2.id === 'introduction' ||
			/^(Related|Relacionado|References|Referencias)/i.test(h2.textContent ?? '')
		) {
			continue;
		}
		let el: Element | null = h2.nextElementSibling;
		let sectionVisible = false;
		while (el && el.tagName !== 'H2') {
			if (el.tagName === 'P' && (el as HTMLElement).style.display !== 'none') {
				sectionVisible = true;
				break;
			}
			el = el.nextElementSibling;
		}
		h2.style.display = sectionVisible || !needle ? '' : 'none';
	}

	let emptyEl = container.querySelector<HTMLElement>('[data-glossary-empty]');
	if (needle && visible === 0) {
		if (!emptyEl) {
			emptyEl = document.createElement('p');
			emptyEl.dataset.glossaryEmpty = 'true';
			emptyEl.className = 'text-muted-foreground text-sm not-prose';
			container.prepend(emptyEl);
		}
		emptyEl.textContent = emptyMessage;
		emptyEl.style.display = '';
	} else if (emptyEl) {
		emptyEl.style.display = 'none';
	}
}
