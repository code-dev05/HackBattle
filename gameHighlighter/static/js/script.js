function myMenuFunction() {
    var i = document.getElementById("navMenu");

    if (i.className === "nav-menu") {
        i.className += " responsive";
    } else {
        i.className = "nav-menu";
    }
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

