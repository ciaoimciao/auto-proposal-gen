/**
 * 日期工具函數
 */

export interface WeekData {
  week: number;
  startDate: string;
  endDate: string;
  milestones: string[];
  deliverables: string[];
  status: 'pending' | 'in_progress' | 'completed';
}

/**
 * 獲取今天日期
 */
export function getToday(): Date {
  return new Date();
}

/**
 * 格式化日期為 YYYY/MM/DD 格式
 */
export function formatDate(date: Date): string {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}/${month}/${day}`;
}

/**
 * 獲取指定日期的下一個週一
 */
export function getNextMonday(date: Date): Date {
  const day = date.getDay();
  const diff = (8 - day) % 7 || 7; // 如果今天是週一，則返回下週一
  const nextMonday = new Date(date);
  nextMonday.setDate(date.getDate() + diff);
  return nextMonday;
}

/**
 * 獲取指定日期的週五
 */
export function getFriday(date: Date): Date {
  const day = date.getDay();
  const diff = (5 - day + 7) % 7; // 計算到週五的天數
  const friday = new Date(date);
  friday.setDate(date.getDate() + diff);
  return friday;
}

/**
 * 生成未來五週的路線圖數據
 */
export function generateRoadmapData(): WeekData[] {
  const weeks: WeekData[] = [];
  const today = getToday();
  let currentMonday = getNextMonday(today);

  for (let i = 1; i <= 5; i++) {
    const startDate = new Date(currentMonday);
    const endDate = getFriday(currentMonday);

    weeks.push({
      week: i,
      startDate: formatDate(startDate),
      endDate: formatDate(endDate),
      milestones: [`第 ${i} 週里程碑`],
      deliverables: [`第 ${i} 週交付物`],
      status: 'pending'
    });

    // 移動到下一個週一
    currentMonday.setDate(currentMonday.getDate() + 7);
  }

  return weeks;
}

/**
 * 根據今天日期計算是否已完成某週
 */
export function calculateWeekStatus(weekData: WeekData): 'pending' | 'in_progress' | 'completed' {
  const today = getToday();
  const startDate = parseDate(weekData.startDate);
  const endDate = parseDate(weekData.endDate);

  if (today > endDate) {
    return 'completed';
  } else if (today >= startDate && today <= endDate) {
    return 'in_progress';
  } else {
    return 'pending';
  }
}

/**
 * 解析日期字符串為 Date 對象
 */
function parseDate(dateString: string): Date {
  const [year, month, day] = dateString.split('/').map(Number);
  return new Date(year, month - 1, day);
}

/**
 * 更新路線圖狀態
 */
export function updateRoadmapStatus(roadmapData: WeekData[]): WeekData[] {
  return roadmapData.map(week => ({
    ...week,
    status: calculateWeekStatus(week)
  }));
}