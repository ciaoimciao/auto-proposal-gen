/**
 * 幻燈片渲染組件
 */

import { Slide, SlideType, AppState } from '../types';

/**
 * 幻燈片渲染器
 */
export class SlideRenderer {
  private container: HTMLElement;

  constructor(containerId: string) {
    this.container = document.getElementById(containerId) as HTMLElement;
  }

  /**
   * 渲染指定幻燈片
   */
  renderSlide(slide: Slide, state: AppState): void {
    this.container.innerHTML = this.generateSlideHtml(slide, state);
  }

  /**
   * 生成幻燈片 HTML
   */
  private generateSlideHtml(slide: Slide, state: AppState): string {
    switch (slide.type) {
      case 'cover':
        return this.renderCoverSlide(state.data.cover);
      case 'brand':
        return this.renderBrandSlide(state.data.brand);
      case 'problem':
        return this.renderProblemSlide(state.data.problem);
      case 'solution':
        return this.renderSolutionSlide(state.data.solution);
      case 'timeline':
        return this.renderTimelineSlide(state.data.timeline);
      case 'team':
        return this.renderTeamSlide(state.data.team);
      case 'budget':
        return this.renderBudgetSlide(state.data.budget);
      case 'summary':
        return this.renderSummarySlide(state.data.summary);
      default:
        return this.renderDefaultSlide(slide);
    }
  }

