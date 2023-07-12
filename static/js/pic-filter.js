const picBtnContainers = document.querySelector(".pic-filter");
const picContainer = document.querySelector(".pic-list__list");
const pictures = document.querySelectorAll(".pictures");
const pic = document.querySelector(".pic-filter__slide");
const chevron = document.querySelector(".pic-filter__chevron");

pic.addEventListener("click", (e) => {
  console.log("button");

  const active = document.querySelector(".selected");
  // 선택된 아이

  active.classList.remove("selected");
  // 선택된 아이 제거
  // 읽을수없대 뭐를 ? selected를

  const target =
    e.target.nodeName === "BUTTON" ? e.target : e.target.parentNode;
  target.classList.add("selected");

  console.log(e.target);
});

const SHOWING_CLASS = "showing";

chevron.addEventListener("click", (e) => {
  const currentSlide = document.querySelector(`.${SHOWING_CLASS}`);
  const firstSlide = document.querySelector(".pic-filter__slide:first-child");
  console.log(currentSlide);
  if (currentSlide) {
    currentSlide.classList.remove(SHOWING_CLASS);
    const nextSlide = currentSlide.document.querySelector(
      ".pic-filter__slide:nth-child(2)"
    );
    console.log(nextSlide);
    // 다음슬라이드는 2번째걸 택하고
    // nextSlide 하는 이유 ?
    if (nextSlide) {
      nextSlide.classList.add(SHOWING_CLASS);
    } else {
      firstSlide.classList.add(SHOWING_CLASS);
    }
    // next 슬라이드가 없을경우
  } else {
    firstSlide.classList.add(SHOWING_CLASS);
  }
});

// picBtnContainers.addEventListener("click", (e) => {
//   // // 클릭을 하면
//   // const active = document.querySelector(".pic-filter__button.selected");
//   // active.classList.remove("selected");
//   // const target =
//   //   e.target.nodeName === "BUTTON" ? e.target : e.target.parentNode;
//   // target.classList.add("selected");
//   // // 필터가 dataset node를 받고
//   // picContainer.classList.add("anim-out");
// });

// // const form = document.querySelector(".picture__search");

// // form.addEventListener("submit", (e) => {
// //   e.preventDefault();
// //   // 추가로 수행할 작업을 여기에 작성하세요.
// // });

// // // input 값 저장하기
// // function saveInputValue(event) {
// //   const input = document.getElementById("cityInput");
// //   localStorage.setItem("cityValue", input.value);
// // }

// // // 페이지 로드 시 저장된 input 값 복원하기
// // window.addEventListener("DOMContentLoaded", () => {
// //   const input = document.getElementById("cityInput");
// //   const savedValue = localStorage.getItem("cityValue");
// //   if (savedValue) {
// //     input.value = savedValue;
// //   }
// // });

document.addEventListener("DOMContentLoaded", function () {
  // 버튼 요소 선택
  var buttons = document.querySelectorAll(".pic-filter__button");

  // 각 버튼에 이벤트 리스너 추가
  buttons.forEach(function (button) {
    button.addEventListener("click", function () {
      // 버튼에 설정된 query 값 가져오기
      var query = button.getAttribute("data-query");

      // AJAX 요청 생성
      var xhr = new XMLHttpRequest();
      xhr.open(
        "GET",
        "http://127.0.0.1:8000/search/?query=" + encodeURIComponent(query),
        true
      );

      // 요청 전송
      xhr.send();
    });
  });
});
