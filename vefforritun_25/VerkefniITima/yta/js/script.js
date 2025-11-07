const shapes = document.getElementById("shapes");

const button = document.getElementById("yta");

current_radius = 0

button.addEventListener("click", () => {
    if (current_radius == 0) {
        current_radius = 100
        shapes.style.borderRadius = current_radius + "%";
    } else {
        current_radius = 0
        shapes.style.borderRadius = current_radius + "%";
    }
});

