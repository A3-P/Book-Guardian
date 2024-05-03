// profile
const profileBtn = document.getElementById("profileBtn");
const profileMenuHeader = document.getElementById("profileMenuHeader").style;

profileMenuHeader.display = "none";

profileBtn.addEventListener("click", function () {
    if (profileMenuHeader.display === "none") {
        profileMenuHeader.display = "flex";
        profileMenuHeader.animation = "slideDown 0.3s ease forwards";
    } else {
        profileMenuHeader.animation = "slideUp 0.3s ease forwards";
        setTimeout(() => {
            profileMenuHeader.display = "none";
        }, 300);
    }
});

//mobile menu
const menuBtn = document.getElementById("menuBtn");
const mobileMenuContainer = document.getElementById("mobileMenuContainer").style;

mobileMenuContainer.display = "none";

menuBtn.addEventListener("click", function () {
    if (mobileMenuContainer.display === "none") {
        mobileMenuContainer.display = "flex";
        mobileMenuContainer.animation = "slideDown 0.3s ease forwards";
    } else {
        mobileMenuContainer.animation = "slideUp 0.3s ease forwards";
        setTimeout(() => {
            mobileMenuContainer.display = "none";
        }, 300);
    }
});

const profileBtnMobile = document.getElementById("profileBtnMobile");
const subMobileMenu = document.getElementById("subMobileMenu").style;

subMobileMenu.display = "none";

profileBtnMobile.addEventListener("click", function () {
    if (subMobileMenu.display === "none") {
        subMobileMenu.display = "flex";
        subMobileMenu.animation = "slideRight 0.3s ease forwards";
    } else {
        subMobileMenu.animation = "slideLeft 0.3s ease forwards";
        setTimeout(() => {
            subMobileMenu.display = "none";
        }, 300);
    }
});

const filterBtnMobile = document.getElementById("filterBtnMobile");
const applyFilters = document.getElementById("applyFilters");

filterBtnMobile.addEventListener("click", function () {
    if (filter.display === "none") {
        applyFilters.innerHTML = "Aplicar"
        filter.display = "flex";
        filter.animation = "slideDown 0.5s ease forwards";
        mobileMenuContainer.top = "11rem"
        mobileMenuContainer.animation = "slideDown 1s ease forwards";

    } else {
        mobileMenuContainer.top = "6rem"
        filter.animation = "slideUp 0.5s ease forwards";
        mobileMenuContainer.animation = "slideDown 1s ease forwards";
        setTimeout(() => {
            filter.display = "none";
        }, 500);
    }
});

// filter
const filterBtn = document.getElementById("filterBtn");
const filter = document.getElementById("filter").style;

filter.display = "none";

filterBtn.addEventListener("click", function () {
    if (filter.display === "none") {
        filter.display = "flex";
        filter.animation = "slideDown 0.5s ease forwards";
    } else {
        filter.animation = "slideUp 0.5s ease forwards";
        setTimeout(() => {
            filter.display = "none";
        }, 500);
    }
});


// home
document.getElementById("homeBtn").addEventListener("click", function(){
    window.location.href = "";
});


// config
document.getElementById("configBtn").addEventListener("click", function(){
    window.location.href = "static/html/configPage.html";
});

//add book
document.getElementById("addBookbtn").addEventListener("click", function(){
    window.location.href = "static/html/addBook.html";
});
