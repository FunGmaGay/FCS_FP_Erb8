document.addEventListener('DOMContentLoaded', () => {
    const signInButton = document.getElementById("signIn");
    const signUpButton = document.getElementById("signUp");
    const container = document.querySelector(".container");

    console.log("Script loaded"); // For debugging

    if (signInButton && signUpButton && container) {
        signInButton.addEventListener("click", () => {
            console.log("Login button clicked");
            container.classList.add("right-panel-active");
        });

        signUpButton.addEventListener("click", () => {
            console.log("Register button clicked");
            container.classList.remove("right-panel-active");
        });
    } else {
        console.error("Elements not found: Check IDs and class names.");
    }
});