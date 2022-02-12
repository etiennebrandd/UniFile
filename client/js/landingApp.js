const featureTabButtons = document.getElementsByClassName(
  'feature-tab__button'
);

for (const btn of featureTabButtons) {
  btn.addEventListener('click', function () {
    btn.nextElementSibling.classList.toggle('feature-tab__content--active');
    btn.classList.toggle('feature-tab__button--active');
  });
}
