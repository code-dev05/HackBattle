function myMenuFunction() {
    var i = document.getElementById("navMenu");

    if (i.className === "nav-menu") {
        i.className += " responsive";
    } else {
        i.className = "nav-menu";
    }
}

var a = document.getElementById("loginBtn");
var b = document.getElementById("registerBtn");
var x = document.getElementById("login");
var y = document.getElementById("register");

function login() {
    x.style.left = "4px";
    y.style.right = "-520px";
    a.className += " white-btn";
    b.className = "btn";
    x.style.opacity = 1;
    y.style.opacity = 0;
}

function register() {
    x.style.left = "-510px";
    y.style.right = "5px";
    a.className = "btn";
    b.className += " white-btn";
    x.style.opacity = 0;
    y.style.opacity = 1;
}

document.addEventListener('DOMContentLoaded', function () {
    const dropContainer = document.querySelector("div > div > form > p > label");
    const fileInput = document.querySelector("div > div > form > p > label > input");

    dropContainer.addEventListener("dragover", (e) => {
        // prevent default to allow drop
        e.preventDefault()
    }, false)

    dropContainer.addEventListener("dragenter", () => {
        dropContainer.classList.add("drag-active")
    })

    dropContainer.addEventListener("dragleave", () => {
        dropContainer.classList.remove("drag-active")
    })

    dropContainer.addEventListener("drop", (e) => {
        e.preventDefault()
        dropContainer.classList.remove("drag-active")
        fileInput.files = e.dataTransfer.files
    })
});

