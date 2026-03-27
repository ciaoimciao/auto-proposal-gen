// 基礎類型定義
export interface Slide {
  id: string;
  type: SlideType;
  title: string;
  content: any;
  order: number;
}

export type SlideType = 
  | 'cover' 
  | 'brand' 
  | 'problem' 
  | 'solution' 
  | 'timeline' 
  | 'team' 
  | 'budget' 
  | 'summary';

// 封面頁數據
export interface CoverData {
  title: string;
  subtitle: string;
  date: string;
  client: string;
  presenter: string;
}

// 品牌頁數據
export interface BrandData {
  personality: BrandPersonality;
  colors: BrandColors;
  logo: string;
  tagline: string;
}

export type BrandPersonality = 'minimal' | 'bold' | 'warm';
export interface BrandColors {
  primary: string;
  secondary: string;
  accent: string;
}

// 問題頁數據
export interface ProblemData {
  title: string;
  description: string;
  painPoints: string[];
  impact: string;
}

// 解決方案頁數據
export interface SolutionData {
  approach: string;
  features: string[];
  benefits: string[];
  timeline: string;
}

// 時間軸頁數據
export interface TimelineData {
  phases: Phase[];
}

export interface Phase {
  name: string;
  duration: string;
  milestones: string[];
  deliverables: string[];
}

// 團隊頁數據
export interface TeamData {
  members: TeamMember[];
  structure: string;
  expertise: string[];
}

export interface TeamMember {
  name: string;
  role: string;
  expertise: string[];
  photo?: string;
}

// 預算頁數據
export interface BudgetData {
  total: number;
  breakdown: BudgetItem[];
  currency: string;
}

export interface BudgetItem {
  category: string;
  amount: number;
  description: string;
}

// 總結頁數據
export interface SummaryData {
  keyPoints: string[];
  nextSteps: string[];
  contact: ContactInfo;
}

export interface ContactInfo {
  name: string;
  email: string;
  phone: string;
  website: string;
}

// 路線圖數據
export interface RoadmapData {
  weeks: WeekData[];
}

export interface WeekData {
  week: number;
  startDate: string;
  endDate: string;
  milestones: string[];
  deliverables: string[];
  status: 'pending' | 'in_progress' | 'completed';
}

// 應用狀態
export interface AppState {
  currentSlide: string;
  slides: Slide[];
  data: {
    cover: CoverData;
    brand: BrandData;
    problem: ProblemData;
    solution: SolutionData;
    timeline: TimelineData;
    team: TeamData;
    budget: BudgetData;
    summary: SummaryData;
    roadmap: RoadmapData;
  };
  settings: {
    theme: BrandPersonality;
    language: 'zh' | 'en';
    exportFormat: 'pdf' | 'pptx' | 'html';
  };
}

// 事件類型
export type AppEvent = 
  | { type: 'SLIDE_CHANGE'; payload: { slideId: string } }
  | { type: 'DATA_UPDATE'; payload: { section: string; data: any } }
  | { type: 'THEME_CHANGE'; payload: { theme: BrandPersonality } }
  | { type: 'EXPORT_REQUEST'; payload: { format: string } }
  | { type: 'SAVE_REQUEST' }
  | { type: 'LOAD_REQUEST'; payload: { data: any } };