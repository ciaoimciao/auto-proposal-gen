/**
 * 路線圖編輯器組件
 */

import { WeekData } from '../types';
import { generateRoadmapData, updateRoadmapStatus } from '../utils/dateUtils';

/**
 * 路線圖編輯器
 */
export class RoadmapEditor {
  private container: HTMLElement;
  private weeks: WeekData[] = [];

  constructor(containerId: string) {
    this.container = document.getElementById(containerId) as HTMLElement;
    this.initialize();
  }

  /**
   * 初始化組件
   */
  private initialize(): void {
    this.generateDefaultData();
    this.render();
    this.bindEvents();
  }

  /**
   * 生成預設數據
   */
  private generateDefaultData(): void {
    this.weeks = generateRoadmapData();
  }

  /**
   * 渲染路線圖
   */
  render(): void {
    this.container.innerHTML = `
      <div class="roadmap-editor">
        <div class="editor-header">
          <h2>路線圖編輯器</h2>
          <div class="controls">
            <button class="btn btn-primary" onclick="window.roadmapEditor.generateNewData()">重新生成</button>
            <button class="btn btn-secondary" onclick="window.roadmapEditor.updateStatus()">更新狀態</button>
          </div>
        </div>
        <div class="roadmap-grid">
          ${this.weeks.map((week, index) => this.renderWeekCard(week, index)).join('')}
        </div>
      </div>
    `;
  }

  /**
   * 渲染單週卡片
   */
  private renderWeekCard(week: WeekData, index: number): string {
    const statusClass = this.getStatusClass(week.status);
    return `
      <div class="week-card ${statusClass}">
        <div class="week-header">
          <h3>第 ${week.week} 週</h3>
          <span class="week-dates">${week.startDate} - ${week.endDate}</span>
          <span class="status-badge ${week.status}">${this.getStatusText(week.status)}</span>
        </div>
        <div class="week-content">
          <div class="milestones">
            <h4>里程碑</h4>
            <div class="milestone-list">
              ${week.milestones.map((milestone, i) => `
                <div class="milestone-item">
                  <input type="text" 
                         value="${milestone}" 
                         class="milestone-input"
                         data-week="${index}"
                         data-index="${i}"
                         data-type="milestone"
                         oninput="window.roadmapEditor.updateData(this)">
                </div>
              `).join('')}
              <button class="btn btn-small" onclick="window.roadmapEditor.addMilestone(${index})">+ 新增里程碑</button>
            </div>
          </div>
          <div class="deliverables">
            <h4>交付物</h4>
            <div class="deliverable-list">
              ${week.deliverables.map((deliverable, i) => `
                <div class="deliverable-item">
                  <input type="text" 
                         value="${deliverable}" 
                         class="deliverable-input"
                         data-week="${index}"
                         data-index="${i}"
                         data-type="deliverable"
                         oninput="window.roadmapEditor.updateData(this)">
                </div>
              `).join('')}
              <button class="btn btn-small" onclick="window.roadmapEditor.addDeliverable(${index})">+ 新增交付物</button>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  /**
   * 綁定事件
   */
  private bindEvents(): void {
    // 將方法綁定到 window 對象，以便在 HTML 中調用
    (window as any).roadmapEditor = this;
  }

  /**
   * 重新生成數據
   */
  generateNewData(): void {
    this.generateDefaultData();
    this.render();
  }

  /**
   * 更新狀態
   */
  updateStatus(): void {
    this.weeks = updateRoadmapStatus(this.weeks);
    this.render();
  }

  /**
   * 更新數據
   */
  updateData(input: HTMLInputElement): void {
    const weekIndex = parseInt(input.dataset.week || '0');
    const itemIndex = parseInt(input.dataset.index || '0');
    const type = input.dataset.type as 'milestone' | 'deliverable';
    const value = input.value;

    if (type === 'milestone') {
      this.weeks[weekIndex].milestones[itemIndex] = value;
    } else if (type === 'deliverable') {
      this.weeks[weekIndex].deliverables[itemIndex] = value;
    }
  }

  /**
   * 新增里程碑
   */
  addMilestone(weekIndex: number): void {
    this.weeks[weekIndex].milestones.push('新里程碑');
    this.render();
  }

  /**
   * 新增交付物
   */
  addDeliverable(weekIndex: number): void {
    this.weeks[weekIndex].deliverables.push('新交付物');
    this.render();
  }

  /**
   * 獲取路線圖數據
   */
  getRoadmapData(): WeekData[] {
    return this.weeks;
  }

  /**
   * 設置路線圖數據
   */
  setRoadmapData(weeks: WeekData[]): void {
    this.weeks = weeks;
    this.render();
  }

  /**
   * 獲取狀態類名
   */
  private getStatusClass(status: string): string {
    switch (status) {
      case 'completed':
        return 'status-completed';
      case 'in_progress':
        return 'status-in-progress';
      case 'pending':
        return 'status-pending';
      default:
        return '';
    }
  }

  /**
   * 獲取狀態文字
   */
  private getStatusText(status: string): string {
    switch (status) {
      case 'completed':
        return '已完成';
      case 'in_progress':
        return '進行中';
      case 'pending':
        return '未開始';
      default:
        return status;
    }
  }
}