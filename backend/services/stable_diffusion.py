from typing import Dict
import httpx
from config import STABILITY_API_KEY, STABILITY_ENGINE

STABILITY_URL = "https://api.stability.ai/v1/generation/{engine}/text-to-image"

async def generate_logo_image(payload: Dict[str, str]) -> str:
    if not STABILITY_API_KEY:
        # Placeholder image from a data URI (simple transparent pixel)
        return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAASsJTYQAAAAASUVORK5CYII="

    prompt = (payload.get("logo_prompt") or "Minimal modern logo").strip()

    headers = {
        "Authorization": f"Bearer {STABILITY_API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    body = {
        "text_prompts": [{"text": prompt, "weight": 1}],
        "cfg_scale": 7,
        "height": 512,
        "width": 512,
        "steps": 30,
        "samples": 1,
    }

    url = STABILITY_URL.format(engine=STABILITY_ENGINE)

    try:
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(url, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()

        image_b64 = data["artifacts"][0]["base64"]
        return f"data:image/png;base64,{image_b64}"
    except Exception:
        return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAASsJTYQAAAAASUVORK5CYII="
