const recipeShowcaseButtons = document.getElementsByClassName(
  'recipe-showcase__button'
);

const recipeCards = document.getElementsByClassName('recipe-card');

function changeRecipeBtnColour() {
  if (!btn.classList.contains('recipe-showcase--active')) {
    for (const btn of recipeShowcaseButtons) {
      btn.classList.remove('recipe-showcase--active');
    }
    btn.classList.add('recipe-showcase--active');
  }
}

for (const btn of recipeShowcaseButtons) {
  btn.addEventListener('click', changeRecipeBtnColour);
}
