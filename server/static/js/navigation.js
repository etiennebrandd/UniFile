let navigation = document.getElementById('site-nav');

navigation.addEventListener(
  'mousemove',
  () => {
    console.log('enter');
    navigation.classList.remove('site-nav__hidden');
  },
  true
);

navigation.addEventListener('mouseleave', () => {
  console.log('over');
  navigation.classList.add('site-nav__hidden');
});
