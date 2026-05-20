import mermaid from 'mermaid';

export function isDarkMode(): boolean {
	if (typeof document === 'undefined') return false;
	return document.documentElement.classList.contains('dark');
}

/** Mermaid theme aligned with site CSS variables (no default yellow subgraphs). */
export function configureMermaid(): void {
	const dark = isDarkMode();

	mermaid.initialize({
		startOnLoad: false,
		securityLevel: 'loose',
		theme: 'base',
		themeVariables: dark
			? {
					darkMode: true,
					background: 'transparent',
					mainBkg: '#2a2a2a',
					secondBkg: '#1f1f1f',
					tertiaryBkg: '#171717',
					primaryColor: '#2a2a2a',
					primaryTextColor: '#fafafa',
					primaryBorderColor: '#525252',
					secondaryColor: '#333333',
					secondaryTextColor: '#fafafa',
					secondaryBorderColor: '#525252',
					tertiaryColor: '#262626',
					tertiaryTextColor: '#a3a3a3',
					tertiaryBorderColor: '#404040',
					clusterBkg: '#1f1f1f',
					clusterBorder: '#525252',
					titleColor: '#fafafa',
					lineColor: '#a3a3a3',
					textColor: '#fafafa',
					edgeLabelBackground: '#262626',
					nodeTextColor: '#fafafa',
					nodeBorder: '#525252'
				}
			: {
					darkMode: false,
					background: 'transparent',
					mainBkg: '#f4f4f5',
					secondBkg: '#fafafa',
					tertiaryBkg: '#ffffff',
					primaryColor: '#f4f4f5',
					primaryTextColor: '#18181b',
					primaryBorderColor: '#d4d4d8',
					secondaryColor: '#e4e4e7',
					secondaryTextColor: '#18181b',
					secondaryBorderColor: '#d4d4d8',
					tertiaryColor: '#fafafa',
					tertiaryTextColor: '#525252',
					tertiaryBorderColor: '#e4e4e7',
					clusterBkg: '#fafafa',
					clusterBorder: '#d4d4d8',
					titleColor: '#18181b',
					lineColor: '#71717a',
					textColor: '#18181b',
					edgeLabelBackground: '#f4f4f5',
					nodeTextColor: '#18181b',
					nodeBorder: '#d4d4d8'
				}
	});
}

function wrapMermaidOutput(el: HTMLElement): void {
	if (el.closest('.mermaid-chart')) return;
	const wrapper = document.createElement('div');
	wrapper.className = 'mermaid-chart';
	const source = el.dataset.mermaidSource;
	if (source) wrapper.dataset.mermaidSource = source;
	el.parentNode?.insertBefore(wrapper, el);
	wrapper.appendChild(el);
}

export async function renderMermaidIn(container: HTMLElement): Promise<void> {
	const blocks = container.querySelectorAll<HTMLElement>('pre.mermaid:not([data-processed])');
	if (!blocks.length) return;

	for (const block of blocks) {
		const source = block.textContent?.trim() ?? '';
		if (source) block.dataset.mermaidSource = source;
	}

	configureMermaid();
	await mermaid.run({ nodes: Array.from(blocks) });

	for (const block of blocks) {
		block.dataset.processed = 'true';
		wrapMermaidOutput(block);
	}

	// Mermaid may replace pre with a sibling div — wrap those too
	container.querySelectorAll<HTMLElement>('div.mermaid, [id^="dmermaid-"]').forEach((el) => {
		if (!el.closest('.mermaid-chart')) wrapMermaidOutput(el);
	});
}

/** Re-render diagrams after light/dark toggle (uses stored source). */
export async function rerenderMermaidIn(container: HTMLElement): Promise<void> {
	const charts = container.querySelectorAll<HTMLElement>('.mermaid-chart');
	if (!charts.length) return;

	for (const chart of charts) {
		const source = chart.dataset.mermaidSource;
		if (!source) continue;
		const pre = document.createElement('pre');
		pre.className = 'mermaid';
		pre.textContent = source;
		pre.dataset.mermaidSource = source;
		chart.replaceWith(pre);
	}

	await renderMermaidIn(container);
}
