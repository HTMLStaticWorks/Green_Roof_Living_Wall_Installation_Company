
document.addEventListener('DOMContentLoaded', () => {
    // Theme logic
    const themeToggleDesktop = document.getElementById('theme-toggle-desktop');
    const themeToggleMobile = document.getElementById('theme-toggle-mobile');
    
    function setTheme(isDark) {
        if (isDark) {
            document.documentElement.classList.add('dark');
            localStorage.setItem('theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('theme', 'light');
        }
    }
    
    // Init theme
    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        setTheme(true);
    } else {
        setTheme(false);
    }

    if(themeToggleDesktop) themeToggleDesktop.addEventListener('click', () => setTheme(!document.documentElement.classList.contains('dark')));
    if(themeToggleMobile) themeToggleMobile.addEventListener('click', () => setTheme(!document.documentElement.classList.contains('dark')));

    // RTL logic
    const rtlToggleDesktop = document.getElementById('rtl-toggle-desktop');
    const rtlToggleMobile = document.getElementById('rtl-toggle-mobile');
    
    function setRtl(isRtl) {
        if (isRtl) {
            document.documentElement.setAttribute('dir', 'rtl');
            localStorage.setItem('dir', 'rtl');
        } else {
            document.documentElement.setAttribute('dir', 'ltr');
            localStorage.setItem('dir', 'ltr');
        }
    }
    
    if (localStorage.getItem('dir') === 'rtl') {
        setRtl(true);
    }

    if(rtlToggleDesktop) rtlToggleDesktop.addEventListener('click', () => setRtl(document.documentElement.getAttribute('dir') !== 'rtl'));
    if(rtlToggleMobile) rtlToggleMobile.addEventListener('click', () => {
        setRtl(document.documentElement.getAttribute('dir') !== 'rtl');
    });

    // Mobile menu
    const btn = document.getElementById('mobile-menu-btn');
    const menu = document.getElementById('mobile-menu');
    const iconOpen = document.getElementById('menu-icon-open');
    const iconClose = document.getElementById('menu-icon-close');
    
    if (btn && menu) {
        btn.addEventListener('click', () => {
            menu.classList.toggle('hidden');
            iconOpen.classList.toggle('hidden');
            iconClose.classList.toggle('hidden');
        });

        // Close menu on link click
        const links = menu.querySelectorAll('.mobile-nav-link');
        links.forEach(link => {
            link.addEventListener('click', () => {
                menu.classList.add('hidden');
                iconOpen.classList.remove('hidden');
                iconClose.classList.add('hidden');
            });
        });
    }

    // Scroll to top
    const scrollToTopBtn = document.getElementById('scroll-to-top');
    if (scrollToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                scrollToTopBtn.classList.remove('opacity-0', 'pointer-events-none');
                scrollToTopBtn.classList.add('opacity-100', 'pointer-events-auto');
            } else {
                scrollToTopBtn.classList.add('opacity-0', 'pointer-events-none');
                scrollToTopBtn.classList.remove('opacity-100', 'pointer-events-auto');
            }
        });
        
        scrollToTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Set active nav link based on current path
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const allLinks = document.querySelectorAll('.nav-link, .mobile-nav-link');
    allLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath) {
            // Desktop active classes
            if (link.classList.contains('nav-link')) {
                link.classList.add('text-emerald-700', 'dark:text-emerald-400');
                link.classList.remove('text-neutral-600', 'dark:text-neutral-300');
            }
            // Mobile active classes
            if (link.classList.contains('mobile-nav-link')) {
                link.classList.add('text-emerald-700', 'dark:text-emerald-400', 'bg-emerald-50', 'dark:bg-emerald-900/30');
                link.classList.remove('text-neutral-700', 'dark:text-neutral-200');
            }
        }
    });

    // Form validations
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Enquiry submitted successfully!');
            contactForm.reset();
        });
    }

    const authForm = document.getElementById('auth-form');
    if (authForm) {
        authForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // basic check for password match on signup
            const pwd = document.getElementById('password');
            const confirm = document.getElementById('confirm-password');
            if(confirm && pwd.value !== confirm.value) {
                alert('Passwords do not match');
                return;
            }
            
            alert('Form submitted successfully!');
            window.location.href = 'index.html';
        });
    }
});
