let filterButtons = document.getElementsByClassName('filters-button');

for (const btn of filterButtons) {
  btn.addEventListener('click', function () {
    let content = btn.nextElementSibling;

    if (content.style.maxHeight) {
      btn.querySelector('p').innerHTML = '+';
      content.style.maxHeight = null;
    } else {
      btn.querySelector('p').innerHTML = '-';
      content.style.maxHeight = content.scrollHeight + 'px';
    }
  });
}
