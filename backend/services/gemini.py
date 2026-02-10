from typing import Dict
import json
import logging

import google.generativeai as genai

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

async def generate_brand_content(payload: Dict[str, str]) -> Dict:
    if not GEMINI_API_KEY:
        logging.warning("GEMINI_API_KEY is missing; using fallback response.")
        return FALLBACK

    user_prompt = {
        "business_idea": payload.get("business_idea", ""),
        "industry": payload.get("industry", ""),
        "target_audience": payload.get("target_audience", ""),
        "brand_personality": payload.get("brand_personality", ""),
    }

    prompt = SYSTEM_PROMPT + "\nUser input: " + json.dumps(user_prompt)

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(prompt)
        text = (response.text or "").strip()
    except Exception:
        logging.exception("Gemini request failed; using fallback response.")
        return FALLBACK

    if not text:
        return FALLBACK

    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        text = "\n".join(lines).strip()
        if text.lower().startswith("json"):
            text = text[4:].strip()

    try:
        return json.loads(text)
    except Exception:
        return FALLBACK

