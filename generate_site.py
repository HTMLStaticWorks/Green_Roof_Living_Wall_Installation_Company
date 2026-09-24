import os

def create_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"d:\SEPT WEBSITES\Green Roof & Living Wall Installation Company"
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# Helper for common head and tail
def get_head(title):
    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | EcoArch Living Architecture</title>
    <meta name="description" content="Premium green roof and living wall installation company specializing in sustainable modern architecture.">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        emerald: {{
                            50: '#ecfdf5',
                            100: '#d1fae5',
                            200: '#a7f3d0',
                            300: '#6ee7b7',
                            400: '#34d399',
                            500: '#10b981',
                            600: '#059669',
                            700: '#047857',
                            800: '#065f46',
                            900: '#064e3b',
                            950: '#022c22',
                        }},
                        neutral: {{
                            850: '#1f1f1f',
                        }}
                    }},
                    fontFamily: {{
                        sans: ['Inter', 'system-ui', 'sans-serif'],
                        heading: ['Outfit', 'system-ui', 'sans-serif'],
                    }}
                }}
            }}
        }}
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body class="bg-neutral-50 dark:bg-neutral-950 text-neutral-800 dark:text-neutral-200 antialiased transition-colors duration-300 flex flex-col min-h-screen">
"""

shared_header = """
    <!-- Header -->
    <header class="fixed w-full top-0 z-50 bg-white/90 dark:bg-neutral-900/90 backdrop-blur-md shadow-sm border-b border-neutral-200 dark:border-neutral-800 transition-all duration-300" id="navbar">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <!-- Logo -->
                <a href="index.html" class="flex-shrink-0 flex items-center gap-2 group">
                    <svg class="h-8 w-8 text-emerald-700 dark:text-emerald-500 group-hover:scale-105 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
                    </svg>
                    <span class="font-heading font-bold text-2xl tracking-tight text-neutral-900 dark:text-white">EcoArch</span>
                </a>
                
                <!-- Desktop Menu -->
                <nav class="hidden md:flex space-x-8 items-center" id="desktop-menu">
                    <a href="index.html" class="nav-link text-sm font-medium text-neutral-600 hover:text-emerald-700 dark:text-neutral-300 dark:hover:text-emerald-400 transition-colors">Home 1</a>
                    <a href="home2.html" class="nav-link text-sm font-medium text-neutral-600 hover:text-emerald-700 dark:text-neutral-300 dark:hover:text-emerald-400 transition-colors">Home 2</a>
                    <a href="about.html" class="nav-link text-sm font-medium text-neutral-600 hover:text-emerald-700 dark:text-neutral-300 dark:hover:text-emerald-400 transition-colors">About</a>
                    <a href="services.html" class="nav-link text-sm font-medium text-neutral-600 hover:text-emerald-700 dark:text-neutral-300 dark:hover:text-emerald-400 transition-colors">Services</a>
                    <a href="portfolio.html" class="nav-link text-sm font-medium text-neutral-600 hover:text-emerald-700 dark:text-neutral-300 dark:hover:text-emerald-400 transition-colors">Portfolio</a>
                    <a href="blog.html" class="nav-link text-sm font-medium text-neutral-600 hover:text-emerald-700 dark:text-neutral-300 dark:hover:text-emerald-400 transition-colors">Blog</a>
                    <a href="contact.html" class="nav-link text-sm font-medium text-neutral-600 hover:text-emerald-700 dark:text-neutral-300 dark:hover:text-emerald-400 transition-colors">Contact</a>
                </nav>

                <div class="hidden md:flex items-center space-x-5">
                    <button id="theme-toggle-desktop" class="p-2 rounded-full hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-colors text-neutral-500 dark:text-neutral-400" aria-label="Toggle Theme">
                        <svg class="w-5 h-5 hidden dark:block" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/></svg>
                        <svg class="w-5 h-5 block dark:hidden" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
                    </button>
                    <button id="rtl-toggle-desktop" class="text-xs font-semibold px-2 py-1 border border-neutral-300 dark:border-neutral-600 rounded text-neutral-500 dark:text-neutral-400 hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-colors">
                        RTL
                    </button>
                    <a href="login.html" class="px-5 py-2.5 text-sm font-medium text-white bg-neutral-900 dark:bg-emerald-600 hover:bg-neutral-800 dark:hover:bg-emerald-500 rounded transition-colors shadow-sm">Client Portal</a>
                </div>

                <!-- Mobile menu button -->
                <div class="flex items-center md:hidden gap-3">
                    <button id="mobile-menu-btn" class="p-2 rounded-md text-neutral-600 dark:text-neutral-300 hover:bg-neutral-100 dark:hover:bg-neutral-800 focus:outline-none transition-colors">
                        <svg class="h-6 w-6 block" id="menu-icon-open" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
                        </svg>
                        <svg class="h-6 w-6 hidden" id="menu-icon-close" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                        </svg>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Menu -->
        <div class="md:hidden hidden bg-white dark:bg-neutral-900 border-t border-neutral-200 dark:border-neutral-800 absolute w-full left-0 shadow-xl" id="mobile-menu">
            <div class="px-4 pt-4 pb-6 space-y-2">
                <a href="index.html" class="mobile-nav-link block px-4 py-3 rounded text-base font-medium text-neutral-700 dark:text-neutral-200 hover:bg-neutral-50 dark:hover:bg-neutral-800 transition-colors">Home 1</a>
                <a href="home2.html" class="mobile-nav-link block px-4 py-3 rounded text-base font-medium text-neutral-700 dark:text-neutral-200 hover:bg-neutral-50 dark:hover:bg-neutral-800 transition-colors">Home 2</a>
                <a href="about.html" class="mobile-nav-link block px-4 py-3 rounded text-base font-medium text-neutral-700 dark:text-neutral-200 hover:bg-neutral-50 dark:hover:bg-neutral-800 transition-colors">About</a>
                <a href="services.html" class="mobile-nav-link block px-4 py-3 rounded text-base font-medium text-neutral-700 dark:text-neutral-200 hover:bg-neutral-50 dark:hover:bg-neutral-800 transition-colors">Services</a>
                <a href="portfolio.html" class="mobile-nav-link block px-4 py-3 rounded text-base font-medium text-neutral-700 dark:text-neutral-200 hover:bg-neutral-50 dark:hover:bg-neutral-800 transition-colors">Portfolio</a>
                <a href="blog.html" class="mobile-nav-link block px-4 py-3 rounded text-base font-medium text-neutral-700 dark:text-neutral-200 hover:bg-neutral-50 dark:hover:bg-neutral-800 transition-colors">Blog</a>
                <a href="contact.html" class="mobile-nav-link block px-4 py-3 rounded text-base font-medium text-neutral-700 dark:text-neutral-200 hover:bg-neutral-50 dark:hover:bg-neutral-800 transition-colors">Contact</a>
                
                <div class="flex items-center justify-between px-4 py-4 border-t border-neutral-200 dark:border-neutral-800 mt-4">
                    <button id="theme-toggle-mobile" class="flex items-center gap-2 py-2 text-sm font-medium text-neutral-600 dark:text-neutral-300">
                        <span class="dark:hidden">Dark Mode</span>
                        <span class="hidden dark:inline">Light Mode</span>
                    </button>
                    <button id="rtl-toggle-mobile" class="flex items-center gap-2 py-2 text-sm font-medium text-neutral-600 dark:text-neutral-300">
                        <span>Toggle RTL</span>
                    </button>
                </div>
                <div class="px-2 pt-2">
                     <a href="login.html" class="block w-full text-center px-5 py-3 text-base font-medium text-white bg-neutral-900 dark:bg-emerald-600 rounded transition-colors">Client Portal</a>
                </div>
            </div>
        </div>
    </header>
    
    <!-- Main Content wrapper to push footer down -->
    <main class="flex-grow pt-20">
