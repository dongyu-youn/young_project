const openButton = document.querySelector(".pic-filter__filterbtn");
const modal = document.querySelector(".modal");
const overlay = document.querySelector(".body");

const openModal = () => {
  modal.classList.remove("hidden");
};

const closeModal = () => {
  modal.classList.add("hidden");
};

openButton.addEventListener("click", (e) => {
  modal.classList.remove("hidden");
});

picContainer.addEventListener("click", console.log("hello"));