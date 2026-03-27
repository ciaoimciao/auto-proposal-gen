// ═══════════════════════════════════════
// Claude API Integration
// ═══════════════════════════════════════

import { FormData, Presentation } from '../types';

const CLAUDE_API_URL = 'https://api.anthropic.com/v1/messages';
const MODEL = 'claude-opus-4-6';
const MAX_TOKENS = 4096;

/**
 * 建立 Claude system prompt
 */
function buildSystemPrompt(lang: string, slideCount: string): string {
  const langNote = lang === 'zh'
    ? '所有投影片內容必須使用繁體中文，技術名詞可保留英文。'
    : 'Write all slide content in English.';

  return `You are a world-class business presentation consultant. You create concise, compelling, data-driven slide decks.
${langNote}
Respond with ONLY a valid JSON object — no markdown fences, no explanation, no extra text.

JSON schema:
{
  "title": "string — presentation title",
  "slides": [
    {
      "type": "cover|agenda|problem|solution|feature|timeline|team|budget|metric|closing",
      "title": "string",
      "subtitle": "string (optional)",
      "body": "string — 1-2 sentences of context (optional)",
      "points": ["string"] — bullet points (optional),
      "highlight": "string — key stat or number (optional)",
      "highlightLabel": "string — label for the highlight (optional)",
      "table": {
        "headers": ["string"],
        "rows": [["string"]]
      } (optional, for budget type only)
    }
  ]
}

Slide type rules:
- cover: title + subtitle (no points needed)
- agenda: title + points (list of topics covered)
- problem: title + body + 3-5 points (specific pain points)
- solution: title + body + 3-5 points (solution features/benefits)
- feature: title + 3-4 points ("Feature Name: short description")
- timeline: title + points ("Phase X — Name: tasks, duration")
- team: title + points ("Name / Role: key expertise")
- budget: title + table + highlight (total amount)
- metric: title + highlight (big number) + highlightLabel + body
- closing: title + points (next steps) + subtitle (contact)

Generate exactly ${slideCount} slides. Make content specific and professional, not generic.`;
}

/**
 * 建立 user prompt
 */
function buildUserPrompt(data: FormData): string {
  return `Create a business proposal presentation:
- Client: ${data.clientName || '（未指定）'}
- Project: ${data.projectName || '（未指定）'}
- Industry: ${data.industry}
- Presenter: ${data.presenter || '（未指定）'}
- Description: ${data.description}

Generate ${data.slideCount} slides telling a compelling story: context → problem → solution → plan → call to action.`;
}

/**
 * 呼叫 Claude API 生成投影片
 */
export async function generatePresentation(data: FormData): Promise<Presentation> {
  const response = await fetch(CLAUDE_API_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': data.apiKey,
      'anthropic-version': '2023-06-01',
      // Required for direct browser access (no backend proxy)
      'anthropic-dangerous-direct-browser-access': 'true'
    },
    body: JSON.stringify({
      model: MODEL,
      max_tokens: MAX_TOKENS,
      system: buildSystemPrompt(data.language, data.slideCount),
      messages: [{ role: 'user', content: buildUserPrompt(data) }]
    })
  });

  if (!response.ok) {
    const err = await response.json().catch(() => ({})) as any;
    throw new Error(err.error?.message || `API Error ${response.status}`);
  }

  const result = await response.json() as any;
  let text = result.content[0].text.trim();

  // Strip markdown code fences if Claude wraps the JSON
  const match = text.match(/```(?:json)?\s*([\s\S]*?)```/);
  if (match) text = match[1].trim();

  try {
    return JSON.parse(text) as Presentation;
  } catch {
    throw new Error('Claude 回傳格式錯誤，請重試');
  }
}