"""

shared_footer = """
    </main>
    
    <!-- Footer -->
    <footer class="bg-neutral-950 text-neutral-400 py-16 border-t border-neutral-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-8">
                <!-- Brand -->
                <div class="space-y-6">
                    <a href="index.html" class="flex items-center gap-2">
                        <svg class="h-8 w-8 text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
                        </svg>
                        <span class="font-heading font-bold text-2xl tracking-tight text-white">EcoArch</span>
                    </a>
                    <p class="text-sm leading-relaxed max-w-xs">
                        Pioneering sustainable architecture through premium green roof and living wall systems for modern urban spaces.
                    </p>
                    <div class="flex space-x-4">
                        <a href="#" class="text-neutral-500 hover:text-white transition-colors" aria-label="LinkedIn">
                            <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                        </a>
                        <a href="#" class="text-neutral-500 hover:text-white transition-colors" aria-label="Instagram">
                            <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                        </a>
                    </div>
                </div>
                
                <!-- Quick Links -->
                <div>
                    <h3 class="text-white font-heading font-semibold mb-6 uppercase tracking-wider text-sm">Navigation</h3>
                    <ul class="space-y-4 text-sm">
                        <li><a href="about.html" class="hover:text-emerald-500 transition-colors">About Us</a></li>
                        <li><a href="portfolio.html" class="hover:text-emerald-500 transition-colors">Our Portfolio</a></li>
                        <li><a href="blog.html" class="hover:text-emerald-500 transition-colors">Insights & News</a></li>
                        <li><a href="contact.html" class="hover:text-emerald-500 transition-colors">Contact</a></li>
                    </ul>
                </div>
                
                <!-- Services -->
                <div>
                    <h3 class="text-white font-heading font-semibold mb-6 uppercase tracking-wider text-sm">Expertise</h3>
                    <ul class="space-y-4 text-sm">
                        <li><a href="services.html" class="hover:text-emerald-500 transition-colors">Extensive Green Roofs</a></li>
                        <li><a href="services.html" class="hover:text-emerald-500 transition-colors">Intensive Roof Gardens</a></li>
                        <li><a href="services.html" class="hover:text-emerald-500 transition-colors">Exterior Living Walls</a></li>
                        <li><a href="services.html" class="hover:text-emerald-500 transition-colors">Long-term Maintenance</a></li>
                    </ul>
                </div>
                
                <!-- Contact -->
                <div>
                    <h3 class="text-white font-heading font-semibold mb-6 uppercase tracking-wider text-sm">Studio</h3>
                    <ul class="space-y-4 text-sm">
                        <li class="flex gap-3">
                            <svg class="h-5 w-5 text-neutral-600 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                            <span>450 Architecture Blvd, Suite 200<br>Design District, NY 10012</span>
                        </li>
                        <li class="flex gap-3">
                            <svg class="h-5 w-5 text-neutral-600 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                            <a href="mailto:hello@ecoarch.com" class="hover:text-white transition-colors">hello@ecoarch.com</a>
                        </li>
                        <li class="flex gap-3">
                            <svg class="h-5 w-5 text-neutral-600 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                            <span>+1 (555) 123-4567</span>
                        </li>
                    </ul>
                </div>
            </div>
            
            <div class="mt-16 pt-8 border-t border-neutral-800 flex flex-col md:flex-row justify-between items-center gap-4 text-xs">
                <p>&copy; 2026 EcoArch Living Architecture. All rights reserved.</p>
                <div class="flex space-x-6">
                    <a href="#" class="hover:text-white transition-colors">Privacy Policy</a>
                    <a href="#" class="hover:text-white transition-colors">Terms & Conditions</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Scroll to top button -->
    <button id="scroll-to-top" class="fixed bottom-8 right-8 bg-neutral-900 dark:bg-emerald-600 text-white p-3 rounded-full shadow-lg opacity-0 pointer-events-none transition-all duration-300 hover:-translate-y-1 z-40" aria-label="Scroll to top">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"/></svg>
    </button>

    <script src="js/main.js"></script>
