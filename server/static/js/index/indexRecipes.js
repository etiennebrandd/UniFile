const recipes = {
  breakfast: [
    {
      title: 'Berry Banana Breakfast Smoothie',
      img: 'static/images/landing/breakfast-1.jpg',
      description:
        'If you have around 5 minutes to spend in the kitchen, Berry Banana Breakfast Smoothie might be a tremendous lacto ovo vegetarian recipe to try.',
      cost: 2.04,
      time: '5 mins',
    },
    {
      title: 'Homemade Muesli Breakfast Cereal',
      img: 'static/images/landing/breakfast-2.jpg',
      description:
        'Homemade Muesli Breakfast Cereal might be just the morn meal you are searching for.',
      cost: 0.88,
      time: '1 hour 30 mins',
    },
    {
      title: 'Mini Quinoa Egg Breakfast Casserole',
      img: 'static/images/landing/breakfast-3.jpg',
      description:
        "Mini Quinoan Egg Breakfast Casserole might be a good recipe to expand your hor d'oeuvre collection.",
      cost: 1.46,
      time: '30 mins',
    },
  ],

  lunch: [
    {
      title: 'Turkey Ranch BLT',
      img: 'static/images/landing/lunch-1.jpg',
      description:
        'Turkey, bacon, lettice and tomato in pita breads, dressed in ranch sauce.',
      cost: 1.54,
      time: '10 mins',
    },
    {
      title: 'Thai Pasta Salad',
      img: 'static/images/landing/lunch-2.jpg',
      description:
        'Satisfy your Asian craving, with a taste of Thailand. Works well on its own or as part of a larger meal.',
      cost: 3.25,
      time: '45 mins',
    },
    {
      title: 'Orzo Salad With Vegetables and Herbs',
      img: 'static/images/landing/lunch-3.jpg',
      description:
        'Orzo rice with a selection of fresh vegetables and seasonings. Perfect for a lighter lunch.',
      cost: 1.46,
      time: '45 mins',
    },
  ],

  dinner: [
    {
      title: 'BLT Pizza',
      img: 'static/images/landing/dinner-1.jpg',
      description:
        'Colby jack cheese, pizza crust, turkey bacon, and a handful of other ingredients are all it takes to make this recipe so scrumptious.',
      cost: 2.78,
      time: '45 mins',
    },
    {
      title: 'Mixed Paella',
      img: 'static/images/landing/dinner-2.jpg',
      description:
        'A mixture of lemon zest, saffron threads, garlic, and a handful of other ingredients.',
      cost: 2.02,
      time: '45 mins',
    },
    {
      title: 'Ozoni',
      img: 'static/images/landing/dinner-3.jpg',
      description:
        "A good option if you're following a gluten free and dairy free diet.",
      cost: 3.05,
      time: '45 mins',
    },
  ],

  deserts: [
    {
      title: 'German Rhubarb Cake with Meringue',
      img: 'static/images/landing/desert-1.jpg',
      description:
        'A cake filled with rhubarb sandwiched between crisp bits of meringue - two excellent puddings in one!',
      cost: 0.61,
      time: '45 mins',
    },
    {
      title: 'Coconut Cassava Pancakes',
      img: 'static/images/landing/desert-2.jpg',
      description:
        'Coconut flavoured pancakes dressed with honey and served with the freshest fruit.',
      cost: 2.53,
      time: '45 mins',
    },
    {
      title: 'Strawberry Shortcake Cobbler',
      img: 'static/images/landing/desert-3.jpg',
      description:
        'The best parts of shortcake and cobbler fused in to one, delectable, strawberry-flavoured desert!',
      cost: 2.52,
      time: '45 mins',
    },
  ],
};

const recipeShowcaseButtons = document.getElementsByClassName(
  'recipe-showcase__button'
);

for (const btn of recipeShowcaseButtons) {
  btn.addEventListener('click', (event) => {
    if (!btn.classList.contains('recipe-showcase--active')) {
      for (const btn of recipeShowcaseButtons) {
        btn.classList.remove('recipe-showcase--active');
      }
      btn.classList.add('recipe-showcase--active');
      let list;

      if (event.target.id === 'breakfast') {
        list = recipes.breakfast;
      }
      if (event.target.id === 'lunch') {
        list = recipes.lunch;
      }
      if (event.target.id === 'dinner') {
        list = recipes.dinner;
      }
      if (event.target.id === 'deserts') {
        list = recipes.deserts;
      }

      let recipeCards = document.getElementsByClassName('recipe-card');

      // card elements are changed individually rather than making a whole new set of cards, and inserting them in the recipe-showcase
      // reason for this is due to the jittery-ness from rerendered a whole new card
      for (let i = 0; i < recipeCards.length; i++) {
        let img = recipeCards[i].querySelector('.recipe-card__img');
        let title = recipeCards[i].querySelector('.recipe-card__title');
        let description = recipeCards[i].querySelector(
          '.recipe-card__description'
        );
        let cost = recipeCards[i].querySelector('.recipe-card__sinfo');
        let time = recipeCards[i].querySelector('.recipe-card__linfo');

        img.src = list[i].img;
        title.innerHTML = list[i].title;
        description.innerHTML = list[i].description;
        cost.innerHTML = list[i].cost;
        time.innerHTML = list[i].time;

        // using reflow through selecting the offsetHeight - easy but resource expensive
        // index page is fairly lightweight, so no worries for the expense
        recipeCards[i].style.animation = 'none';
        recipeCards[i].offsetHeight;
        recipeCards[i].style.animation = null;
      }
    }
  });
}

// <img src="{{ url_for('static', filename='${item.img}') }}">
