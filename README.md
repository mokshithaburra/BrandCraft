# BrandCraft

AI branding assistant that generates brand identities and AI logos.

---

## 📝 Resume-Ready Project Description

> **BrandCraft** — an AI-powered branding platform that generates complete brand identities in under 30 seconds. Built with a **FastAPI** backend and a responsive **vanilla JavaScript** frontend, the app integrates **Google Gemini** for brand-strategy text generation and **Stable Diffusion XL** for AI logo creation. A single API call returns a brand name, tagline, story, color palette, typography, marketing strategy, and growth workflow — reducing the typical brand-development cycle from weeks to seconds. The platform serves **5 brand categories** (Startup, Creator, Influencer, Business, Personal Brand) and delivers a quantified **brand score (60–98%)** with every generation. Users can export the full brand kit as a downloadable file. Deployed on **Render** with CORS-enabled RESTful endpoints, BrandCraft demonstrates end-to-end full-stack development, third-party AI API integration, async processing, and responsive UI/UX design.

---

## 🛠️ Complete Tech Stack

### Backend
| Technology | Version | Purpose |
|---|---|---|
| **Python** | 3.x | Backend runtime |
| **FastAPI** | 0.115.0 | Async REST API framework |
| **Uvicorn** | 0.30.6 | ASGI production server |
| **Pydantic** | 2.8.2 | Request/response data validation |
| **httpx** | 0.27.2 | Async HTTP client for external API calls |
| **python-dotenv** | 1.0.1 | Environment variable management |
| **google-generativeai** | 0.7.2 | Google Gemini API SDK |

### Frontend
| Technology | Purpose |
|---|---|
| **HTML5** | Semantic page structure |
| **CSS3** (Custom Properties, Keyframe Animations) | Styling, theming, responsive design |
| **Vanilla JavaScript** (ES6+) | Client-side logic, async fetch, DOM manipulation |
| **Google Fonts** (Ballet, Sora) | Typography |

### AI / ML APIs
| Service | Model | Purpose |
|---|---|---|
| **Google Gemini** | gemini-flash-latest | Brand strategy text generation (name, tagline, story, colors, typography, marketing strategy) |
| **Stability AI** | Stable Diffusion XL 1024 v1.0 | AI logo image generation from text prompts |

### DevOps & Deployment
| Tool | Purpose |
|---|---|
| **Render** | Backend hosting & deployment (live at `brandcraft-ihtv.onrender.com`) |
| **Static Hosting** | Frontend served as static HTML/CSS/JS |
| **Git / GitHub** | Version control & collaboration |

### Architecture
| Aspect | Details |
|---|---|
| **Pattern** | Client–Server with RESTful API |
| **Communication** | JSON over HTTPS |
| **CORS** | Enabled via FastAPI middleware |
| **State** | Stateless (no database; on-demand generation) |
| **Error Handling** | Graceful fallback data on API failures |

---

## ✨ Features
- Modern dark-themed landing page with animated gradient backgrounds and logo orbit
- Interactive dashboard for brand generation with real-time brand score
- AI-generated brand identity: name, tagline, story, personality, colors, typography, marketing strategy, and growth workflow
- AI logo generation with regenerate support
- Exportable brand kit (`.txt` download)
- Responsive design (mobile-friendly at ≤ 980 px)
- 5 brand categories: Startup, Creator, Influencer, Business, Personal Brand
- Testimonial carousel with auto-rotation

---

## 🚀 Setup

### Backend
1. Open a terminal in `backend/`.
2. Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with the following keys:
   ```
   GEMINI_API_KEY=<your-google-gemini-api-key>
   STABILITY_API_KEY=<your-stability-ai-api-key>
   ```
5. Start the API:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend
1. Open `frontend/index.html` in a live server (VS Code Live Server or similar).
2. Click **"Open Dashboard"** to generate your brand.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `GET` | `/health` | API status |
| `POST` | `/generate-brand` | Generate a complete brand identity |
| `POST` | `/generate-logo` | Generate an AI logo |

The frontend expects the API at `http://127.0.0.1:8000` (local) or the Render deployment URL (production).

---

## 📂 Project Structure

```
BrandCraft/
├── backend/
│   ├── main.py              # FastAPI app, routes, CORS middleware
│   ├── config.py            # Environment variable configuration
│   ├── models.py            # Pydantic request/response schemas
│   ├── requirements.txt     # Python dependencies
│   ├── requirements.lock    # Locked dependency versions
│   ├── services/
│   │   ├── gemini.py        # Google Gemini integration
│   │   └── stable_diffusion.py  # Stable Diffusion integration
│   └── tools/
│       └── list_gemini_models.py
├── frontend/
│   ├── index.html           # Landing page
│   ├── dashboard.html       # Brand generation dashboard
│   ├── script.js            # Dashboard logic & API calls
│   └── styles.css           # Styling & animations
├── index.html               # Root landing page
├── script.js                # Root-level JS
├── styles.css               # Root-level CSS
└── README.md
```
