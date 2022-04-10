let config = {
  type: 'slider',
  perView: 3,
  bound: true,
  peek: { before: 0, after: 70 },
};

new Glide('.glide', config).mount();
