const featureTabButtons = document.getElementsByClassName(
  'feature-tab__button'
);

const recipeShowcaseButtons = document.getElementsByClassName(
  'recipe-showcase__button'
);

for (const btn of featureTabButtons) {
  btn.addEventListener('click', function () {
    btn.nextElementSibling.classList.toggle('feature-tab__content--active');
    btn.classList.toggle('feature-tab__button--active');
  });
}

for (const btn of recipeShowcaseButtons) {
  btn.addEventListener('click', () => {
    if (!btn.classList.contains('recipe-showcase--active')) {
      for (const btn of recipeShowcaseButtons) {
        btn.classList.remove('recipe-showcase--active');
      }

      btn.classList.add('recipe-showcase--active');
    }
  });
}
