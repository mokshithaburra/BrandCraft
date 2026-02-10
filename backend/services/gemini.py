from google import genai
from typing import Dict, List
import json
from config import GEMINI_API_KEY, GEMINI_MODEL

SYSTEM_PROMPT = """
You are BrandCraft, an expert branding strategist.
Return a compact JSON object with keys:
brand_name, tagline, story, personality, colors, typography, strategy, workflow, logo_prompt, brand_score
- colors must be an array of 3-5 hex values
- workflow must be an array of 4 short steps
- brand_score must be an integer 60-98
Keep the tone friendly, modern, and premium.
"""

FALLBACK = {
    "brand_name": "BrandCraft",
    "tagline": "Craft a brand that blooms",
    "story": "BrandCraft helps founders shape a clear, elegant identity with AI-guided strategy and visuals.",
    "personality": "Warm, visionary, confident",
    "colors": ["#F8C8DC", "#FFF2B2", "#111111", "#FFFFFF"],
    "typography": "Ballet for headlines, a clean sans for body",
    "strategy": "Content-led launch, social proof, and community-driven storytelling.",
    "workflow": ["Discovery", "Identity", "Visuals", "Launch"],
    "logo_prompt": "Minimal floral monogram logo, soft pastel palette, modern serif.",
    "brand_score": 86,
}
client = genai.Client(api_key=GEMINI_API_KEY)

async def generate_brand_content(payload: Dict[str, str]) -> Dict:
    if not GEMINI_API_KEY:
        return FALLBACK

    user_prompt = {
        "business_idea": payload.get("business_idea", ""),
        "industry": payload.get("industry", ""),
        "target_audience": payload.get("target_audience", ""),
        "brand_personality": payload.get("brand_personality", ""),
    }

    prompt = SYSTEM_PROMPT + "\nUser input: " + json.dumps(user_prompt)

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )

        text = (response.text or "").strip()

        if text.startswith("```"):
            text = text.strip("`")
            text = text.replace("json", "", 1).strip()

        return json.loads(text)

    except Exception as e:
        print("🔥 GEMINI ERROR:", e)
        return FALLBACK
    


