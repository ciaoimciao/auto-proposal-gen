/**
 * 導出工具函數
 */

import { AppState } from '../types';

/**
 * 導出為 JSON 格式
 */
export function exportToJson(state: AppState): string {
  return JSON.stringify(state, null, 2);
}

/**
 * 導出為 HTML 格式
 */
export function exportToHtml(state: AppState): string {
  const html = `
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${state.data.cover.title}</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        .slide { page-break-after: always; margin: 20px; }
        .slide h1 { color: var(--color-primary); }
        .slide h2 { color: var(--color-secondary); }
    </style>
</head>
<body>
    ${generateSlidesHtml(state)}
</body>
</html>
  `;
  return html;
}

/**
 * 生成幻燈片 HTML
 */
function generateSlidesHtml(state: AppState): string {
  return state.slides.map(slide => {
    switch (slide.type) {
      case 'cover':
        return generateCoverHtml(state.data.cover);
      case 'brand':
        return generateBrandHtml(state.data.brand);
      case 'problem':
        return generateProblemHtml(state.data.problem);
      case 'solution':
        return generateSolutionHtml(state.data.solution);
      case 'timeline':
        return generateTimelineHtml(state.data.timeline);
      case 'team':
        return generateTeamHtml(state.data.team);
      case 'budget':
        return generateBudgetHtml(state.data.budget);
      case 'summary':
        return generateSummaryHtml(state.data.summary);
      default:
        return `<div class="slide"><h1>${slide.title}</h1></div>`;
    }
  }).join('');
}

/**
 * 生成封面 HTML
 */
function generateCoverHtml(data: any): string {
  return `
    <div class="slide">
        <h1>${data.title}</h1>
        <h2>${data.subtitle}</h2>
        <p>客戶：${data.client}</p>
        <p>日期：${data.date}</p>
        <p>簡報人：${data.presenter}</p>
    </div>
  `;
}

/**
 * 生成品牌頁 HTML
 */
function generateBrandHtml(data: any): string {
  return `
    <div class="slide">
        <h1>品牌策略</h1>
        <h2>品牌個性：${data.personality}</h2>
        <p>標語：${data.tagline}</p>
    </div>
  `;
}

/**
 * 生成問題頁 HTML
 */
function generateProblemHtml(data: any): string {
  return `
    <div class="slide">
        <h1>${data.title}</h1>
        <p>${data.description}</p>
        <ul>
            ${data.painPoints.map((point: string) => `<li>${point}</li>`).join('')}
        </ul>
        <p>影響：${data.impact}</p>
    </div>
  `;
}

/**
 * 生成解決方案頁 HTML
 */
function generateSolutionHtml(data: any): string {
  return `
    <div class="slide">
        <h1>解決方案</h1>
        <p>方法：${data.approach}</p>
        <ul>
            ${data.features.map((feature: string) => `<li>${feature}</li>`).join('')}
        </ul>
        <ul>
            ${data.benefits.map((benefit: string) => `<li>${benefit}</li>`).join('')}
        </ul>
        <p>時間：${data.timeline}</p>
    </div>
  `;
}

/**
 * 生成時間軸 HTML
 */
function generateTimelineHtml(data: any): string {
  return `
    <div class="slide">
        <h1>時間軸</h1>
        ${data.phases.map((phase: any) => `
            <div>
                <h3>${phase.name}</h3>
                <p>持續時間：${phase.duration}</p>
                <ul>
                    ${phase.milestones.map((milestone: string) => `<li>${milestone}</li>`).join('')}
                </ul>
                <ul>
                    ${phase.deliverables.map((deliverable: string) => `<li>${deliverable}</li>`).join('')}
                </ul>
            </div>
        `).join('')}
    </div>
  `;
}

/**
 * 生成團隊頁 HTML
 */
function generateTeamHtml(data: any): string {
  return `
    <div class="slide">
        <h1>團隊介紹</h1>
        <p>結構：${data.structure}</p>
        <ul>
            ${data.expertise.map((expertise: string) => `<li>${expertise}</li>`).join('')}
        </ul>
        ${data.members.map((member: any) => `
            <div>
                <h3>${member.name}</h3>
                <p>角色：${member.role}</p>
                <ul>
                    ${member.expertise.map((skill: string) => `<li>${skill}</li>`).join('')}
                </ul>
            </div>
        `).join('')}
    </div>
  `;
}

/**
 * 生成預算頁 HTML
 */
function generateBudgetHtml(data: any): string {
  return `
    <div class="slide">
        <h1>預算規劃</h1>
        <p>總預算：${data.currency} ${data.total.toLocaleString()}</p>
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
  `;
}

/**
 * 生成總結頁 HTML
 */
function generateSummaryHtml(data: any): string {
  return `
    <div class="slide">
        <h1>總結</h1>
        <ul>
            ${data.keyPoints.map((point: string) => `<li>${point}</li>`).join('')}
        </ul>
        <ul>
            ${data.nextSteps.map((step: string) => `<li>${step}</li>`).join('')}
        </ul>
        <div>
            <p>聯絡人：${data.contact.name}</p>
            <p>郵箱：${data.contact.email}</p>
            <p>電話：${data.contact.phone}</p>
            <p>網站：${data.contact.website}</p>
        </div>
    </div>
  `;
}

/**
 * 下載文件
 */
export function downloadFile(content: string, filename: string, mimeType: string): void {
  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}