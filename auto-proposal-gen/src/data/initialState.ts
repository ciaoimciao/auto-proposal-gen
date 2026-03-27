/**
 * 初始狀態數據
 */

import { AppState, BrandPersonality } from '../types';
import { generateRoadmapData } from '../utils/dateUtils';

/**
 * 生成初始應用狀態
 */
export function createInitialState(): AppState {
  return {
    currentSlide: 'cover',
    slides: [
      {
        id: 'cover',
        type: 'cover',
        title: '封面',
        content: {},
        order: 1
      },
      {
        id: 'brand',
        type: 'brand',
        title: '品牌策略',
        content: {},
        order: 2
      },
      {
        id: 'problem',
        type: 'problem',
        title: '問題分析',
        content: {},
        order: 3
      },
      {
        id: 'solution',
        type: 'solution',
        title: '解決方案',
        content: {},
        order: 4
      },
      {
        id: 'timeline',
        type: 'timeline',
        title: '時間軸',
        content: {},
        order: 5
      },
      {
        id: 'team',
        type: 'team',
        title: '團隊介紹',
        content: {},
        order: 6
      },
      {
        id: 'budget',
        type: 'budget',
        title: '預算規劃',
        content: {},
        order: 7
      },
      {
        id: 'summary',
        type: 'summary',
        title: '總結',
        content: {},
        order: 8
      }
    ],
    data: {
      cover: {
        title: '專案提案書',
        subtitle: '專業解決方案',
        date: new Date().toLocaleDateString('zh-TW'),
        client: '客戶名稱',
        presenter: '簡報人'
      },
      brand: {
        personality: 'minimal',
        colors: {
          primary: '#2563eb',
          secondary: '#64748b',
          accent: '#f59e0b'
        },
        logo: '',
        tagline: '專業、創新、可靠'
      },
      problem: {
        title: '問題分析',
        description: '詳細描述客戶面臨的問題和挑戰',
        painPoints: [
          '痛點 1：描述具體問題',
          '痛點 2：描述具體問題',
          '痛點 3：描述具體問題'
        ],
        impact: '這些問題對業務造成的影響和損失'
      },
      solution: {
        approach: '我們的解決方法和策略',
        features: [
          '功能特色 1：描述功能',
          '功能特色 2：描述功能',
          '功能特色 3：描述功能'
        ],
        benefits: [
          '效益 1：描述帶來的好處',
          '效益 2：描述帶來的好處',
          '效益 3：描述帶來的好處'
        ],
        timeline: '預計執行時間：3-6 個月'
      },
      timeline: {
        phases: [
          {
            name: '第一階段：需求分析',
            duration: '1 個月',
            milestones: [
              '完成需求調研',
              '制定詳細規格',
              '確認技術架構'
            ],
            deliverables: [
              '需求規格書',
              '技術架構圖',
              '項目計劃書'
            ]
          },
          {
            name: '第二階段：設計開發',
            duration: '2-3 個月',
            milestones: [
              '完成系統設計',
              '核心模組開發',
              '功能測試驗證'
            ],
            deliverables: [
              '系統設計文件',
              '核心功能模組',
              '測試報告'
            ]
          },
          {
            name: '第三階段：部署上線',
            duration: '1 個月',
            milestones: [
              '系統部署',
              '用戶培訓',
              '正式上線'
            ],
            deliverables: [
              '部署文件',
              '培訓材料',
              '上線報告'
            ]
          }
        ]
      },
      team: {
        members: [
          {
            name: '張經理',
            role: '專案經理',
            expertise: ['專案管理', '需求分析', '客戶溝通']
          },
          {
            name: '李工程師',
            role: '前端工程師',
            expertise: ['React', 'Vue.js', 'UI/UX 設計']
          },
          {
            name: '王工程師',
            role: '後端工程師',
            expertise: ['Node.js', '資料庫設計', 'API 開發']
          },
          {
            name: '陳設計師',
            role: 'UI/UX 設計師',
            expertise: ['介面設計', '使用者體驗', '視覺設計']
          }
        ],
        structure: '跨功能團隊，包含專案管理、開發、設計等專業人員',
        expertise: [
          'Web 開發',
          '移動應用開發',
          '雲端服務部署',
          '資料分析',
          '使用者體驗設計'
        ]
      },
      budget: {
        total: 500000,
        currency: 'NTD',
        breakdown: [
          {
            category: '人力成本',
            amount: 350000,
            description: '開發團隊薪資與福利'
          },
          {
            category: '硬體設備',
            amount: 50000,
            description: '伺服器與開發設備'
          },
          {
            category: '軟體授權',
            amount: 30000,
            description: '開發工具與第三方服務'
          },
          {
            category: '其他費用',
            amount: 70000,
            description: '差旅、教育訓練等雜項'
          }
        ]
      },
      summary: {
        keyPoints: [
          '完整的解決方案，滿足客戶需求',
          '專業的團隊，確保項目品質',
          '合理的預算規劃，控制成本風險',
          '明確的時間規劃，保證交付時程'
        ],
        nextSteps: [
          '確認合作意向',
          '簽訂合作協議',
          '啟動項目執行',
          '定期進度報告'
        ],
        contact: {
          name: '專案經理',
          email: 'project@company.com',
          phone: '+886-2-1234-5678',
          website: 'www.company.com'
        }
      },
      roadmap: {
        weeks: generateRoadmapData()
      }
    },
    settings: {
      theme: 'minimal',
      language: 'zh',
      exportFormat: 'html'
    }
  };
}

/**
 * 重置狀態為預設值
 */
export function resetToDefaultState(): AppState {
  return createInitialState();
}