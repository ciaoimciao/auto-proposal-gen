// ═══════════════════════════════════════
// AI Slide Gen — Type Definitions
// ═══════════════════════════════════════

export type SlideType =
  | 'cover'
  | 'agenda'
  | 'problem'
  | 'solution'
  | 'feature'
  | 'timeline'
  | 'team'
  | 'budget'
  | 'metric'
  | 'closing';

export type Theme = 'dark' | 'light' | 'navy';
export type Language = 'zh' | 'en';
export type SlideCount = '8' | '12' | '16';

export interface SlideTable {
  headers: string[];
  rows: string[][];
}

export interface Slide {
  type: SlideType;
  title: string;
  subtitle?: string;
  body?: string;
  points?: string[];
  highlight?: string;
  highlightLabel?: string;
  table?: SlideTable;
}

export interface Presentation {
  title: string;
  slides: Slide[];
}

export interface FormData {
  apiKey: string;
  clientName: string;
  projectName: string;
  description: string;
  industry: string;
  language: Language;
  slideCount: SlideCount;
  presenter: string;
  theme: Theme;
}

export interface ThemeColors {
  bg: string;
  bg2: string;
  tx: string;
  tx2: string;
  ac: string;
  ac2: string;
  isDark: boolean;
}

export interface AppState {
  apiKey: string;
  theme: Theme;
  slides: Slide[];
  title: string;
  current: number;
}
