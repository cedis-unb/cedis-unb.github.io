(() => {
  // <stdin>
  var themeToggleDarkIcon = document.getElementById("theme-toggle-dark-icon");
  var themeToggleLightIcon = document.getElementById("theme-toggle-light-icon");
  if (localStorage.getItem("color-theme") === "dark" || !("color-theme" in localStorage) && window.matchMedia("(prefers-color-scheme: dark)").matches) {
    themeToggleLightIcon.classList.remove("hidden");
  } else {
    themeToggleDarkIcon.classList.remove("hidden");
  }
  var themeToggleBtn = document.getElementById("theme-toggle");
  function applyDarkMode(isDark) {
    var root = document.documentElement;
    if (isDark) {
      root.classList.add("dark");
      root.classList.add("scheme-dark");
      root.classList.remove("scheme-light");
    } else {
      root.classList.remove("dark");
      root.classList.add("scheme-light");
      root.classList.remove("scheme-dark");
    }
  }
  themeToggleBtn.addEventListener("click", function() {
    themeToggleDarkIcon.classList.toggle("hidden");
    themeToggleLightIcon.classList.toggle("hidden");
    if (localStorage.getItem("color-theme")) {
      if (localStorage.getItem("color-theme") === "light") {
        applyDarkMode(true);
        localStorage.setItem("color-theme", "dark");
      } else {
        applyDarkMode(false);
        localStorage.setItem("color-theme", "light");
      }
    } else {
      if (document.documentElement.classList.contains("dark")) {
        applyDarkMode(false);
        localStorage.setItem("color-theme", "light");
      } else {
        applyDarkMode(true);
        localStorage.setItem("color-theme", "dark");
      }
    }
  });
})();
