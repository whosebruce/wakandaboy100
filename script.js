/* 
   ---------------------------------------------------------
   DATA CONFIGURATION
   Add your projects here.
   'youtubeId': The code at the end of a YouTube URL (e.g. dQw4w9WgXcQ)
   ---------------------------------------------------------
*/
const projects = [
    {
        id: 1,
        title: "Hit Single Visuals",
        artist: "Big Artist Name",
        category: "video",
        role: "Director & Editor",
        youtubeId: "placeholder", 
        image: "images/project1.jpg", 
        description: "Directed the official music video for [Artist Name]. The concept focused on high-energy performance and neon aesthetics.",
        tags: ["Music Video", "Direction", "4K"]
    },
    {
        id: 2,
        title: "Summer Vibe Anthem",
        artist: "Famous Rapper",
        category: "video",
        role: "Director of Photography",
        youtubeId: "placeholder", 
        image: "images/project2.jpg",
        description: "Captured the summer vibes for this chart-topping track. Shot on location in Miami featuring complex drone work.",
        tags: ["Cinematography", "Outdoor", "Drone"]
    },
    {
        id: 3,
        title: "TV Series: Crime Drama",
        artist: "Network TV",
        category: "acting",
        role: "Supporting Actor (Detective)",
        youtubeId: "", 
        image: "images/acting1.jpg",
        description: "Appeared in Season 3 Episode 4 as Detective Johnson. Delivered key dialogue in a high-stakes interrogation scene.",
        tags: ["Acting", "Drama", "TV"]
    },
    {
        id: 4,
        title: "Streetwear Brand Launch",
        artist: "Fashion Brand",
        category: "commercial",
        role: "Creative Director",
        youtubeId: "placeholder", 
        image: "images/comm1.jpg",
        description: "Produced the launch campaign for a new luxury streetwear line. Managed the entire visual identity from video to stills.",
        tags: ["Fashion", "Commercial", "Branding"]
    }
];

// ----------------------
// LOGIC (Do not edit below unless you know JS)
// ----------------------

const projectGrid = document.getElementById('projectGrid');
const filterBtns = document.querySelectorAll('.filter-btn');

// Initial Render
renderProjects(projects);

// Filter Function
function filterProjects(category) {
    filterBtns.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
    
    const filtered = category === 'all' 
        ? projects 
        : projects.filter(p => p.category === category);
    
    projectGrid.innerHTML = '';
    renderProjects(filtered);
}

// Render Function
function renderProjects(items) {
    items.forEach((project, index) => {
        const card = document.createElement('div');
        card.className = 'project-card';
        card.style.animationDelay = `${index * 0.1}s`;
        
        // Use placeholder if image fails
        const imgUrl = project.image || `https://via.placeholder.com/600x400/111/333?text=${project.title}`;
        
        card.innerHTML = `
            <div class="project-image">
                <img src="${imgUrl}" alt="${project.title}" onerror="this.src='https://via.placeholder.com/600x400/111/333?text=Image+Missing'">
                ${project.youtubeId ? '<div class="play-icon">▶</div>' : ''}
            </div>
            <div class="project-content">
                <div class="project-meta">${project.artist || 'Personal Project'}</div>
                <h3 class="project-title">${project.title}</h3>
                <div class="project-role">${project.role}</div>
                <p class="project-description">${project.description.substring(0, 80)}...</p>
                <div class="project-tags">
                    ${project.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
                </div>
            </div>
        `;
        
        card.addEventListener('click', () => openModal(project));
        projectGrid.appendChild(card);
        
        setTimeout(() => card.classList.add('visible'), 50);
    });
}

// Modal functionality
const modal = document.getElementById('projectModal');
const modalClose = document.getElementById('modalClose');
const modalMedia = document.getElementById('modalMedia');

function openModal(project) {
    document.getElementById('modalTitle').textContent = project.title;
    document.getElementById('modalRole').textContent = project.role;
    document.getElementById('modalCategory').textContent = project.artist;
    document.getElementById('modalDescription').textContent = project.description;
    document.getElementById('modalTags').innerHTML = project.tags.map(tag => `<span class="tag">${tag}</span>`).join('');
    
    // Handle Media
    if (project.youtubeId && project.youtubeId !== "placeholder") {
        modalMedia.innerHTML = `
            <iframe 
                src="https://www.youtube.com/embed/${project.youtubeId}?autoplay=1" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
            </iframe>`;
    } else {
        const imgUrl = project.image || `https://via.placeholder.com/600x400/111/333?text=${project.title}`;
        modalMedia.innerHTML = `<img src="${imgUrl}" style="width:100%; height:100%; object-fit:cover;" alt="${project.title}">`;
    }
    
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    modal.classList.remove('active');
    modalMedia.innerHTML = ''; 
    document.body.style.overflow = 'auto';
}

modalClose.addEventListener('click', closeModal);
modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
});

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if(target) target.scrollIntoView({ behavior: 'smooth' });
    });
});
