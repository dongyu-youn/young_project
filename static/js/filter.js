const workBtnContainer = document.querySelector(".category__btn");
const projectContainer = document.querySelector(".work__projects");

workBtnContainer.addEventListener("click", (e) => {
  const filter = e.target.dataset.filter || e.target.parentNode.dataset.filter;
  console.log(filter);
  z;
});
