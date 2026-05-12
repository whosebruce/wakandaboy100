document.getElementById('year').textContent = new Date().getFullYear();
const cards = document.querySelectorAll('.work-card, .platform-grid a, .shorts-stack a');
const io = 'IntersectionObserver' in window ? new IntersectionObserver(entries => {
  entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('is-visible'); });
}, { threshold: 0.12 }) : null;
cards.forEach(card => io && io.observe(card));
