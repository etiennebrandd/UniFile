let config = {
  type: 'slider',
  startAt: 0,
  perView: 3,
  gap: -150,
  rewind: false,
  bound: true,
  breakpoints: {
    1800: {
      perView: 2,
      gap: 0,
    },
  },
};

new Glide('.glide', config).mount();
