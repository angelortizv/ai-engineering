import RocketIcon from '@lucide/svelte/icons/rocket';
import BrainIcon from '@lucide/svelte/icons/brain';
import FlaskConicalIcon from '@lucide/svelte/icons/flask-conical';
import ClipboardCheckIcon from '@lucide/svelte/icons/clipboard-check';
import MessageSquareQuoteIcon from '@lucide/svelte/icons/message-square-quote';
import BotIcon from '@lucide/svelte/icons/bot';
import SlidersHorizontalIcon from '@lucide/svelte/icons/sliders-horizontal';
import DatabaseIcon from '@lucide/svelte/icons/database';
import GaugeIcon from '@lucide/svelte/icons/gauge';
import Building2Icon from '@lucide/svelte/icons/building-2';
import type { DocsConfig } from './types.js';

export const docsConfig: DocsConfig = {
	site: {
		title: 'AI Engineering',
		description: 'Resumen y aprendizajes del libro AI Engineering: Building Applications with Foundation Models by Chip Huyen.',
		social: {
			github: 'https://github.com/angelortizv/ai-engineering'
		}
	},
	sidebar: [
		{
			label: 'Introduction to Building AI Applications with Foundation Models',
			icon: RocketIcon,
			href: '/docs/introduction-to-building-ai-applications-with-foundation-models'
		},
		{ label: 'Understanding Foundation Models', icon: BrainIcon, href: '/docs/understanding-foundation-models' },
		{ label: 'Evaluation Methodology', icon: FlaskConicalIcon, href: '/docs/evaluation-methodology' },
		{ label: 'Evaluating Modern AI Systems', icon: ClipboardCheckIcon, href: '/docs/evaluating-modern-ai-systems' },
		{ label: 'Prompt Engineering', icon: MessageSquareQuoteIcon, href: '/docs/prompt-engineering' },
		{ label: 'RAG and Agents', icon: BotIcon, href: '/docs/rag-and-agents' },
		{ label: 'Finetuning', icon: SlidersHorizontalIcon, href: '/docs/finetuning' },
		{ label: 'Dataset Engineering', icon: DatabaseIcon, href: '/docs/dataset-engineering' },
		{ label: 'Inference Optimization', icon: GaugeIcon, href: '/docs/inference-optimization' },
		{
			label: 'AI Engineering Architecture and User Feedback',
			icon: Building2Icon,
			href: '/docs/ai-engineering-architecture-and-user-feedback'
		}
	],
	toc: {
		minDepth: 2,
		maxDepth: 3
	},
	i18n: {
		defaultLocale: 'en',
		locales: [
			{ code: 'en', label: 'English', flag: '🇺🇸' },
			{ code: 'es', label: 'Español', flag: '🇨🇷' }
		]
	}
	// Uncomment to enable version selector:
	// versions: {
	// 	current: 'v1.0.0',
	// 	versions: [
	// 		{ label: 'v1.0.0 (latest)', href: '/docs' }
	// 	]
	// }
};
