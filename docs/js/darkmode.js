(() => {
  // <stdin>
  (function() {
    var toggles = document.querySelectorAll("[data-theme-toggle]");
    var darkIcons = document.querySelectorAll("[data-theme-toggle-dark-icon]");
    var lightIcons = document.querySelectorAll("[data-theme-toggle-light-icon]");
    if (!toggles.length) return;
    function isDarkPreferred() {
      var stored = null;
      try {
        stored = localStorage.getItem("color-theme");
      } catch (e) {
      }
      if (stored === "dark") return true;
      if (stored === "light") return false;
      return window.matchMedia("(prefers-color-scheme: dark)").matches;
    }
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
    function syncIcons(isDark) {
      for (var i = 0; i < darkIcons.length; i++) {
        darkIcons[i].classList.toggle("hidden", isDark);
      }
      for (var j = 0; j < lightIcons.length; j++) {
        lightIcons[j].classList.toggle("hidden", !isDark);
      }
    }
    var currentDark = isDarkPreferred();
    syncIcons(currentDark);
    function onClick() {
      var newDark = !document.documentElement.classList.contains("dark");
      applyDarkMode(newDark);
      try {
        localStorage.setItem("color-theme", newDark ? "dark" : "light");
      } catch (e) {
      }
      syncIcons(newDark);
    }
    for (var k = 0; k < toggles.length; k++) {
      toggles[k].addEventListener("click", onClick);
    }
  })();
})();
