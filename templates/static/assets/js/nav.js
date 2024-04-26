// profile
const profileBtn = document.getElementById("profileBtn");
const profileMenuHeader = document.getElementById("profileMenuHeader").style;
const goToLoginPage = document.getElementById("goToLoginPage");

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

goToLoginPage.addEventListener("click", function () {
    window.location.href = "nadoxLoginScreen/index.html";
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