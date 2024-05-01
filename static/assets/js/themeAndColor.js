document.addEventListener("DOMContentLoaded", function () {
    const body = document.body;
    const darkThemeRadio = document.getElementById("darkRadio");
    const lightThemeRadio = document.getElementById("lightRadio");
    const autoThemeRadio = document.getElementById("autoRadio");
    const pinkColorButton = document.getElementById("pink");
    const blueColorButton = document.getElementById("blue");

    function updateThemeBasedOnSystemPreference() {
        const prefersDarkMode = window.matchMedia(
            "(prefers-color-scheme: dark)"
        ).matches;
        if (prefersDarkMode) {
            setTheme("dark");
        } else {
            setTheme("light");
        }
    }

    function setTheme(theme) {
        body.setAttribute("data-theme", theme);
        localStorage.setItem("theme", theme);
    }

    function setColor(color) {
        body.setAttribute("data-color", color);
        localStorage.setItem("color", color);
    }

    const savedTheme = localStorage.getItem("theme");
    const savedColor = localStorage.getItem("color");
    if (savedTheme) {
        setTheme(savedTheme);
    } else {
        updateThemeBasedOnSystemPreference();
    }
    if (savedColor) {
        setColor(savedColor);
    }

    window
        .matchMedia("(prefers-color-scheme: dark)")
        .addEventListener("change", (e) => {
            if (e.matches) {
                setTheme("dark");
            } else {
                setTheme("light");
            }
        });

    darkThemeRadio.addEventListener("change", () => {
        if (darkThemeRadio.checked) {
            setTheme("dark");
        }
    });

    lightThemeRadio.addEventListener("change", () => {
        if (lightThemeRadio.checked) {
            setTheme("light");
        }
    });

    autoThemeRadio.addEventListener("change", () => {
        if (autoThemeRadio.checked) {
            updateThemeBasedOnSystemPreference();
        }
    });

    pinkColorButton.addEventListener("click", () => {
        setColor("pink");
    });

    blueColorButton.addEventListener("click", () => {
        setColor("blue");
    });
});
document.getElementById("saveConfig").addEventListener("click", function () {
    window.location.href = "/index";
});
