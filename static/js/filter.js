const workBtnContainer = document.querySelector(".work__categories");
const projectContainer = document.querySelector(".work__projects");
const projects = document.querySelectorAll(".project");
const button = document.querySelector(".category__button");

workBtnContainer.addEventListener("click", (e) => {
  const filter = e.target.dataset.filter || e.target.parentNode.dataset.filter;
  console.log(projects);

  const active = document.querySelector(".category__btn.selected");
  const target =
    e.target.nodeName === "Button" ? e.target : e.target.parentNode;
  active.classList.remove("selected");
  target.classList.add("selected");

  projectContainer.classList.add("anim-out");
  projects.forEach((v) => {
    if (filter === v.dataset.type) {
      v.classList.remove("invisible");
    } else {
      v.classList.add("invisible");
    }
  });

  setTimeout(() => {
    projectContainer.classList.remove("anim-out");
  }, 300);
});

// active가 될경우
