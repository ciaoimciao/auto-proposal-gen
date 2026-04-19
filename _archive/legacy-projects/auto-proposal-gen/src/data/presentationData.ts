/**
 * 簡報資料結構定義
 */

// 模組類型定義
export interface Module {
  id: string;
  title: string;
  content: string;
  order: number;
  enabled: boolean;
}

// 簡報資料結構
export interface PresentationData {
  clientName: string;
  projectName: string;
  date: string;
  presenter: string;
  modules: Module[];
}

/**
 * 生成預設簡報資料
 */
export function createPresentationData(): PresentationData {
  return {
    clientName: '客戶名稱',
    projectName: '專案名稱',
    date: new Date().toLocaleDateString('zh-TW'),
    presenter: '簡報人',
    modules: [
      {
        id: 'M01',
        title: '封面頁',
        content: `
          <h1>{{Project_Name}}</h1>
          <h2>專案提案書</h2>
          <div class="info-grid">
            <div class="info-item">客戶：{{Client_Name}}</div>
            <div class="info-item">日期：{{Date}}</div>
            <div class="info-item">簡報人：{{Presenter}}</div>
          </div>
        `,
        order: 1,
        enabled: true
      },
      {
        id: 'M02',
        title: '議程',
        content: `
          <h2>會議議程</h2>
          <ul>
            <li>1. 專案背景與目標</li>
            <li>2. 現況分析</li>
            <li>3. 解決方案</li>
            <li>4. 執行計畫</li>
            <li>5. 預算規劃</li>
            <li>6. Q&A</li>
          </ul>
        `,
        order: 2,
        enabled: true
      },
      {
        id: 'M03',
        title: '專案背景',
        content: `
          <h2>專案背景</h2>
          <p>隨著 {{Client_Name}} 業務的快速發展，現有的 {{Project_Name}} 系統已無法滿足日益增長的業務需求。本專案旨在...</p>
          <ul>
            <li>提升系統效能與穩定性</li>
            <li>改善使用者體驗</li>
            <li>支持未來業務擴展</li>
          </ul>
        `,
        order: 3,
        enabled: true
      },
      {
        id: 'M04',
        title: '目標與願景',
        content: `
          <h2>專案目標</h2>
          <div class="goals-grid">
            <div class="goal-item">
              <h3>短期目標</h3>
              <p>6 個月內完成核心功能開發與上線</p>
            </div>
            <div class="goal-item">
              <h3>中期目標</h3>
              <p>1 年內實現業務流程全面數位化</p>
            </div>
            <div class="goal-item">
              <h3>長期目標</h3>
              <p>3 年內建立智慧化決策支援系統</p>
            </div>
          </div>
        `,
        order: 4,
        enabled: true
      },
      {
        id: 'M05',
        title: '現況分析',
        content: `
          <h2>現況分析</h2>
          <div class="analysis-grid">
            <div class="analysis-item">
              <h3>優勢</h3>
              <ul>
                <li>{{Client_Name}} 在業界的領導地位</li>
                <li>成熟的業務流程</li>
                <li>穩定的客戶基礎</li>
              </ul>
            </div>
            <div class="analysis-item">
              <h3>劣勢</h3>
              <ul>
                <li>系統老舊，維護成本高</li>
                <li>資料分散，整合困難</li>
                <li>缺乏即時分析能力</li>
              </ul>
            </div>
            <div class="analysis-item">
              <h3>機會</h3>
              <ul>
                <li>數位轉型趨勢</li>
                <li>新興技術應用</li>
                <li>市場需求增長</li>
              </ul>
            </div>
            <div class="analysis-item">
              <h3>威脅</h3>
              <ul>
                <li>競爭對手技術升級</li>
                <li>法規政策變化</li>
                <li>人才短缺</li>
              </ul>
            </div>
          </div>
        `,
        order: 5,
        enabled: true
      },
      {
        id: 'M06',
        title: '痛點分析',
        content: `
          <h2>痛點分析</h2>
          <div class="pain-points">
            <div class="pain-point">
              <h3>痛點 1：系統效能問題</h3>
              <p>現有系統反應緩慢，影響工作效率</p>
              <div class="impact">影響：每日損失 2 小時工作效率</div>
            </div>
            <div class="pain-point">
              <h3>痛點 2：資料孤島</h3>
              <p>各部門資料分散，無法有效整合</p>
              <div class="impact">影響：決策缺乏完整資訊支援</div>
            </div>
            <div class="pain-point">
              <h3>痛點 3：擴展性不足</h3>
              <p>系統架構限制，難以支持業務成長</p>
              <div class="impact">影響：錯失市場機會</div>
            </div>
          </div>
        `,
        order: 6,
        enabled: true
      },
      {
        id: 'M07',
        title: '解決方案',
        content: `
          <h2>解決方案</h2>
          <div class="solution-overview">
            <h3>整體架構</h3>
            <p>我們將為 {{Client_Name}} 建立一個全新的 {{Project_Name}} 系統，採用...</p>
            
            <div class="solution-features">
              <div class="feature">
                <h4>模組化設計</h4>
                <p>可根據業務需求靈活擴展</p>
              </div>
              <div class="feature">
                <h4>雲端部署</h4>
                <p>提升系統可用性與彈性</p>
              </div>
              <div class="feature">
                <h4>數據整合</h4>
                <p>打破資料孤島，實現資訊共享</p>
              </div>
              <div class="feature">
                <h4>智慧分析</h4>
                <p>提供即時洞察與預測分析</p>
              </div>
            </div>
          </div>
        `,
        order: 7,
        enabled: true
      },
      {
        id: 'M08',
        title: '技術架構',
        content: `
          <h2>技術架構</h2>
          <div class="architecture-diagram">
            <div class="layer">
              <h3>前端層</h3>
              <ul>
                <li>React.js</li>
                <li>Vue.js</li>
                <li>響應式設計</li>
              </ul>
            </div>
            <div class="layer">
              <h3>應用層</h3>
              <ul>
                <li>Node.js</li>
                <li>微服務架構</li>
                <li>API Gateway</li>
              </ul>
            </div>
            <div class="layer">
              <h3>資料層</h3>
              <ul>
                <li>PostgreSQL</li>
                <li>MongoDB</li>
                <li>Redis</li>
              </ul>
            </div>
            <div class="layer">
              <h3>基礎設施</h3>
              <ul>
                <li>AWS/Azure</li>
                <li>Docker</li>
                <li>Kubernetes</li>
              </ul>
            </div>
          </div>
        `,
        order: 8,
        enabled: true
      },
      {
        id: 'M09',
        title: '執行計畫',
        content: `
          <h2>執行計畫</h2>
          <div class="timeline">
            <div class="phase">
              <h3>Phase 1：需求分析 (1個月)</h3>
              <ul>
                <li>業務流程梳理</li>
                <li>技術需求確認</li>
                <li>風險評估</li>
              </ul>
            </div>
            <div class="phase">
              <h3>Phase 2：設計開發 (3個月)</h3>
              <ul>
                <li>系統架構設計</li>
                <li>核心模組開發</li>
                <li>測試驗證</li>
              </ul>
            </div>
            <div class="phase">
              <h3>Phase 3：部署上線 (1個月)</h3>
              <ul>
                <li>系統部署</li>
                <li>用戶培訓</li>
                <li>正式上線</li>
              </ul>
            </div>
          </div>
        `,
        order: 9,
        enabled: true
      },
      {
        id: 'M10',
        title: '風險評估',
        content: `
          <h2>風險評估與因應策略</h2>
          <div class="risk-assessment">
            <table>
              <thead>
                <tr>
                  <th>風險項目</th>
                  <th>影響程度</th>
                  <th>發生機率</th>
                  <th>因應策略</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>技術整合風險</td>
                  <td>高</td>
                  <td>中</td>
                  <td>提前進行技術驗證，建立備援方案</td>
                </tr>
                <tr>
                  <td>時程延遲</td>
                  <td>中</td>
                  <td>低</td>
                  <td>制定詳細時程表，定期追蹤進度</td>
                </tr>
                <tr>
                  <td>預算超支</td>
                  <td>中</td>
                  <td>低</td>
                  <td>嚴格成本控制，預留應急預算</td>
                </tr>
              </tbody>
            </table>
          </div>
        `,
        order: 10,
        enabled: true
      },
      {
        id: 'M11',
        title: '效益分析',
        content: `
          <h2>效益分析</h2>
          <div class="benefits-analysis">
            <div class="benefit-category">
              <h3>直接效益</h3>
              <ul>
                <li>工作效率提升 40%</li>
                <li>營運成本降低 25%</li>
                <li>錯誤率減少 60%</li>
              </ul>
            </div>
            <div class="benefit-category">
              <h3>間接效益</h3>
              <ul>
                <li>客戶滿意度提升</li>
                <li>品牌形象改善</li>
                <li>市場競爭力增強</li>
              </ul>
            </div>
            <div class="benefit-category">
              <h3>長期效益</h3>
              <ul>
                <li>數據資產累積</li>
                <li>決策支援能力</li>
                <li>業務創新基礎</li>
              </ul>
            </div>
          </div>
        `,
        order: 11,
        enabled: true
      },
      {
        id: 'M12',
        title: '時程規劃',
        content: `
          <h2>時程規劃</h2>
          <div class="roadmap">
            <div class="week-planning">
              <h3>第 1 週：需求分析</h3>
              <p>日期：{{Date}} - {{EndDate}}</p>
              <ul>
                <li>與 {{Client_Name}} 團隊深入訪談</li>
                <li>現有系統評估</li>
                <li>業務流程梳理</li>
              </ul>
            </div>
            <div class="week-planning">
              <h3>第 2 週：方案設計</h3>
              <p>日期：{{Date}} - {{EndDate}}</p>
              <ul>
                <li>技術架構設計</li>
                <li>介面原型設計</li>
                <li>資料模型建立</li>
              </ul>
            </div>
            <div class="week-planning">
              <h3>第 3 週：核心開發</h3>
              <p>日期：{{Date}} - {{EndDate}}</p>
              <ul>
                <li>基礎框架搭建</li>
                <li>核心模組開發</li>
                <li>單元測試</li>
              </ul>
            </div>
            <div class="week-planning">
              <h3>第 4 週：整合測試</h3>
              <p>日期：{{Date}} - {{EndDate}}</p>
              <ul>
                <li>模組整合</li>
                <li>系統測試</li>
                <li>效能優化</li>
              </ul>
            </div>
            <div class="week-planning">
              <h3>第 5 週：部署上線</h3>
              <p>日期：{{Date}} - {{EndDate}}</p>
              <ul>
                <li>生產環境部署</li>
                <li>用戶培訓</li>
                <li>正式上線</li>
              </ul>
            </div>
          </div>
        `,
        order: 12,
        enabled: true
      },
      {
        id: 'M13',
        title: '預算規劃',
        content: `
          <h2>預算規劃</h2>
          <div class="budget-breakdown">
            <table>
              <thead>
                <tr>
                  <th>項目</th>
                  <th>金額</th>
                  <th>說明</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>人力成本</td>
                  <td>NT$ 350,000</td>
                  <td>開發團隊 5 人，5 個月</td>
                </tr>
                <tr>
                  <td>硬體設備</td>
                  <td>NT$ 50,000</td>
                  <td>伺服器與開發設備</td>
                </tr>
                <tr>
                  <td>軟體授權</td>
                  <td>NT$ 30,000</td>
                  <td>開發工具與第三方服務</td>
                </tr>
                <tr>
                  <td>其他費用</td>
                  <td>NT$ 70,000</td>
                  <td>差旅、教育訓練等</td>
                </tr>
                <tr class="total-row">
                  <td><strong>總計</strong></td>
                  <td><strong>NT$ 500,000</strong></td>
                  <td></td>
                </tr>
              </tbody>
            </table>
          </div>
        `,
        order: 13,
        enabled: true
      },
      {
        id: 'M14',
        title: '團隊介紹',
        content: `
          <h2>執行團隊</h2>
          <div class="team-intro">
            <div class="team-member">
              <h3>專案經理</h3>
              <p>10 年專案管理經驗，PMP 認證</p>
              <ul>
                <li>擅長跨部門協調</li>
                <li>風險管控專家</li>
                <li>客戶溝通橋樑</li>
              </ul>
            </div>
            <div class="team-member">
              <h3>技術主管</h3>
              <p>15 年軟體開發經驗，架構設計專家</p>
              <ul>
                <li>雲端技術專家</li>
                <li>效能優化能手</li>
                <li>技術顧問</li>
              </ul>
            </div>
            <div class="team-member">
              <h3>前端工程師</h3>
              <p>5 年前端開發經驗，UI/UX 設計</p>
              <ul>
                <li>React/Vue 專家</li>
                <li>響應式設計</li>
                <li>使用者體驗</li>
              </ul>
            </div>
            <div class="team-member">
              <h3>後端工程師</h3>
              <p>8 年後端開發經驗，資料庫專家</p>
              <ul>
                <li>API 設計</li>
                <li>資料庫優化</li>
                <li>安全防護</li>
              </ul>
            </div>
          </div>
        `,
        order: 14,
        enabled: true
      },
      {
        id: 'M15',
        title: '總結與下一步',
        content: `
          <h2>總結與下一步</h2>
          <div class="summary-next-steps">
            <div class="summary-points">
              <h3>專案亮點</h3>
              <ul>
                <li>完整的解決方案，滿足 {{Client_Name}} 需求</li>
                <li>專業的執行團隊，確保項目品質</li>
                <li>合理的預算規劃，控制成本風險</li>
                <li>明確的時間規劃，保證交付時程</li>
              </ul>
            </div>
            <div class="next-steps">
              <h3>後續步驟</h3>
              <ol>
                <li>確認合作意向</li>
                <li>簽訂合作協議</li>
                <li>成立專案小組</li>
                <li>啟動項目執行</li>
                <li>定期進度報告</li>
              </ol>
            </div>
            <div class="contact-info">
              <h3>聯絡資訊</h3>
              <p>如有任何問題，請隨時與我們聯繫：</p>
              <p>專案經理：{{Presenter}}</p>
              <p>電話：+886-2-1234-5678</p>
              <p>郵箱：project@company.com</p>
            </div>
          </div>
        `,
        order: 15,
        enabled: true
      }
    ]
  };
}