</body>
</html>
"""

def generate_page(title, content, include_header_footer=True):
    if include_header_footer:
        return get_head(title) + shared_header + content + shared_footer
    else:
        return get_head(title) + content + '<script src="js/main.js"></script>\n</body>\n</html>'


# ----- CSS & JS -----
css_content = """
/* Custom styles */
@layer utilities {
    .text-balance {
        text-wrap: balance;
    }
}
html {
    scroll-behavior: smooth;
}
"""

js_content = """
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
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath) {
            link.classList.add('text-emerald-700', 'dark:text-emerald-400');
            link.classList.remove('text-neutral-600', 'dark:text-neutral-300');
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
"""

import os
os.makedirs(os.path.join(base_dir, 'css'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'js'), exist_ok=True)
create_file(os.path.join(base_dir, 'css', 'style.css'), css_content)
create_file(os.path.join(base_dir, 'js', 'main.js'), js_content)


# ----- HOME 1 -----
home1_content = """
<!-- Section 1: Architectural Hero -->
<section class="relative min-h-[90vh] flex items-center bg-neutral-100 dark:bg-neutral-900 overflow-hidden">
    <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80" alt="Modern building with green roof" class="w-full h-full object-cover object-center" />
        <div class="absolute inset-0 bg-neutral-900/40 dark:bg-neutral-950/60 backdrop-blur-[2px]"></div>
    </div>
    
    <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full py-20">
        <div class="max-w-3xl">
            <h1 class="font-heading text-5xl md:text-6xl lg:text-7xl font-bold text-white leading-tight mb-6">
                Integrating nature with <span class="text-emerald-400">modern architecture</span>.
            </h1>
            <p class="text-lg md:text-xl text-neutral-200 mb-10 text-balance max-w-2xl font-light leading-relaxed">
                We design, install, and maintain sophisticated green roofs and living walls that elevate sustainable building performance and aesthetic excellence.
            </p>
            <div class="flex flex-col sm:flex-row gap-4">
                <a href="portfolio.html" class="inline-flex justify-center items-center px-8 py-4 text-base font-medium text-neutral-900 bg-white hover:bg-neutral-100 rounded transition-colors shadow-lg">
                    Explore Projects
                </a>
                <a href="contact.html" class="inline-flex justify-center items-center px-8 py-4 text-base font-medium text-white border border-white/30 hover:bg-white/10 backdrop-blur-sm rounded transition-colors">
                    Request Consultation
                </a>
            </div>
        </div>
    </div>
</section>

<!-- Section 2: Sustainable Building Approach -->
<section class="py-24 bg-white dark:bg-neutral-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col lg:flex-row gap-16 items-center">
            <div class="lg:w-1/2 space-y-8">
                <h2 class="font-heading text-4xl md:text-5xl font-semibold text-neutral-900 dark:text-white leading-tight">
                    Transforming the built environment.
                </h2>
                <div class="space-y-6 text-lg text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">
                    <p>
                        Living architecture is no longer an afterthought. It is a fundamental component of high-performance buildings, providing critical thermal regulation, stormwater management, and acoustic insulation.
                    </p>
                    <p>
                        Our approach seamlessly blends structural engineering with advanced horticultural science, ensuring that every installation not only thrives but actively contributes to the building's ecosystem and lifespan.
                    </p>
                </div>
            </div>
            <div class="lg:w-1/2 w-full">
                <img src="https://images.unsplash.com/photo-1545060894-7b64f9f300c3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Sustainable modern building architecture" class="w-full h-auto object-cover rounded shadow-2xl aspect-[4/3]" />
            </div>
        </div>
    </div>
</section>

<!-- Section 3: Green Roof + Living Wall Expertise -->
<section class="py-24 bg-neutral-50 dark:bg-neutral-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col lg:flex-row gap-12 items-start mb-16">
            <div class="lg:w-1/2">
                <h2 class="font-heading text-4xl font-semibold text-neutral-900 dark:text-white mb-4">Core Expertise</h2>
                <p class="text-neutral-600 dark:text-neutral-400 text-lg font-light">Comprehensive solutions engineered for longevity and architectural integrity.</p>
            </div>
            <div class="lg:w-1/2">
                <img src="https://images.unsplash.com/photo-1599580436449-cd8b0ed3a5bf?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Living wall detail" class="w-full h-48 object-cover rounded shadow-md" />
            </div>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-16">
            <div class="flex gap-6 border-t border-neutral-200 dark:border-neutral-800 pt-8">
                <div class="text-emerald-600 dark:text-emerald-500 font-heading text-xl font-semibold">01</div>
                <div>
                    <h3 class="text-2xl font-semibold text-neutral-900 dark:text-white mb-3">Green Roof Systems</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">From lightweight extensive sedum roofs to highly engineered intensive roof gardens, we design systems tailored to load capacities and aesthetic goals.</p>
                    <img src="https://images.unsplash.com/photo-1524317112001-f09919b491fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Green roof system" class="w-full h-32 object-cover rounded mt-4 opacity-90" />
                </div>
            </div>
            <div class="flex gap-6 border-t border-neutral-200 dark:border-neutral-800 pt-8">
                <div class="text-emerald-600 dark:text-emerald-500 font-heading text-xl font-semibold">02</div>
                <div>
                    <h3 class="text-2xl font-semibold text-neutral-900 dark:text-white mb-3">Living Wall Structures</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">Vertical botanical installations for interior and exterior facades, featuring integrated automated irrigation and specialized structural mounting.</p>
                    <img src="https://images.unsplash.com/photo-1541888079001-ce151cdfa900?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Living wall installation" class="w-full h-32 object-cover rounded mt-4 opacity-90" />
                </div>
            </div>
            <div class="flex gap-6 border-t border-neutral-200 dark:border-neutral-800 pt-8">
                <div class="text-emerald-600 dark:text-emerald-500 font-heading text-xl font-semibold">03</div>
                <div>
                    <h3 class="text-2xl font-semibold text-neutral-900 dark:text-white mb-3">Structural & Waterproofing</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">Meticulous coordination with structural engineers to ensure flawless waterproofing, root barriers, and drainage layers that protect the building envelope.</p>
                </div>
            </div>
            <div class="flex gap-6 border-t border-neutral-200 dark:border-neutral-800 pt-8">
                <div class="text-emerald-600 dark:text-emerald-500 font-heading text-xl font-semibold">04</div>
                <div>
                    <h3 class="text-2xl font-semibold text-neutral-900 dark:text-white mb-3">Long-term Maintenance</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">Proactive care programs including soil testing, pruning, irrigation monitoring, and seasonal adjustments to ensure enduring vitality.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Section 4: Featured Project Story -->
<section class="py-24 bg-white dark:bg-neutral-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col lg:flex-row-reverse gap-16 items-center">
            <div class="lg:w-5/12 space-y-6">
                <div class="text-sm font-semibold tracking-wider text-emerald-600 dark:text-emerald-500 uppercase">Featured Case Study</div>
                <h2 class="font-heading text-4xl font-semibold text-neutral-900 dark:text-white">The Apex Tower Vertical Forest</h2>
                <div class="space-y-4 text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">
                    <p><strong>Location:</strong> Downtown Metropolitan District</p>
                    <p><strong>Challenge:</strong> Integrating 4,000 sq ft of living walls into a south-facing high-rise facade subjected to extreme urban heat and wind sheer.</p>
                    <p><strong>Solution:</strong> A custom modular mounting system with wind-baffling capabilities and a dual-zone sensory irrigation system utilizing captured rainwater.</p>
                    <p><strong>Outcome:</strong> Reduced ambient facade temperature by 12°C in summer, achieving LEED Platinum certification for the development.</p>
                </div>
                <div class="pt-4">
                    <a href="portfolio.html" class="inline-flex items-center gap-2 text-neutral-900 dark:text-white font-medium hover:text-emerald-600 dark:hover:text-emerald-400 transition-colors border-b border-current pb-1">
                        View Full Portfolio
                        <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                    </a>
                </div>
            </div>
            <div class="lg:w-7/12 w-full">
                <img src="https://images.unsplash.com/photo-1574621100236-d26b5275e533?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Vertical forest on a modern high-rise" class="w-full h-auto object-cover rounded shadow-lg aspect-[4/5] object-center" />
            </div>
        </div>
    </div>
</section>

<!-- Section 5: Consultation CTA -->
<section class="py-24 bg-neutral-900 text-white relative overflow-hidden">
    <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1518005020951-eccb494ad742?ixlib=rb-4.0.3&auto=format&fit=crop&w=1500&q=80" alt="CTA background" class="w-full h-full object-cover opacity-20" />
        <div class="absolute inset-0 bg-gradient-to-r from-neutral-900 via-neutral-900/90 to-neutral-900/40"></div>
    </div>
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
        <h2 class="font-heading text-4xl md:text-5xl font-semibold mb-6">Ready to build greener?</h2>
        <p class="text-xl text-neutral-400 font-light mb-10 text-balance max-w-2xl mx-auto">
            Partner with our architectural integration experts to bring sustainable living infrastructure to your next development.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <a href="contact.html" class="inline-flex justify-center items-center px-8 py-4 text-base font-medium text-white bg-emerald-600 hover:bg-emerald-700 rounded transition-colors shadow-lg">
                Request Project Consultation
            </a>
            <a href="tel:+15551234567" class="inline-flex justify-center items-center px-8 py-4 text-base font-medium text-white border border-neutral-700 hover:bg-neutral-800 rounded transition-colors">
                Call +1 (555) 123-4567
            </a>
        </div>
    </div>
</section>
"""

# ----- HOME 2 -----
home2_content = """
<!-- Section 1: Immersive Sustainability Hero -->
<section class="relative min-h-screen flex items-center pt-20">
    <div class="absolute inset-0 flex">
        <div class="w-full lg:w-1/2 bg-neutral-50 dark:bg-neutral-950"></div>
        <div class="hidden lg:block w-1/2 relative">
            <img src="https://images.unsplash.com/photo-1513694203232-719a280e022f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Architectural living wall" class="absolute inset-0 w-full h-full object-cover" />
            <div class="absolute inset-0 bg-neutral-900/20"></div>
        </div>
    </div>
    
    <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
        <div class="lg:w-1/2 lg:pr-16 py-20">
            <div class="inline-block px-3 py-1 bg-emerald-100 dark:bg-emerald-900/30 text-emerald-800 dark:text-emerald-400 text-xs font-bold tracking-widest uppercase rounded mb-6">
                Living Architecture Studio
            </div>
            <h1 class="font-heading text-5xl md:text-6xl font-bold text-neutral-900 dark:text-white leading-tight mb-8">
                Cultivating architecture for a resilient future.
            </h1>
            <p class="text-xl text-neutral-600 dark:text-neutral-400 mb-10 font-light leading-relaxed">
                Elevating commercial and residential properties through expertly engineered green roofs and vertical gardens.
            </p>
            <a href="services.html" class="inline-flex justify-center items-center px-8 py-4 text-base font-medium text-white bg-neutral-900 dark:bg-white dark:text-neutral-900 hover:bg-neutral-800 dark:hover:bg-neutral-100 rounded transition-colors shadow-lg">
                Discover Our Services
            </a>
        </div>
    </div>
</section>

<!-- Section 2: Why Living Architecture Matters -->
<section class="py-24 bg-white dark:bg-neutral-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-12 gap-12 items-center">
            <div class="md:col-span-5 flex flex-col justify-center">
                <h2 class="font-heading text-4xl font-semibold text-neutral-900 dark:text-white mb-6">The Environmental Imperative</h2>
                <div class="h-1 w-20 bg-emerald-500 mb-8"></div>
                <img src="https://images.unsplash.com/photo-1545060894-7b64f9f300c3?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Sustainability impact" class="w-full rounded shadow-lg hidden md:block" />
            </div>
            <div class="md:col-span-7 space-y-6 text-lg text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">
                <p>
                    As urban density increases, integrating plant life into structural surfaces is vital. Green infrastructure mitigates the urban heat island effect, significantly lowering ambient temperatures and reducing HVAC energy consumption by up to 20%.
                </p>
                <img src="https://images.unsplash.com/photo-1599580436449-cd8b0ed3a5bf?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Living wall detail" class="w-full rounded shadow-md my-8 md:hidden" />
                <p>
                    Beyond temperature management, our systems capture and filter stormwater, reducing municipal runoff and protecting local waterways, while simultaneously reintroducing essential biodiversity to concrete-dominated landscapes.
                </p>
                <div class="pt-6">
                    <img src="https://images.unsplash.com/photo-1518005020951-eccb494ad742?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Green roof ecosystem" class="w-full h-64 object-cover rounded shadow-lg" />
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Section 3: Installation Process -->
<section class="py-24 bg-neutral-50 dark:bg-neutral-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="font-heading text-4xl font-semibold text-neutral-900 dark:text-white mb-16 text-center">Our Methodology</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center mb-16">
            <div>
                <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Team reviewing architecture plans" class="w-full rounded shadow-lg" />
            </div>
            <div class="space-y-12 relative">
                <!-- Connective line -->
                <div class="absolute left-6 top-6 bottom-6 w-0.5 bg-emerald-200 dark:bg-emerald-900/50"></div>
                
                <div class="relative pl-16">
                    <div class="absolute left-0 top-0 w-12 h-12 rounded-full bg-white dark:bg-neutral-900 border-2 border-emerald-500 flex items-center justify-center text-emerald-600 dark:text-emerald-400 font-bold shadow-sm">1</div>
                    <h3 class="text-xl font-semibold text-neutral-900 dark:text-white mb-2">Site Assessment</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 text-sm font-light">Structural load analysis and micro-climate evaluation for optimal green roof viability.</p>
                </div>
                
                <div class="relative pl-16">
                    <div class="absolute left-0 top-0 w-12 h-12 rounded-full bg-white dark:bg-neutral-900 border-2 border-emerald-500 flex items-center justify-center text-emerald-600 dark:text-emerald-400 font-bold shadow-sm">2</div>
                    <h3 class="text-xl font-semibold text-neutral-900 dark:text-white mb-2">Design & Planning</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 text-sm font-light">System engineering, waterproofing coordination, and specialized plant curation.</p>
                </div>
                
                <div class="relative pl-16">
                    <div class="absolute left-0 top-0 w-12 h-12 rounded-full bg-white dark:bg-neutral-900 border-2 border-emerald-500 flex items-center justify-center text-emerald-600 dark:text-emerald-400 font-bold shadow-sm">3</div>
                    <h3 class="text-xl font-semibold text-neutral-900 dark:text-white mb-2">Execution & Integration</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 text-sm font-light">Precision placement of drainage layers, irrigation calibration, and botanical installation.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Section 4: Project Showcase -->
<section class="py-24 bg-white dark:bg-neutral-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="font-heading text-4xl font-semibold text-neutral-900 dark:text-white mb-16">Select Works</h2>
        
        <div class="space-y-24">
            <!-- Project 1 -->
            <div class="flex flex-col lg:flex-row gap-12 items-center">
                <div class="lg:w-2/3">
                    <img src="https://images.unsplash.com/photo-1524317112001-f09919b491fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Extensive green roof on corporate headquarters" class="w-full h-auto object-cover rounded" />
                </div>
                <div class="lg:w-1/3 space-y-4">
                    <h3 class="text-2xl font-semibold text-neutral-900 dark:text-white">Nordic Innovation Center</h3>
                    <p class="text-emerald-600 dark:text-emerald-400 text-sm font-semibold tracking-wide uppercase">Extensive Green Roof</p>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light">A 12,000 sq ft undulating green roof acting as natural insulation and public recreation space.</p>
                </div>
            </div>
            
            <!-- Project 2 -->
            <div class="flex flex-col lg:flex-row-reverse gap-12 items-center">
                <div class="lg:w-2/3">
                    <img src="https://images.unsplash.com/photo-1582298538104-fe2e74c878f1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Interior living wall in atrium" class="w-full h-auto object-cover rounded" />
                </div>
                <div class="lg:w-1/3 space-y-4">
                    <h3 class="text-2xl font-semibold text-neutral-900 dark:text-white">Meridian Atrium</h3>
                    <p class="text-emerald-600 dark:text-emerald-400 text-sm font-semibold tracking-wide uppercase">Interior Living Wall</p>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light">A five-story internal bio-filter wall utilizing hydroponic systems to purify indoor air quality.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Section 5: Build Greener CTA -->
<section class="py-32 bg-neutral-100 dark:bg-neutral-950 border-t border-neutral-200 dark:border-neutral-800 relative overflow-hidden">
    <div class="absolute inset-0 opacity-10">
        <img src="https://images.unsplash.com/photo-1541888079001-ce151cdfa900?ixlib=rb-4.0.3&auto=format&fit=crop&w=1500&q=80" alt="Abstract eco structure" class="w-full h-full object-cover" />
    </div>
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
        <h2 class="font-heading text-4xl md:text-5xl font-semibold text-neutral-900 dark:text-white mb-8">Initiate your project.</h2>
        <p class="text-xl text-neutral-600 dark:text-neutral-400 mb-12 font-light max-w-2xl mx-auto">
            Our team of horticultural architects and structural engineers are ready to discuss the specific requirements of your next development.
        </p>
        <a href="contact.html" class="inline-flex justify-center items-center px-10 py-5 text-lg font-medium text-white bg-emerald-600 hover:bg-emerald-700 rounded transition-all hover:scale-105 shadow-xl">
            Start the Conversation
        </a>
    </div>
</section>
"""

# ----- ABOUT PAGE -----
about_content = """
<!-- Section 1: About the Company -->
<section class="py-24 bg-white dark:bg-neutral-950 pt-32">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-3xl">
            <h1 class="font-heading text-5xl md:text-6xl font-bold text-neutral-900 dark:text-white mb-8 leading-tight">
                Architectural discipline meets environmental stewardship.
            </h1>
            <p class="text-xl text-neutral-600 dark:text-neutral-400 font-light leading-relaxed mb-10">
                EcoArch was founded on a singular premise: that the built environment should not merely displace nature, but actively incorporate it. We are a multidisciplinary studio of landscape architects, structural engineers, and horticulturalists dedicated to elevating urban spaces.
            </p>
        </div>
        <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80" alt="EcoArch studio team reviewing architectural plans" class="w-full h-auto object-cover rounded shadow-lg aspect-[21/9]" />
    </div>
</section>

<!-- Section 2: Our Design Philosophy -->
<section class="py-24 bg-neutral-50 dark:bg-neutral-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div>
                <h2 class="font-heading text-4xl font-semibold text-neutral-900 dark:text-white mb-6">Our Design Philosophy</h2>
                <div class="space-y-6 text-lg text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">
                    <p>
                        We approach green roofs and living walls not as decorative add-ons, but as integral building systems. Our philosophy dictates that true sustainability requires longevity—a living installation is only successful if it thrives decades after installation.
                    </p>
                    <p>
                        By combining precise structural engineering, advanced water management technology, and climate-specific botanical selection, we create resilient micro-ecosystems that enhance architectural intent.
                    </p>
                </div>
            </div>
            <div class="relative rounded overflow-hidden shadow-lg border border-neutral-200 dark:border-neutral-800 h-full min-h-[400px]">
                <img src="https://images.unsplash.com/photo-1541888079001-ce151cdfa900?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Design detail" class="absolute inset-0 w-full h-full object-cover" />
                <div class="absolute inset-0 bg-neutral-900/70 flex flex-col justify-end p-10 text-white">
                    <blockquote class="text-2xl font-heading font-medium leading-relaxed italic mb-4 text-balance">
                        "The most sophisticated building material available to modern architecture is life itself."
                    </blockquote>
                    <div class="text-emerald-400 font-semibold uppercase tracking-widest text-sm">— Elena Rostova, Principal Architect</div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Section 3: Expertise & Standards -->
<section class="py-24 bg-white dark:bg-neutral-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
            <div class="lg:col-span-5">
                <h2 class="font-heading text-4xl font-semibold text-neutral-900 dark:text-white mb-6">Uncompromising Standards</h2>
                <p class="text-xl text-neutral-600 dark:text-neutral-400 font-light mb-8">Every installation adheres to rigorous technical specifications ensuring structural safety and botanical health.</p>
                <img src="https://images.unsplash.com/photo-1518005020951-eccb494ad742?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Installation process" class="w-full rounded shadow-md hidden lg:block" />
            </div>
            
            <div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-12">
                <div class="space-y-4">
                    <h3 class="text-2xl font-semibold text-neutral-900 dark:text-white border-b border-emerald-500 pb-2 inline-block">Structural Assessment</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">Comprehensive dead and live load calculations for saturated media and mature plant weight, ensuring perfect integration with the building's structural capacity.</p>
                </div>
                <div class="space-y-4">
                    <h3 class="text-2xl font-semibold text-neutral-900 dark:text-white border-b border-emerald-500 pb-2 inline-block">Waterproofing Integration</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">We utilize monolithic, seamless membrane systems with integrated root barriers, independently leak-tested prior to any system installation.</p>
                </div>
                <div class="space-y-4">
                    <h3 class="text-2xl font-semibold text-neutral-900 dark:text-white border-b border-emerald-500 pb-2 inline-block">Advanced Irrigation</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">Smart, weather-responsive fertigation systems that precisely deliver water and nutrients, significantly reducing waste while maximizing plant vitality.</p>
                </div>
                <div class="space-y-4">
                    <h3 class="text-2xl font-semibold text-neutral-900 dark:text-white border-b border-emerald-500 pb-2 inline-block">Engineered Growing Media</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">Custom-blended lightweight substrates formulated for specific wind uplift resistance, water retention capabilities, and nutrient delivery.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Section 4: Sustainability Commitment -->
<section class="py-24 bg-emerald-900 text-white relative">
    <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1545060894-7b64f9f300c3?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80" alt="Eco architecture" class="w-full h-full object-cover opacity-20" />
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
            <div class="lg:col-span-5">
                <h2 class="font-heading text-4xl md:text-5xl font-semibold mb-6">Our Commitment to the Future</h2>
            </div>
            <div class="lg:col-span-7 space-y-6 text-lg text-emerald-100 font-light leading-relaxed">
                <p>
                    Beyond the installations we create, EcoArch operates with a profound commitment to environmental responsibility. We source 80% of our plants from nurseries within a 100-mile radius of the project site to reduce transport emissions and ensure regional hardiness.
                </p>
                <p>
                    Our mounting systems utilize recycled aluminum and plastics, and we continually research methods to capture and utilize greywater for all our irrigation systems, pushing the boundaries of what sustainable architecture can achieve.
                </p>
            </div>
        </div>
    </div>
</section>
"""

# ----- SERVICES PAGE -----
services_content = """
<!-- Section 1: Services Introduction -->
<section class="py-32 bg-neutral-100 dark:bg-neutral-900 relative">
    <div class="absolute top-0 right-0 h-full w-1/3 opacity-30 dark:opacity-20 hidden lg:block">
        <img src="https://images.unsplash.com/photo-1518005020951-eccb494ad742?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover rounded-l-full" alt="Leaves background" />
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
        <h1 class="font-heading text-5xl md:text-6xl font-bold text-neutral-900 dark:text-white mb-6">Capabilities</h1>
        <p class="text-xl text-neutral-600 dark:text-neutral-400 max-w-3xl mx-auto font-light leading-relaxed">
            From expansive ecological roofs to intricate interior bio-walls, we deliver end-to-end engineering, installation, and care.
        </p>
    </div>
</section>

<!-- Section 2: Green Roof Systems -->
<section class="py-24 bg-white dark:bg-neutral-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-start">
            <div class="sticky top-28 space-y-6">
                <img src="https://images.unsplash.com/photo-1541888079001-ce151cdfa900?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Extensive green roof installation" class="w-full rounded shadow-xl" />
                <img src="https://images.unsplash.com/photo-1524317112001-f09919b491fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Sedum green roof close up" class="w-full h-48 object-cover rounded shadow-md hidden lg:block" />
            </div>
            <div class="space-y-12">
                <div>
                    <h2 class="font-heading text-4xl font-semibold text-neutral-900 dark:text-white mb-4">Green Roof Systems</h2>
                    <p class="text-lg text-neutral-600 dark:text-neutral-400 font-light">Transforming unused space into performing ecological assets.</p>
                </div>
                
                <div class="space-y-8">
                    <div>
                        <h3 class="text-xl font-semibold text-neutral-900 dark:text-white mb-2">Extensive Systems</h3>
                        <p class="text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">Lightweight, low-maintenance roofs featuring shallow growing media (3-6 inches). Ideal for large commercial spaces seeking stormwater management and thermal regulation with minimal structural reinforcement. Planted with hardy sedums and drought-tolerant grasses.</p>
                    </div>
                    <div>
                        <h3 class="text-xl font-semibold text-neutral-900 dark:text-white mb-2">Intensive Roof Gardens</h3>
                        <p class="text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">Accessible park-like environments requiring deeper soil (8+ inches). These robust systems support diverse plant life, including shrubs and small trees, creating high-value amenity spaces for residential and commercial developments.</p>
                    </div>
                    <div>
                        <h3 class="text-xl font-semibold text-neutral-900 dark:text-white mb-2">Technical Integration</h3>
                        <ul class="list-disc list-inside text-neutral-600 dark:text-neutral-400 font-light space-y-2 mt-2">
                            <li>Multi-layer drainage and water retention boards</li>
                            <li>High-performance root barrier installation</li>
                            <li>Engineered wind-uplift mitigation systems</li>
                            <li>Parapet and penetration detailing</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Section 3: Living Wall Systems -->
<section class="py-24 bg-neutral-50 dark:bg-neutral-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-start">
            <div class="order-2 lg:order-1 space-y-12">
                <div>
                    <h2 class="font-heading text-4xl font-semibold text-neutral-900 dark:text-white mb-4">Living Wall Systems</h2>
                    <p class="text-lg text-neutral-600 dark:text-neutral-400 font-light">Vertical flora integration for striking aesthetic and environmental impact.</p>
                </div>
                
                <div class="space-y-8">
                    <div>
                        <h3 class="text-xl font-semibold text-neutral-900 dark:text-white mb-2">Exterior Facades</h3>
                        <p class="text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">Engineered to withstand wind sheer, extreme temperatures, and UV exposure. Our exterior systems protect building envelopes while dramatically improving local air quality and urban biodiversity.</p>
                    </div>
                    <div>
                        <h3 class="text-xl font-semibold text-neutral-900 dark:text-white mb-2">Interior Bio-Walls</h3>
                        <p class="text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">Designed for lobbies, atriums, and offices. These systems utilize specialized indoor botanicals and integrated lighting to purify air (phytoremediation) and boost occupant wellbeing and productivity.</p>
                    </div>
                    <div>
                        <h3 class="text-xl font-semibold text-neutral-900 dark:text-white mb-2">System Architecture</h3>
                        <ul class="list-disc list-inside text-neutral-600 dark:text-neutral-400 font-light space-y-2 mt-2">
                            <li>Hydroponic or soil-based modular panel options</li>
                            <li>Automated, remotely-monitored fertigation zones</li>
                            <li>Custom structural framework and drip trays</li>
                            <li>Integrated horticultural lighting design</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="order-1 lg:order-2 sticky top-28 space-y-6">
                <img src="https://images.unsplash.com/photo-1599580436449-cd8b0ed3a5bf?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Large scale living wall installation" class="w-full rounded shadow-xl" />
                <img src="https://images.unsplash.com/photo-1582298538104-fe2e74c878f1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Interior living wall" class="w-full h-48 object-cover rounded shadow-md hidden lg:block" />
            </div>
        </div>
    </div>
</section>

<!-- Section 4: Maintenance & Long-Term Care -->
<section class="py-24 bg-white dark:bg-neutral-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-3xl mx-auto text-center mb-16">
            <h2 class="font-heading text-4xl font-semibold text-neutral-900 dark:text-white mb-6">Long-Term Stewardship</h2>
            <p class="text-lg text-neutral-600 dark:text-neutral-400 font-light">A living system is dynamic. We provide comprehensive preventative care programs to ensure the architectural intent matures beautifully over decades.</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
            <div class="relative overflow-hidden rounded group border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900">
                <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Horticulture care" class="w-full h-48 object-cover transition-transform duration-500 group-hover:scale-105" />
                <div class="p-8">
                    <h3 class="text-xl font-semibold text-neutral-900 dark:text-white mb-4">Horticultural Care</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light text-sm leading-relaxed">Scheduled pruning, weed abatement, pest management, and seasonal plant replacements to maintain intended design patterns.</p>
                </div>
            </div>
            
            <div class="relative overflow-hidden rounded group border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900">
                <img src="https://images.unsplash.com/photo-1545060894-7b64f9f300c3?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="System Diagnostics" class="w-full h-48 object-cover transition-transform duration-500 group-hover:scale-105" />
                <div class="p-8">
                    <h3 class="text-xl font-semibold text-neutral-900 dark:text-white mb-4">System Diagnostics</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light text-sm leading-relaxed">Rigorous testing of irrigation sensors, valve operations, structural mount integrity, and drainage flow capacity.</p>
                </div>
            </div>
            
            <div class="relative overflow-hidden rounded group border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900">
                <img src="https://images.unsplash.com/photo-1513694203232-719a280e022f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Soil Analysis" class="w-full h-48 object-cover transition-transform duration-500 group-hover:scale-105" />
                <div class="p-8">
                    <h3 class="text-xl font-semibold text-neutral-900 dark:text-white mb-4">Soil & Water Analysis</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light text-sm leading-relaxed">Bi-annual laboratory testing of media pH and nutrient levels to adjust fertigation dosing for optimal plant resilience.</p>
                </div>
            </div>
        </div>
        
        <div class="text-center">
            <a href="contact.html" class="inline-flex justify-center items-center px-8 py-4 text-base font-medium text-white bg-neutral-900 dark:bg-emerald-600 hover:bg-neutral-800 dark:hover:bg-emerald-500 rounded transition-colors shadow-sm">
                Discuss a Maintenance Plan
            </a>
        </div>
    </div>
</section>
"""

# ----- PORTFOLIO PAGE -----
portfolio_content = """
<!-- Section 1: Portfolio Introduction -->
<section class="pt-32 pb-16 bg-white dark:bg-neutral-950 border-b border-neutral-200 dark:border-neutral-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 class="font-heading text-5xl md:text-6xl font-bold text-neutral-900 dark:text-white mb-6">Selected Works</h1>
        <p class="text-xl text-neutral-600 dark:text-neutral-400 max-w-2xl font-light">
            An archive of our structural landscape integration across commercial, residential, and civic architecture.
        </p>
    </div>
</section>

<!-- Section 2: Featured Architectural Projects -->
<section class="py-24 bg-neutral-50 dark:bg-neutral-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-24">
        
        <!-- Gallery Item 1 -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            <div class="lg:col-span-8 group relative overflow-hidden rounded">
                <img src="https://images.unsplash.com/photo-1518005020951-eccb494ad742?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Tech campus green roof" class="w-full h-auto object-cover transform group-hover:scale-105 transition-transform duration-700 aspect-[16/10]" />
            </div>
            <div class="lg:col-span-4 lg:pl-8 space-y-4">
                <div class="text-sm tracking-widest text-emerald-600 dark:text-emerald-400 uppercase font-semibold">Corporate Campus</div>
                <h2 class="font-heading text-3xl font-semibold text-neutral-900 dark:text-white">Silicon Valley HQ</h2>
                <p class="text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">A 20,000 sq ft intensive green roof serving as a primary recreation space for employees, featuring native grasses and mature olive trees.</p>
            </div>
        </div>
        
        <!-- Gallery Item 2 -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            <div class="lg:col-span-4 lg:pr-8 space-y-4 order-2 lg:order-1 text-right lg:text-left">
                <div class="text-sm tracking-widest text-emerald-600 dark:text-emerald-400 uppercase font-semibold">Civic Center</div>
                <h2 class="font-heading text-3xl font-semibold text-neutral-900 dark:text-white">Metropolitan Library</h2>
                <p class="text-neutral-600 dark:text-neutral-400 font-light leading-relaxed">A striking geometric exterior living wall that acts as a natural cooling system for the glass-facade reading rooms within.</p>
            </div>
            <div class="lg:col-span-8 group relative overflow-hidden rounded order-1 lg:order-2">
                <img src="https://images.unsplash.com/photo-1541888079001-ce151cdfa900?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Metropolitan library living wall" class="w-full h-auto object-cover transform group-hover:scale-105 transition-transform duration-700 aspect-[16/10]" />
            </div>
        </div>
        
    </div>
</section>

<!-- Section 3: Project Case Study -->
<section class="py-24 bg-white dark:bg-neutral-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-3xl mb-16">
            <div class="text-sm font-semibold tracking-wider text-neutral-500 dark:text-neutral-400 uppercase mb-4">Deep Dive</div>
            <h2 class="font-heading text-4xl font-semibold text-neutral-900 dark:text-white mb-6">The Obsidian Residences</h2>
            <p class="text-xl text-neutral-600 dark:text-neutral-400 font-light">Integrating high-altitude living architecture into luxury mountain residential design.</p>
        </div>
        
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-12 mb-12">
            <div class="col-span-1 lg:col-span-2">
                <img src="https://images.unsplash.com/photo-1600607688969-a5bfcd646154?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Mountain residence green roof" class="w-full h-full object-cover rounded" />
            </div>
            <div class="col-span-1 space-y-8 bg-neutral-50 dark:bg-neutral-900 p-8 rounded">
                <div>
                    <h4 class="text-sm font-semibold text-neutral-900 dark:text-white uppercase mb-1">Project Type</h4>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light">Intensive Green Roof & Terraces</p>
                </div>
                <div>
                    <h4 class="text-sm font-semibold text-neutral-900 dark:text-white uppercase mb-1">Challenge</h4>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light text-sm">Designing a system capable of surviving extreme freeze-thaw cycles and heavy snow loads while maintaining aesthetic appeal.</p>
                </div>
                <div>
                    <h4 class="text-sm font-semibold text-neutral-900 dark:text-white uppercase mb-1">Approach</h4>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light text-sm">Implementation of specialized heated drainage layers and alpine-specific botanical selection resilient to zone 4 climates.</p>
                </div>
                <div>
                    <h4 class="text-sm font-semibold text-neutral-900 dark:text-white uppercase mb-1">Outcome</h4>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light text-sm">A seamless visual transition from the built structure to the surrounding mountain landscape, with zero membrane failures over 5 years.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Section 4: Project Enquiry CTA -->
<section class="py-24 bg-emerald-900 text-white text-center relative overflow-hidden">
    <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1545060894-7b64f9f300c3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1500&q=80" alt="Abstract building" class="w-full h-full object-cover opacity-20 mix-blend-overlay" />
    </div>
    <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <h2 class="font-heading text-4xl font-semibold mb-6">Envisioning your space?</h2>
        <p class="text-xl text-emerald-100 mb-10 font-light">
            Contact our design team to discuss feasibility, structural requirements, and aesthetic possibilities for your property.
        </p>
        <a href="contact.html" class="inline-flex justify-center items-center px-8 py-4 text-base font-medium text-emerald-900 bg-white hover:bg-neutral-100 rounded transition-colors shadow-lg">
            Start a Project Enquiry
        </a>
    </div>
</section>
"""

# ----- BLOG PAGE -----
blog_content = """
<!-- Section 1: Blog Hero -->
<section class="pt-32 pb-16 bg-white dark:bg-neutral-950 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="font-heading text-5xl md:text-6xl font-bold text-neutral-900 dark:text-white mb-6">Journal</h1>
        <p class="text-xl text-neutral-600 dark:text-neutral-400 max-w-2xl mx-auto font-light">
            Insights on sustainable architecture, botanical engineering, and the future of living buildings.
        </p>
    </div>
</section>

<!-- Section 2: Featured Article -->
<section class="py-12 bg-white dark:bg-neutral-950 border-b border-neutral-200 dark:border-neutral-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="group cursor-pointer">
            <div class="relative overflow-hidden rounded mb-8">
                <img src="https://images.unsplash.com/photo-1524317112001-f09919b491fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80" alt="Future of urban biodiversity" class="w-full h-auto object-cover transform group-hover:scale-105 transition-transform duration-700 aspect-[21/9]" />
                <div class="absolute top-6 left-6 bg-white dark:bg-neutral-900 text-neutral-900 dark:text-white text-xs font-bold uppercase tracking-widest px-3 py-1 rounded shadow">
                    Featured
                </div>
            </div>
            <div class="max-w-3xl mx-auto text-center">
                <div class="text-sm font-medium text-emerald-600 dark:text-emerald-400 mb-3">Urban Biodiversity</div>
                <h2 class="font-heading text-4xl font-semibold text-neutral-900 dark:text-white mb-4 group-hover:text-emerald-600 transition-colors">Rewilding the Skyline: The Impact of High-Altitude Habitats</h2>
                <p class="text-neutral-600 dark:text-neutral-400 font-light text-lg mb-6">An analysis of how interconnected green roofs are creating crucial pollinator corridors across concrete-dense metropolitan districts.</p>
                <span class="inline-flex items-center text-sm font-semibold text-neutral-900 dark:text-white border-b border-current pb-1">
                    Read Article
                </span>
            </div>
        </div>
    </div>
</section>

<!-- Section 3: Latest Insights -->
<section class="py-24 bg-neutral-50 dark:bg-neutral-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="font-heading text-3xl font-semibold text-neutral-900 dark:text-white mb-12">Latest Insights</h2>
        
        <div class="flex flex-col gap-12">
            <!-- Article Item -->
            <article class="grid grid-cols-1 md:grid-cols-4 gap-8 items-start border-b border-neutral-200 dark:border-neutral-800 pb-12 group cursor-pointer">
                <div class="md:col-span-1 overflow-hidden rounded">
                    <img src="https://images.unsplash.com/photo-1599580436449-cd8b0ed3a5bf?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Living wall maintenance" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-500 aspect-square md:aspect-[4/3]" />
                </div>
                <div class="md:col-span-3">
                    <div class="text-sm font-medium text-emerald-600 dark:text-emerald-400 mb-2">Technical Guide</div>
                    <h3 class="font-heading text-2xl font-semibold text-neutral-900 dark:text-white mb-3 group-hover:text-emerald-600 transition-colors">Winterizing Exterior Living Walls</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light mb-4 max-w-2xl">Essential maintenance protocols for ensuring the survival and swift spring recovery of vertical botanical systems in freezing climates.</p>
                    <span class="text-sm text-neutral-500 dark:text-neutral-500">October 12, 2026 • 5 min read</span>
                </div>
            </article>
            
            <!-- Article Item -->
            <article class="grid grid-cols-1 md:grid-cols-4 gap-8 items-start border-b border-neutral-200 dark:border-neutral-800 pb-12 group cursor-pointer">
                <div class="md:col-span-1 overflow-hidden rounded">
                    <img src="https://images.unsplash.com/photo-1518005020951-eccb494ad742?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Cooling strategies" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-500 aspect-square md:aspect-[4/3]" />
                </div>
                <div class="md:col-span-3">
                    <div class="text-sm font-medium text-emerald-600 dark:text-emerald-400 mb-2">Sustainable Architecture</div>
                    <h3 class="font-heading text-2xl font-semibold text-neutral-900 dark:text-white mb-3 group-hover:text-emerald-600 transition-colors">Quantifying Thermal Reduction</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light mb-4 max-w-2xl">A case study examining the direct ROI of green roofs through decreased HVAC dependency in commercial structures.</p>
                    <span class="text-sm text-neutral-500 dark:text-neutral-500">September 28, 2026 • 8 min read</span>
                </div>
            </article>

            <!-- Article Item -->
            <article class="grid grid-cols-1 md:grid-cols-4 gap-8 items-start group cursor-pointer">
                <div class="md:col-span-1 overflow-hidden rounded">
                    <img src="https://images.unsplash.com/photo-1545060894-7b64f9f300c3?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Plant selection" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-500 aspect-square md:aspect-[4/3]" />
                </div>
                <div class="md:col-span-3">
                    <div class="text-sm font-medium text-emerald-600 dark:text-emerald-400 mb-2">Horticulture</div>
                    <h3 class="font-heading text-2xl font-semibold text-neutral-900 dark:text-white mb-3 group-hover:text-emerald-600 transition-colors">Selecting Wind-Resistant Species</h3>
                    <p class="text-neutral-600 dark:text-neutral-400 font-light mb-4 max-w-2xl">Navigating the challenges of high-floor exterior installations and the botanical species proven to withstand severe wind uplift.</p>
                    <span class="text-sm text-neutral-500 dark:text-neutral-500">September 15, 2026 • 6 min read</span>
                </div>
            </article>
        </div>
    </div>
</section>

<!-- Section 4: Sustainability Newsletter / CTA -->
<section class="py-24 bg-neutral-900 text-white relative overflow-hidden">
    <div class="absolute -right-48 -bottom-48 opacity-10 pointer-events-none">
        <svg width="400" height="400" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2L2 22h20L12 2zm0 4.5l6.5 13h-13L12 6.5z"/>
        </svg>
    </div>
    <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
        <h2 class="font-heading text-3xl md:text-4xl font-semibold mb-4">Stay informed on living architecture.</h2>
        <p class="text-neutral-400 font-light mb-8">Subscribe to receive our quarterly journal covering innovations in green building infrastructure.</p>
        
        <form class="flex flex-col sm:flex-row gap-4 max-w-lg mx-auto" onsubmit="event.preventDefault(); alert('Subscribed!');">
            <input type="email" placeholder="Email Address" required class="flex-grow px-4 py-3 bg-neutral-800 border border-neutral-700 rounded text-white focus:outline-none focus:border-emerald-500 transition-colors" />
            <button type="submit" class="px-6 py-3 bg-white text-neutral-900 font-medium rounded hover:bg-neutral-200 transition-colors whitespace-nowrap">
                Subscribe
            </button>
        </form>
    </div>
</section>
"""

# ----- CONTACT PAGE -----
contact_content = """
<!-- Section 1: Contact Hero -->
<section class="relative pt-32 pb-24 bg-neutral-100 dark:bg-neutral-900 overflow-hidden">
    <div class="absolute right-0 top-0 w-1/3 h-full hidden lg:block opacity-30 dark:opacity-20 pointer-events-none">
        <img src="https://images.unsplash.com/photo-1541888079001-ce151cdfa900?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="w-full h-full object-cover rounded-l-full" alt="Abstract leaf architecture" />
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <h1 class="font-heading text-5xl md:text-6xl font-bold text-neutral-900 dark:text-white mb-6">Let's discuss your project.</h1>
        <p class="text-xl text-neutral-600 dark:text-neutral-400 max-w-2xl font-light">
            Whether you are in the early architectural planning phase or seeking an retrofit solution, our team is ready to consult.
        </p>
    </div>
</section>

<!-- Section 2 & 3: Split Form & Details -->
<section class="py-24 bg-white dark:bg-neutral-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col lg:flex-row gap-16">
            
            <!-- Section 2: Enquiry Form -->
            <div class="lg:w-2/3">
                <h2 class="font-heading text-3xl font-semibold text-neutral-900 dark:text-white mb-8">Project Enquiry</h2>
                <form id="contact-form" class="space-y-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <label for="name" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">Full Name *</label>
                            <input type="text" id="name" required class="w-full px-4 py-3 bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 rounded focus:ring-2 focus:ring-emerald-500 focus:border-transparent outline-none transition-all dark:text-white" />
                        </div>
                        <div>
                            <label for="email" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">Email Address *</label>
                            <input type="email" id="email" required class="w-full px-4 py-3 bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 rounded focus:ring-2 focus:ring-emerald-500 focus:border-transparent outline-none transition-all dark:text-white" />
                        </div>
                    </div>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <label for="phone" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">Phone Number</label>
                            <input type="tel" id="phone" class="w-full px-4 py-3 bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 rounded focus:ring-2 focus:ring-emerald-500 focus:border-transparent outline-none transition-all dark:text-white" />
                        </div>
                        <div>
                            <label for="project-type" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">Project Type *</label>
                            <select id="project-type" required class="w-full px-4 py-3 bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 rounded focus:ring-2 focus:ring-emerald-500 focus:border-transparent outline-none transition-all dark:text-white appearance-none">
                                <option value="">Select a type...</option>
                                <option value="green-roof">Green Roof</option>
                                <option value="living-wall">Living Wall</option>
                                <option value="maintenance">Maintenance</option>
                                <option value="consultation">Consultation</option>
                            </select>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <label for="property-type" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">Property Type</label>
                            <select id="property-type" class="w-full px-4 py-3 bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 rounded focus:ring-2 focus:ring-emerald-500 focus:border-transparent outline-none transition-all dark:text-white appearance-none">
                                <option value="">Select...</option>
                                <option value="commercial">Commercial</option>
                                <option value="residential">Residential</option>
                                <option value="civic">Civic / Public</option>
                            </select>
                        </div>
                        <div>
                            <label for="location" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">Project Location</label>
                            <input type="text" id="location" placeholder="City, State" class="w-full px-4 py-3 bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 rounded focus:ring-2 focus:ring-emerald-500 focus:border-transparent outline-none transition-all dark:text-white" />
                        </div>
                    </div>

                    <div>
                        <label for="message" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">Project Details *</label>
                        <textarea id="message" rows="5" required placeholder="Please provide brief details about your objectives, estimated size, and timeline." class="w-full px-4 py-3 bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 rounded focus:ring-2 focus:ring-emerald-500 focus:border-transparent outline-none transition-all dark:text-white resize-y"></textarea>
                    </div>
                    
                    <button type="submit" class="px-8 py-4 bg-neutral-900 dark:bg-emerald-600 text-white font-medium rounded hover:bg-neutral-800 dark:hover:bg-emerald-500 transition-colors w-full md:w-auto">
                        Submit Enquiry
                    </button>
                </form>
            </div>

            <!-- Section 3: Contact Info -->
            <div class="lg:w-1/3 space-y-12 border-t lg:border-t-0 lg:border-l border-neutral-200 dark:border-neutral-800 pt-12 lg:pt-0 lg:pl-12">
                <div>
                    <h3 class="font-heading text-2xl font-semibold text-neutral-900 dark:text-white mb-6">Studio Office</h3>
                    <div class="space-y-4 text-neutral-600 dark:text-neutral-400 font-light">
                        <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Office building" class="w-full h-32 object-cover rounded mb-4" />
                        <p>
                            <strong>EcoArch Living Architecture</strong><br>
                            450 Architecture Blvd, Suite 200<br>
                            Design District, NY 10012
                        </p>
                    </div>
                </div>

                <div>
                    <h3 class="font-heading text-2xl font-semibold text-neutral-900 dark:text-white mb-6">Direct Contact</h3>
                    <div class="space-y-4 text-neutral-600 dark:text-neutral-400 font-light">
                        <p class="flex items-center gap-3">
                            <svg class="w-5 h-5 text-emerald-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                            <a href="tel:+15551234567" class="hover:text-emerald-600 transition-colors">+1 (555) 123-4567</a>
                        </p>
                        <p class="flex items-center gap-3">
                            <svg class="w-5 h-5 text-emerald-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                            <a href="mailto:hello@ecoarch.com" class="hover:text-emerald-600 transition-colors">hello@ecoarch.com</a>
                        </p>
                    </div>
                </div>
                
                <div>
                    <h3 class="font-heading text-2xl font-semibold text-neutral-900 dark:text-white mb-6">Working Hours</h3>
                    <div class="space-y-2 text-neutral-600 dark:text-neutral-400 font-light">
                        <p class="flex justify-between"><span>Monday - Friday</span> <span>9:00 AM - 6:00 PM</span></p>
                        <p class="flex justify-between"><span>Saturday</span> <span>By appointment</span></p>
                        <p class="flex justify-between"><span>Sunday</span> <span>Closed</span></p>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</section>

<!-- Section 4: Location Map -->
<section class="h-96 w-full bg-neutral-200 dark:bg-neutral-800">
    <!-- Responsive map container, hidden scrollbars, no overflow -->
    <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1m2!1s0x89c2598f988156a9%3A0xd54629bdf9d61d68!2sDesign%20District!5e0!3m2!1sen!2sus!4v1700000000000!5m2!1sen!2sus" 
        class="w-full h-full border-0" 
        allowfullscreen="" 
        loading="lazy" 
        referrerpolicy="no-referrer-when-downgrade"
        title="EcoArch Office Location">
    </iframe>
</section>
"""

# ----- LOGIN PAGE -----
login_content = """
<div class="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-white dark:bg-neutral-950 relative">
    <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1541888079001-ce151cdfa900?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80" alt="Login background" class="w-full h-full object-cover opacity-20" />
    </div>
    <div class="max-w-md w-full space-y-8 p-10 border border-neutral-200 dark:border-neutral-800 rounded bg-neutral-50 dark:bg-neutral-900 shadow-sm relative z-10">
        <div>
            <div class="flex justify-center">
                <a href="index.html" class="flex-shrink-0 flex items-center gap-2 group">
                    <svg class="h-10 w-10 text-emerald-700 dark:text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
                    </svg>
                    <span class="font-heading font-bold text-3xl tracking-tight text-neutral-900 dark:text-white">EcoArch</span>
                </a>
            </div>
            <h2 class="mt-8 text-center text-2xl font-semibold text-neutral-900 dark:text-white">Sign in to Client Portal</h2>
        </div>
        <form class="mt-8 space-y-6" id="auth-form">
            <div class="space-y-4">
                <div>
                    <label for="email-address" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">Email address</label>
                    <input id="email-address" name="email" type="email" autocomplete="email" required class="appearance-none relative block w-full px-4 py-3 border border-neutral-300 dark:border-neutral-700 placeholder-neutral-500 text-neutral-900 dark:text-white bg-white dark:bg-neutral-950 rounded focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm transition-colors" placeholder="Email address">
                </div>
                <div>
                    <label for="password" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">Password</label>
                    <input id="password" name="password" type="password" autocomplete="current-password" required class="appearance-none relative block w-full px-4 py-3 border border-neutral-300 dark:border-neutral-700 placeholder-neutral-500 text-neutral-900 dark:text-white bg-white dark:bg-neutral-950 rounded focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm transition-colors" placeholder="Password">
                </div>
            </div>

            <div class="flex items-center justify-between">
                <div class="flex items-center">
                    <input id="remember-me" name="remember-me" type="checkbox" class="h-4 w-4 text-emerald-600 focus:ring-emerald-500 border-neutral-300 rounded cursor-pointer">
                    <label for="remember-me" class="ml-2 block text-sm text-neutral-700 dark:text-neutral-300 cursor-pointer">
                        Remember me
                    </label>
                </div>

                <div class="text-sm">
                    <a href="#" class="font-medium text-emerald-600 hover:text-emerald-500 dark:text-emerald-400 dark:hover:text-emerald-300 transition-colors">
                        Forgot password?
                    </a>
                </div>
            </div>

            <div>
                <button type="submit" class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded text-white bg-neutral-900 hover:bg-neutral-800 dark:bg-emerald-600 dark:hover:bg-emerald-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500 transition-colors">
                    Sign in
                </button>
            </div>
            
            <div class="text-center text-sm text-neutral-600 dark:text-neutral-400 mt-4">
                Don't have an account? <a href="signup.html" class="font-medium text-emerald-600 hover:text-emerald-500 dark:text-emerald-400 transition-colors">Create one</a>
            </div>
        </form>
    </div>
</div>
"""

# ----- SIGNUP PAGE -----
signup_content = """
<div class="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-white dark:bg-neutral-950 relative">
    <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1541888079001-ce151cdfa900?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80" alt="Signup background" class="w-full h-full object-cover opacity-20" />
    </div>
    <div class="max-w-md w-full space-y-8 p-10 border border-neutral-200 dark:border-neutral-800 rounded bg-neutral-50 dark:bg-neutral-900 shadow-sm relative z-10">
        <div>
            <div class="flex justify-center">
                <a href="index.html" class="flex-shrink-0 flex items-center gap-2 group">
                    <svg class="h-10 w-10 text-emerald-700 dark:text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
                    </svg>
                    <span class="font-heading font-bold text-3xl tracking-tight text-neutral-900 dark:text-white">EcoArch</span>
                </a>
            </div>
            <h2 class="mt-8 text-center text-2xl font-semibold text-neutral-900 dark:text-white">Create an Account</h2>
        </div>
        <form class="mt-8 space-y-5" id="auth-form">
            <div>
                <label for="full-name" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">Full Name</label>
                <input id="full-name" name="name" type="text" required class="appearance-none block w-full px-4 py-3 border border-neutral-300 dark:border-neutral-700 text-neutral-900 dark:text-white bg-white dark:bg-neutral-950 rounded focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm transition-colors" placeholder="Full Name">
            </div>
            
            <div>
                <label for="email-address" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">Email address</label>
                <input id="email-address" name="email" type="email" autocomplete="email" required class="appearance-none block w-full px-4 py-3 border border-neutral-300 dark:border-neutral-700 text-neutral-900 dark:text-white bg-white dark:bg-neutral-950 rounded focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm transition-colors" placeholder="Email address">
            </div>
            
            <div>
                <label for="phone" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">Phone Number</label>
                <input id="phone" name="phone" type="tel" required class="appearance-none block w-full px-4 py-3 border border-neutral-300 dark:border-neutral-700 text-neutral-900 dark:text-white bg-white dark:bg-neutral-950 rounded focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm transition-colors" placeholder="Phone Number">
            </div>
            
            <div>
                <label for="password" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">Password</label>
                <input id="password" name="password" type="password" required class="appearance-none block w-full px-4 py-3 border border-neutral-300 dark:border-neutral-700 text-neutral-900 dark:text-white bg-white dark:bg-neutral-950 rounded focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm transition-colors" placeholder="Password">
            </div>
            
            <div>
                <label for="confirm-password" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">Confirm Password</label>
                <input id="confirm-password" name="confirm-password" type="password" required class="appearance-none block w-full px-4 py-3 border border-neutral-300 dark:border-neutral-700 text-neutral-900 dark:text-white bg-white dark:bg-neutral-950 rounded focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm transition-colors" placeholder="Confirm Password">
            </div>

            <div class="flex items-center">
                <input id="terms" name="terms" type="checkbox" required class="h-4 w-4 text-emerald-600 focus:ring-emerald-500 border-neutral-300 rounded cursor-pointer">
                <label for="terms" class="ml-2 block text-sm text-neutral-700 dark:text-neutral-300 cursor-pointer">
                    I agree to the <a href="#" class="text-emerald-600 hover:text-emerald-500">Terms and Conditions</a>
                </label>
            </div>

            <div>
                <button type="submit" class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded text-white bg-neutral-900 hover:bg-neutral-800 dark:bg-emerald-600 dark:hover:bg-emerald-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500 transition-colors">
                    Create Account
                </button>
            </div>
            
            <div class="text-center text-sm text-neutral-600 dark:text-neutral-400 mt-4">
                Already have an account? <a href="login.html" class="font-medium text-emerald-600 hover:text-emerald-500 dark:text-emerald-400 transition-colors">Sign in</a>
            </div>
        </form>
    </div>
</div>
"""

# Write files
create_file(os.path.join(base_dir, 'index.html'), generate_page('Home', home1_content))
create_file(os.path.join(base_dir, 'home2.html'), generate_page('Home Alternative', home2_content))
create_file(os.path.join(base_dir, 'about.html'), generate_page('About Us', about_content))
create_file(os.path.join(base_dir, 'services.html'), generate_page('Services', services_content))
create_file(os.path.join(base_dir, 'portfolio.html'), generate_page('Portfolio', portfolio_content))
create_file(os.path.join(base_dir, 'blog.html'), generate_page('Blog Insights', blog_content))
create_file(os.path.join(base_dir, 'contact.html'), generate_page('Contact', contact_content))

# No header/footer for auth pages
create_file(os.path.join(base_dir, 'login.html'), generate_page('Client Portal Login', login_content, False))
create_file(os.path.join(base_dir, 'signup.html'), generate_page('Create Account', signup_content, False))

print("Website generated successfully with additional images.")
