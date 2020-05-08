
//Setting the sign up div to none-display
document.querySelector("#sign-up").style.display = "none";

//Selecting the create_one button so when clicked it would display the sign up div
document.querySelector(".create_one").addEventListener("click", function(){
    document.querySelector("#sign-in").style.display = "none";
    document.querySelector("#sign-up").style.display = "block";
});
//Selecting the sign_in button so when clicked it would display the sign in div
document.querySelector(".sign_in").addEventListener("click", function(){
    document.querySelector("#sign-in").style.display = "block";
    document.querySelector("#sign-up").style.display = "none";
});