/**
 * 快速模式模組 ID
 */
export const QUICK_MODE_MODULES = ['M01', 'M03', 'M05', 'M07', 'M12', 'M13', 'M15'];

/**
 * 完整模式模組 ID
 */
export const FULL_MODE_MODULES = [
  'M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 
  'M08', 'M09', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15'
];

/**
 * 應用變數到內容
 */
export function applyVariables(content: string, data: PresentationData): string {
  return content
    .replace(/\{\{Client_Name\}\}/g, data.clientName)
    .replace(/\{\{Project_Name\}\}/g, data.projectName)
    .replace(/\{\{Date\}\}/g, data.date)
    .replace(/\{\{Presenter\}\}/g, data.presenter)
    .replace(/\{\{EndDate\}\}/g, calculateEndDate(data.date, 7)); // 7天後的日期
}

/**
 * 計算結束日期
 */
function calculateEndDate(startDate: string, days: number): string {
  const date = new Date(startDate);
  date.setDate(date.getDate() + days);
  return date.toLocaleDateString('zh-TW');
}

/**
 * 過濾模組
 */
export function filterModules(modules: Module[], mode: 'quick' | 'full'): Module[] {
  const targetModules = mode === 'quick' ? QUICK_MODE_MODULES : FULL_MODE_MODULES;
  return modules
    .filter(module => targetModules.includes(module.id))
    .sort((a, b) => a.order - b.order);
}