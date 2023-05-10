const SHOWING_CLASS = "showing";
const firstSlide = document.querySelector(".pic-filter__slide:first-child");
const chevron = document.querySelector(".pic-filter__chevron");

// 클릭할시 showing붙이고 전에거 클릭할시 그전으로 이동

chevron.addEventListener("click", (e) => {
  const currentSlide = document.querySelector(`.${SHOWING_CLASS}`);
  //

  if (currentSlide) {
    currentSlide.classList.remove(SHOWING_CLASS);
    // 현재슬라이드에서 제거
    const nextSlide = currentSlide.nextSibling;
    // 다음슬라이드 선언
    if (nextSlide) {
      // 다음슬라이드에 showing 추가
      nextSlide.classList.add(SHOWING_CLASS);
    } else {
      firstSlide.classList.add(SHOWING_CLASS);
      //
    }
  } else {
    firstSlide.classList.add(SHOWING_CLASS);
  }
});

// 기본적으로

// function slide() {
//   const currentSlide = document.querySelector(`.${SHOWING_CLASS}`);
//   if (currentSlide) {
//     currentSlide.classList.remove(SHOWING_CLASS);
//     const nextSlide = currentSlide.nextSibling;
//     if (nextSlide) {
//       nextSlide.classList.add(SHOWING_CLASS);
//     } else {
//       firstSlide.classList.add(SHOWING_CLASS);
//     }
//   } else {
//     firstSlide.classList.add(SHOWING_CLASS);
//   }
// }

// slide();
// setInterval(slide, 2000);
