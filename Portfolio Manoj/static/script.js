// Run all code when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function() {
    
    // --- 1. THEME TOGGLE LOGIC ---
    const themeToggle = document.getElementById('theme-toggle');
    themeToggle.addEventListener('click', () => {
        document.documentElement.classList.toggle('light-mode');
        if (document.documentElement.classList.contains('light-mode')) {
            localStorage.setItem('theme', 'light');
        } else {
            localStorage.setItem('theme', 'dark');
        }
    });


    // --- 2. STICKY NAV & SMOOTH SCROLL ---
    const navLinks = document.querySelectorAll('.nav-links a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });


    // --- 3. STAGGERED ANIMATION ---
    const animatedElements = document.querySelectorAll('.stagger-fade');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                const children = entry.target.children;
                for (let i = 0; i < children.length; i++) {
                    // Apply delay to each child
                    if (children[i]) {
                         children[i].style.transitionDelay = `${i * 100}ms`;
                    }
                }
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    animatedElements.forEach(el => {
        observer.observe(el);
    });


    // --- 4. ### OLD EXPERIENCE ACCORDION SCRIPT IS DELETED ### ---
    

    // --- 5. PROJECT & EXPERIENCE MODAL LOGIC ---
    // This one script now handles BOTH project and experience modals
    const modalOpenBtns = document.querySelectorAll('.modal-open-btn');
    const modalCloseBtns = document.querySelectorAll('.modal-close-btn');
    const modalOverlay = document.getElementById('modal-overlay');

    // Re-usable function to open a modal
    function openModal(modal) {
        if (modal == null) return;
        modal.classList.add('active');
        modalOverlay.classList.add('active');
    }

    // Re-usable function to close a modal
    function closeModal(modal) {
        if (modal == null) return;
        modal.classList.remove('active');
        modalOverlay.classList.remove('active');
    }

    modalOpenBtns.forEach(button => {
        button.addEventListener('click', () => {
            const modal = document.querySelector(button.dataset.modalTarget);
            openModal(modal);
        });
    });

    modalCloseBtns.forEach(button => {
        button.addEventListener('click', () => {
            const modal = button.closest('.modal');
            closeModal(modal);
        });
    });

    modalOverlay.addEventListener('click', () => {
        const activeModal = document.querySelector('.modal.active');
        closeModal(activeModal);
    });


    // --- 6. CONTACT FORM (AJAX) SUBMISSION ---
    const contactForm = document.getElementById('contact-form');
    const formStatus = document.getElementById('form-status');

    function setStatus(message, type) {
        if (!formStatus) return;
        formStatus.innerHTML = message;
        formStatus.className = type;
    }

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const form = e.target;
            const formData = new FormData(form);
            const action = form.action;
            const object = {};
            formData.forEach((value, key) => { object[key] = value; });
            const json = JSON.stringify(object);

            setStatus('Sending...', 'pending');

            fetch(action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: json
            })
            .then(async (response) => {
                let jsonResponse = await response.json();
                if (response.status == 200) {
                    setStatus(jsonResponse.message || 'Thanks! Your message has been sent.', 'success');
                    form.reset();
                } else {
                    setStatus(jsonResponse.message || 'Oops! There was a problem.', 'error');
                }
            })
            .catch(error => {
                setStatus('Oops! There was a network error.', 'error');
            });
        });
    }

    // --- 7. GITHUB REDIRECT LOGIC ---
    const redirectBtns = document.querySelectorAll('.github-redirect-btn');
    const redirectOverlay = document.getElementById('redirect-overlay');
    
    redirectBtns.forEach(button => {
        button.addEventListener('click', () => {
            const url = button.dataset.href;
            if (url === "#") return; // Do nothing for private projects

            // Close any open modals first
            const activeModal = document.querySelector('.modal.active');
            if (activeModal) {
                closeModal(activeModal);
            }

            // Show the redirect overlay
            if (redirectOverlay) {
                redirectOverlay.classList.add('active');
            }

            // Wait 3 seconds, then redirect
            setTimeout(() => {
                window.open(url, '_blank');
                // We'll just leave the overlay active in the original tab
            }, 3000); // 3 seconds
        });
    });

});