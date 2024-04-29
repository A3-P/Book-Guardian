document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search");
    const searchBtn = document.getElementById("searchBtn");
    const cards = document.querySelectorAll(".card");

    function performSearch() {
        const searchTerm = searchInput.value.trim().toLowerCase();

        cards.forEach(function (card) {
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
            } else {
                card.style.display = "none";
            }
        });
    }

    searchBtn.addEventListener("click", performSearch);

    searchInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            performSearch();
        }
    });
});
