var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

// Change the icons inside the button based on previous settings
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    themeToggleLightIcon.classList.remove('hidden');
} else {
    themeToggleDarkIcon.classList.remove('hidden');
}

var themeToggleBtn = document.getElementById('theme-toggle');

// Aplica dark + scheme-* em sincronia. scheme-* (Tailwind 4) faz controles
// nativos do UA (scrollbar, campos, popovers) acompanharem o tema.
function applyDarkMode(isDark) {
    var root = document.documentElement;
    if (isDark) {
        root.classList.add('dark');
        root.classList.add('scheme-dark');
        root.classList.remove('scheme-light');
    } else {
        root.classList.remove('dark');
        root.classList.add('scheme-light');
        root.classList.remove('scheme-dark');
    }
}

themeToggleBtn.addEventListener('click', function() {

    // toggle icons inside button
    themeToggleDarkIcon.classList.toggle('hidden');
    themeToggleLightIcon.classList.toggle('hidden');

    // if set via local storage previously
    if (localStorage.getItem('color-theme')) {
        if (localStorage.getItem('color-theme') === 'light') {
            applyDarkMode(true);
            localStorage.setItem('color-theme', 'dark');
        } else {
            applyDarkMode(false);
            localStorage.setItem('color-theme', 'light');
        }

    // if NOT set via local storage previously
    } else {
        if (document.documentElement.classList.contains('dark')) {
            applyDarkMode(false);
            localStorage.setItem('color-theme', 'light');
        } else {
            applyDarkMode(true);
            localStorage.setItem('color-theme', 'dark');
        }
    }

});