  /**
   * 渲染封面頁
   */
  private renderCoverSlide(data: any): string {
    return `
      <div class="slide cover-slide">
        <div class="slide-content">
          <h1 class="title">${data.title}</h1>
          <h2 class="subtitle">${data.subtitle}</h2>
          <div class="info-grid">
            <div class="info-item">
              <span class="label">客戶：</span>
              <span class="value">${data.client}</span>
            </div>
            <div class="info-item">
              <span class="label">日期：</span>
              <span class="value">${data.date}</span>
            </div>
            <div class="info-item">
              <span class="label">簡報人：</span>
              <span class="value">${data.presenter}</span>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  /**
   * 渲染品牌頁
   */
  private renderBrandSlide(data: any): string {
    return `
      <div class="slide brand-slide">
        <div class="slide-content">
          <h1 class="title">品牌策略</h1>
          <div class="brand-info">
            <div class="personality">
              <h2>品牌個性</h2>
              <div class="personality-badge">${this.getPersonalityText(data.personality)}</div>
            </div>
            <div class="tagline">
              <h2>品牌標語</h2>
              <p>${data.tagline}</p>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  /**
   * 渲染問題頁
   */
  private renderProblemSlide(data: any): string {
    return `
      <div class="slide problem-slide">
        <div class="slide-content">
          <h1 class="title">${data.title}</h1>
          <div class="problem-content">
            <div class="description">
              <h2>問題描述</h2>
              <p>${data.description}</p>
            </div>
            <div class="pain-points">
              <h2>痛點分析</h2>
              <ul>
                ${data.painPoints.map((point: string) => `<li>${point}</li>`).join('')}
              </ul>
            </div>
            <div class="impact">
              <h2>影響評估</h2>
              <p>${data.impact}</p>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  /**
   * 渲染解決方案頁
   */
  private renderSolutionSlide(data: any): string {
    return `
      <div class="slide solution-slide">
        <div class="slide-content">
          <h1 class="title">解決方案</h1>
          <div class="solution-content">
            <div class="approach">
              <h2>解決方法</h2>
              <p>${data.approach}</p>
            </div>
            <div class="features">
              <h2>核心功能</h2>
              <ul>
                ${data.features.map((feature: string) => `<li>${feature}</li>`).join('')}
              </ul>
            </div>
            <div class="benefits">
              <h2>預期效益</h2>
              <ul>
                ${data.benefits.map((benefit: string) => `<li>${benefit}</li>`).join('')}
              </ul>
            </div>
            <div class="timeline">
              <h2>執行時間</h2>
              <p>${data.timeline}</p>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  /**
   * 渲染時間軸頁
   */
  private renderTimelineSlide(data: any): string {
    return `
      <div class="slide timeline-slide">
        <div class="slide-content">
          <h1 class="title">時間軸規劃</h1>
          <div class="timeline-content">
            ${data.phases.map((phase: any) => `
              <div class="phase">
                <h2>${phase.name}</h2>
                <p class="duration">持續時間：${phase.duration}</p>
                <div class="milestones">
                  <h3>里程碑</h3>
                  <ul>
                    ${phase.milestones.map((milestone: string) => `<li>${milestone}</li>`).join('')}
                  </ul>
                </div>
                <div class="deliverables">
                  <h3>交付物</h3>
                  <ul>
                    ${phase.deliverables.map((deliverable: string) => `<li>${deliverable}</li>`).join('')}
                  </ul>
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      </div>
    `;
  }

  /**
   * 渲染團隊頁
   */
  private renderTeamSlide(data: any): string {
    return `
      <div class="slide team-slide">
        <div class="slide-content">
          <h1 class="title">團隊介紹</h1>
          <div class="team-content">
            <div class="structure">
              <h2>團隊結構</h2>
              <p>${data.structure}</p>
            </div>
            <div class="expertise">
              <h2>專業領域</h2>
              <ul>
                ${data.expertise.map((expertise: string) => `<li>${expertise}</li>`).join('')}
              </ul>
            </div>
            <div class="members">
              <h2>團隊成員</h2>
              ${data.members.map((member: any) => `
                <div class="member">
                  <h3>${member.name}</h3>
                  <p class="role">${member.role}</p>
                  <ul class="skills">
                    ${member.expertise.map((skill: string) => `<li>${skill}</li>`).join('')}
                  </ul>
                </div>
              `).join('')}
            </div>
          </div>
        </div>
      </div>
    `;
  }

  /**
   * 渲染預算頁
   */
  private renderBudgetSlide(data: any): string {
    return `
      <div class="slide budget-slide">
        <div class="slide-content">
          <h1 class="title">預算規劃</h1>
          <div class="budget-content">
            <div class="total-budget">
              <h2>總預算</h2>
              <p class="amount">${data.currency} ${data.total.toLocaleString()}</p>
            </div>
            <div class="breakdown">
              <h2>預算明細</h2>
              <table>
                <thead>
                  <tr>
                    <th>類別</th>
                    <th>金額</th>
                    <th>說明</th>
                  </tr>
                </thead>
                <tbody>
                  ${data.breakdown.map((item: any) => `
                    <tr>
                      <td>${item.category}</td>
                      <td>${data.currency} ${item.amount.toLocaleString()}</td>
                      <td>${item.description}</td>
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  /**
   * 渲染總結頁
   */
  private renderSummarySlide(data: any): string {
    return `
      <div class="slide summary-slide">
        <div class="slide-content">
          <h1 class="title">總結</h1>
          <div class="summary-content">
            <div class="key-points">
              <h2>關鍵要點</h2>
              <ul>
                ${data.keyPoints.map((point: string) => `<li>${point}</li>`).join('')}
              </ul>
            </div>
            <div class="next-steps">
              <h2>後續步驟</h2>
              <ul>
                ${data.nextSteps.map((step: string) => `<li>${step}</li>`).join('')}
              </ul>
            </div>
            <div class="contact">
              <h2>聯絡資訊</h2>
              <div class="contact-info">
                <p><strong>聯絡人：</strong>${data.contact.name}</p>
                <p><strong>郵箱：</strong>${data.contact.email}</p>
                <p><strong>電話：</strong>${data.contact.phone}</p>
                <p><strong>網站：</strong>${data.contact.website}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  /**
   * 渲染預設幻燈片
   */
  private renderDefaultSlide(slide: Slide): string {
    return `
      <div class="slide default-slide">
        <div class="slide-content">
          <h1 class="title">${slide.title}</h1>
          <div class="content">
            <p>此幻燈片類型尚未實現</p>
          </div>
        </div>
      </div>
    `;
  }

  /**
   * 獲取品牌個性文字
   */
  private getPersonalityText(personality: string): string {
    switch (personality) {
      case 'minimal':
        return '極簡專業';
      case 'bold':
        return '大膽創新';
      case 'warm':
        return '溫暖親和';
      default:
        return personality;
    }
  }
}