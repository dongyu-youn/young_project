const picBtnContainers = document.querySelector(".pic-filter");
const picContainer = document.querySelector(".pic-list__list");
const pictures = document.querySelectorAll(".pictures");
const pic = document.querySelector(".pic-filter__button");

pic.addEventListener("click", (e) => {
  const active = document.querySelector(".pic-filter__button.selected");
  const actives = document.querySelector(".pic-filter__button.selected");

  active.classList.remove("selected");
  console.log(e.target);
  const target = e.target;
  target.classList.add("selected");
});

picBtnContainers.addEventListener("click", (e) => {
  // 클릭을 하면
  const active = document.querySelector(".pic-filter__button.selected");
  active.classList.remove("selected");
  const target =
    e.target.nodeName === "BUTTON" ? e.target : e.target.parentNode;
  target.classList.add("selected");

  // 필터가 dataset node를 받고
  picContainer.classList.add("anim-out");
});

// active가 될경우
