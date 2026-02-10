const API_BASE = 'http://127.0.0.1:8000';

const carousel = document.getElementById('carousel');
const dotsContainer = document.getElementById('carouselDots');
const scrollBtn = document.getElementById('scrollTestimonials');

if (carousel && dotsContainer) {
  const items = Array.from(carousel.children);
  items.forEach((_, index) => {
    const dot = document.createElement('div');
    dot.className = 'carousel-dot' + (index === 0 ? ' active' : '');
    dot.addEventListener('click', () => setActive(index));
    dotsContainer.appendChild(dot);
  });

  let activeIndex = 0;
  const setActive = (index) => {
    activeIndex = index;
    items.forEach((item, i) => item.classList.toggle('active', i === index));
    dotsContainer.querySelectorAll('.carousel-dot').forEach((dot, i) => {
      dot.classList.toggle('active', i === index);
    });
  };

  setInterval(() => {
    setActive((activeIndex + 1) % items.length);
  }, 4000);
}

if (scrollBtn) {
  scrollBtn.addEventListener('click', () => {
    document.getElementById('testimonials')?.scrollIntoView({ behavior: 'smooth' });
  });
}

const brandForm = document.getElementById('brandForm');
const chatContent = document.getElementById('chatContent');
const typing = document.getElementById('typing');
const scoreProgress = document.getElementById('scoreProgress');
const scoreValue = document.getElementById('scoreValue');
const logoImage = document.getElementById('logoImage');
const regenLogo = document.getElementById('regenLogo');
const exportKit = document.getElementById('exportKit');

let latestLogoPrompt = '';
let latestBrandData = null;

const updateScore = (payload) => {
  const base = Math.min(90, 60 + Math.round((payload.business_idea.length + payload.brand_personality.length) / 3));
  const score = Math.min(98, base);
  scoreProgress.style.width = `${score}%`;
  scoreValue.textContent = `${score}%`;
};

const renderChat = (data) => {
  chatContent.innerHTML = '';
  const blocks = [
    ['Brand Name', data.brand_name],
    ['Tagline', data.tagline],
    ['Brand Story', data.story],
    ['Brand Personality', data.personality],
    ['Color Suggestions', data.colors.join(', ')],
    ['Typography Style', data.typography],
    ['Marketing Strategy', data.strategy],
    ['Growth Strategy', data.workflow.join(' → ')],
  ];

  blocks.forEach(([title, text]) => {
    const card = document.createElement('div');
    card.className = 'chat-card';
    card.innerHTML = `<h4>${title}</h4><p>${text}</p>`;
    chatContent.appendChild(card);
  });
};

const generateBrand = async (payload) => {
  typing.textContent = 'Crafting your brand…';
  typing.style.visibility = 'visible';

  const response = await fetch(`${API_BASE}/generate-brand`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });

  const data = await response.json();
  latestBrandData = data;
  latestLogoPrompt = data.logo_prompt;
  renderChat(data);
  updateScore(payload);
  typing.textContent = 'Brand ready ✨';

  await generateLogo(data.logo_prompt);
};

const generateLogo = async (logoPrompt) => {
  if (!logoPrompt) return;
  logoImage.src = '';

  const response = await fetch(`${API_BASE}/generate-logo`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ logo_prompt: logoPrompt }),
  });

  const data = await response.json();
  logoImage.src = data.image_url;
};

if (brandForm) {
  brandForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(brandForm);
    const payload = {
      business_idea: formData.get('businessIdea'),
      industry: formData.get('industry'),
      target_audience: formData.get('audience'),
      brand_personality: formData.get('personality'),
    };
    generateBrand(payload).catch(() => {
      typing.textContent = 'Something went wrong. Please try again.';
    });
  });
}

if (regenLogo) {
  regenLogo.addEventListener('click', () => {
    generateLogo(latestLogoPrompt).catch(() => {});
  });
}

if (exportKit) {
  exportKit.addEventListener('click', () => {
    if (!latestBrandData) return;
    const content = `BrandCraft Kit\n\nBrand Name: ${latestBrandData.brand_name}\nTagline: ${latestBrandData.tagline}\nStory: ${latestBrandData.story}\nPersonality: ${latestBrandData.personality}\nColors: ${latestBrandData.colors.join(', ')}\nTypography: ${latestBrandData.typography}\nStrategy: ${latestBrandData.strategy}\nWorkflow: ${latestBrandData.workflow.join(' -> ')}\nLogo Prompt: ${latestBrandData.logo_prompt}`;
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'brandcraft-kit.txt';
    a.click();
    URL.revokeObjectURL(url);
  });
}
