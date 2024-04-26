const singIn = document.getElementById("singIn");
const login= document.getElementById("goToLoginPage");
const singincontainer = document.getElementById("singincontainer").style;
const logincontainer = document.getElementById("logincontainer").style;

singIn.addEventListener("click", function() {
    singincontainer.display = "block";
    logincontainer.display = "none";
});   

login.addEventListener("click", function() {
    singincontainer.display = "none";
    logincontainer.display = "block";
}); 