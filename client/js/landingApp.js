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

    if (btn.classList.contains('feature-tab__button--active')) {
      btn.querySelector('p').textContent = '-';
    } else {
      btn.querySelector('p').textContent = '+';
    }
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
