let config = {
  type: 'slider',
  perView: 3,
  bound: true,
  gap: 20,
  peek: { before: 0, after: 70 },
};

new Glide('.glide', config).mount();
