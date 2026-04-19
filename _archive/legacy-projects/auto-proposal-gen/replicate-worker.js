/**
 * Cloudflare Worker — Replicate API Proxy
 *
 * Deploy:
 *   1. Go to https://dash.cloudflare.com → Workers & Pages → Create
 *   2. Paste this entire file → Deploy
 *   3. Copy the worker URL (e.g. https://replicate-proxy.your-name.workers.dev)
 *   4. Paste it into the Proposal Generator's Settings Panel
 */

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

export default {
  async fetch(request) {
    // Handle CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: CORS });
    }

    const url = new URL(request.url);

    try {
      // POST /predict — Create a new prediction
      if (request.method === 'POST' && url.pathname === '/predict') {
        const body = await request.json();
        const { replicateToken, model, version, ...rest } = body;

        if (!replicateToken) {
          return json({ error: 'Missing replicateToken' }, 400);
        }

        // Support both model-based and version-based predictions
        let apiUrl;
        let payload;

        if (model) {
          // Model-based: POST /v1/models/{owner}/{name}/predictions
          apiUrl = `https://api.replicate.com/v1/models/${model}/predictions`;
          payload = rest; // { input: { ... } }
        } else if (version) {
          // Version-based: POST /v1/predictions
          apiUrl = 'https://api.replicate.com/v1/predictions';
          payload = { version, ...rest };
        } else {
          return json({ error: 'Missing model or version' }, 400);
        }

        const res = await fetch(apiUrl, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${replicateToken}`,
            'Content-Type': 'application/json',
            'Prefer': 'wait',
          },
          body: JSON.stringify(payload),
        });

        const data = await res.json();
        return json(data, res.status);
      }

      // GET /predict/:id?token=xxx — Poll prediction status
      if (request.method === 'GET' && url.pathname.startsWith('/predict/')) {
        const predictionId = url.pathname.split('/predict/')[1];
        const token = url.searchParams.get('token');

        if (!token || !predictionId) {
          return json({ error: 'Missing token or prediction ID' }, 400);
        }

        const res = await fetch(`https://api.replicate.com/v1/predictions/${predictionId}`, {
          headers: { 'Authorization': `Bearer ${token}` },
        });

        const data = await res.json();
        return json(data, res.status);
      }

      return json({ error: 'Not found. Use POST /predict or GET /predict/:id' }, 404);

    } catch (err) {
      return json({ error: err.message }, 500);
    }
  },
};

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { ...CORS, 'Content-Type': 'application/json' },
  });
}
