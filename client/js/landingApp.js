const featureTabButtons = document.getElementsByClassName(
  'feature-tab__button'
);

const recipeShowcaseButtons = document.getElementsByClassName(
  'recipe-showcase__button'
);

const desktopFeatureButtons = document.getElementsByClassName(
  'desktop-features__tab'
);

const desktopFeatureContent = document.querySelector(
  '.desktop-features__content'
);

const featureData = [
  {
    id: 'recipe-tab',
    title: 'Recipe title would go here',
    image: 'url',
    imageAlt: 'An image of something',
    text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur necessitatibus velit ullam cumque minus quasi quibusdam! Voluptatum commodi voluptate beatae aliquam. Ipsam, placeat et autem delectus laboriosam sed eaque nihil sapiente facilis quibusdam, doloremque laborum eligendi ad nesciunt officia! Maiores.',
  },
  {
    id: 'shopping-tab',
    title: 'Shopping title, slightly longer, would appear here',
    image: 'url',
    imageAlt: 'An image of something',
    text: 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Molestiae, minus repellendus libero accusantium quas deleniti aperiam esse tempora neque totam voluptatem excepturi ipsam repudiandae debitis. Assumenda tenetur aspernatur molestiae, error id maiores nisi facere? Ut ex exercitationem minima iste pariatur velit laudantium ab, quam accusantium.',
  },
  {
    id: 'allergy-tab',
    title:
      'The allergy title would be the longest, showing itself right around here',
    image: 'url',
    imageAlt: 'An image of something',
    text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam vel accusantium possimus dolorum dolorem natus accusamus, voluptatem quisquam, id odit eum, harum ea laudantium nostrum numquam quas. Consectetur cumque ad doloremque facere quo. Labore iusto accusamus ex. Impedit fugit ex quia! Molestiae.',
  },
];

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

for (const btn of desktopFeatureButtons) {
  btn.addEventListener('click', () => {
    let chosenFeature = '';

    if (!btn.classList.contains('desktop-features__tab--active')) {
      for (const btn of desktopFeatureButtons) {
        btn.classList.remove('desktop-features__tab--active');
      }

      for (const feature of featureData) {
        if (feature.id === btn.id) {
          chosenFeature = feature;
        }
      }

      btn.classList.add('desktop-features__tab--active');

      desktopFeatureContent.innerHTML = `
      <div class="desktop-features__body">
        <h3>${chosenFeature.title}</h3>
        <br>
        <p>${chosenFeature.text}</p>
      </div>
      <div class="desktop-features__image">
        <img src="${chosenFeature.image}" alt="${chosenFeature.imageAlt}">
      </div>`;
    }
  });
}
