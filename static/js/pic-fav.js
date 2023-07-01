const item = document.querySelector(".project__description");
const work__icon = document.querySelector(".work__icon");
const work = document.querySelector(".work");
const project = document.querySelector(".project");

project.addEventListener("click", (e) => {
  e.preventDefault();
});

const projectLinks = document.querySelectorAll(".project");

projectLinks.forEach((link) => {
  link.addEventListener("click", (e) => {
    e.preventDefault();
    // 추가로 수행할 작업을 여기에 작성하세요.
  });
});

item.addEventListener("click", (e) => {
  print(item);
  e.preventDefault();
});

work__icon.addEventListener("click", function (e) {
  e.preventDefault();
});

const topHeart = document.getElementById("topHeart");
const bottomHeart = document.getElementById("bottomHeart");

topHeart.addEventListener("click", function (e) {
  e.preventDefault();
  topHeart.style.display = "none";
  bottomHeart.style.display = "block";
});

bottomHeart.addEventListener("click", function (e) {
  e.preventDefault();
  bottomHeart.style.display = "none";
  topHeart.style.display = "block";
});
