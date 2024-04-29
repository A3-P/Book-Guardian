document.addEventListener("DOMContentLoaded", function () {
    // Pesquisa
    const searchInput = document.getElementById("search");
    const searchBtn = document.getElementById("searchBtn");
    const msgSearch = document.querySelector("#alertMsg").style;

    searchBtn.addEventListener("click", function () {
        const searchTerm = searchInput.value.trim().toLowerCase();
        let itemsFound = false;

        document.querySelectorAll(".card").forEach(function (card) {
            const title = card
                .querySelector("#title")
                .textContent.trim()
                .toLowerCase();
            const author = card
                .querySelector("#autora")
                .textContent.trim()
                .toLowerCase();
            const matchesTitle = title.includes(searchTerm);
            const matchesAuthor = author.includes(searchTerm);

            if (matchesTitle || matchesAuthor) {
                card.style.display = "flex";
                itemsFound = true;
            } else {
                card.style.display = "none";
            }
        });

        if (!itemsFound) {
            msgSearch.display = "block";
        } else {
            msgSearch.display = "none";
        }
    });

    // Filtro
    const applyFiltersBtn = document.getElementById("applyFilters");
    const msgFilter = document.querySelector("#alertMsg").style;

    applyFiltersBtn.addEventListener("click", function () {
        const genre = document.getElementById("genre").value;
        const readOrNot = document.getElementById("readOrNot").value;
        let itemsFound = false;

        document.querySelectorAll(".card").forEach(function (card) {
            const cardGenre = card.querySelector("#tag").textContent;
            const cardRead = card
                .querySelector(".fi")
                .classList.contains("read");
            const cardNonRead = card
                .querySelector(".fi")
                .classList.contains("nonRead");

            if (
                (genre === "" || cardGenre === genre) &&
                (readOrNot === "" ||
                    (readOrNot === "read" && cardRead) ||
                    (readOrNot === "nonRead" && cardNonRead))
            ) {
                card.style.display = "flex";
                itemsFound = true;
            } else {
                card.style.display = "none";
            }
        });

        if (!itemsFound) {
            msgFilter.display = "block";
        } else {
            msgFilter.display = "none";
        }
    });
});
