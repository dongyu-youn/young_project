const item = document.querySelector(".project__description");
const work__icon = document.querySelector(".work__icon i");
const work = document.querySelector(".work");

item.addEventListener("click", (e) => {
  e.preventDefault();
});

const firstItem = document.querySelector("work__icon i:first-child");
const secondItem = document.querySelector("work__icon i:nth-child(2)");

work__icon.addEventListener("click", (e) => {
  e.preventDefault();
  console.log("하트이 개");
});

work.addEventListener("click", (e) => {
  e.preventDefault();
});
