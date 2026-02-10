# BrandCraft

AI branding assistant that generates brand identities and AI logos.

## Features
- Landing page with modern UI
- Chat dashboard for brand generation
- Gemini text generation
- Stable Diffusion logo generation
- Brand score and exportable brand kit

## Setup

### Backend
1. Open a terminal in `brandcraft-app/backend`.
2. Create and activate a virtual environment.
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and add your API keys.
5. Start the API:
   - `uvicorn main:app --reload`

### Frontend
1. Open `brandcraft-app/frontend/index.html` in a live server (VS Code Live Server or similar).
2. Click "Open Dashboard" to generate your brand.

## API
- `POST /generate-brand`
- `POST /generate-logo`

The frontend expects the API to run at `http://127.0.0.1:8000`.
