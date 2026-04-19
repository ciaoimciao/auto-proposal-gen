/**
 * 主題工具函數
 */

import { BrandPersonality, BrandColors } from '../types';

/**
 * 主題顏色配置
 */
export const THEME_COLORS: Record<BrandPersonality, BrandColors> = {
  minimal: {
    primary: '#2563eb',
    secondary: '#64748b',
    accent: '#f59e0b'
  },
  bold: {
    primary: '#ef4444',
    secondary: '#1f2937',
    accent: '#22c55e'
  },
  warm: {
    primary: '#f59e0b',
    secondary: '#6366f1',
    accent: '#ec4899'
  }
};

/**
 * 獲取主題顏色
 */
export function getThemeColors(personality: BrandPersonality): BrandColors {
  return THEME_COLORS[personality] || THEME_COLORS.minimal;
}

/**
 * 應用主題到文檔
 */
export function applyTheme(personality: BrandPersonality): void {
  const colors = getThemeColors(personality);
  const root = document.documentElement;

  root.style.setProperty('--color-primary', colors.primary);
  root.style.setProperty('--color-secondary', colors.secondary);
  root.style.setProperty('--color-accent', colors.accent);

  // 更新 CSS 變量
  updateCSSVariables(colors);
}

/**
 * 更新 CSS 變量
 */
function updateCSSVariables(colors: BrandColors): void {
  const style = document.createElement('style');
  style.textContent = `
    :root {
      --color-primary: ${colors.primary};
      --color-secondary: ${colors.secondary};
      --color-accent: ${colors.accent};
    }
  `;
  document.head.appendChild(style);
}

/**
 * 獲取主題類名
 */
export function getThemeClass(personality: BrandPersonality): string {
  switch (personality) {
    case 'minimal':
      return 'theme-minimal';
    case 'bold':
      return 'theme-bold';
    case 'warm':
      return 'theme-warm';
    default:
      return 'theme-minimal';
  }
}