// game.js
const gridEl = document.getElementById("grid");
const scoreEl = document.getElementById("score");
const energyEl = document.getElementById("energy");
const sellBtn = document.getElementById("sellBtn");
const descendBtn = document.getElementById("descendBtn");

let score = 0;
let energy = 20;
let backpack = 0;
let depth = 1;
const cols = 12, rows = 8;

function randomOre() {
  return Math.random() < 0.15; // 15% líkur
}

function createGrid() {
  gridEl.innerHTML = "";
  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      const div = document.createElement("div");
      div.className = "tile";
      const hasOre = randomOre();
      div.dataset.ore = hasOre ? "1" : "0";
      div.addEventListener("click", () => dig(div));
      gridEl.appendChild(div);
    }
  }
}

function dig(tile) {
  if (energy <= 0 || tile.classList.contains("dug")) return;
  energy--;
  energyEl.textContent = energy;
  tile.classList.add("dug");
  if (tile.dataset.ore === "1") {
    tile.classList.add("ore");
    backpack++;
  }
}

sellBtn.addEventListener("click", () => {
  score += backpack * depth;
  backpack = 0;
  scoreEl.textContent = score;
});

descendBtn.addEventListener("click", () => {
  depth++;
  energy = 20;
  energyEl.textContent = energy;
  createGrid();
});

createGrid();
