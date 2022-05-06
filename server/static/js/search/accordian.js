let filterButtons = document.getElementsByClassName('accordian-button');

for (const btn of filterButtons) {
  btn.addEventListener('click', function () {
    for (const btnToClose of filterButtons) {
      btnToClose.querySelector('p').innerHTML = '+';
      btnToClose.nextElementSibling.style.maxHeight = null;
    }

    let contentToShow = btn.nextElementSibling;

    if (contentToShow.style.maxHeight) {
      btn.querySelector('p').innerHTML = '+';
      contentToShow.style.maxHeight = null;
    } else {
      btn.querySelector('p').innerHTML = '-';
      contentToShow.style.maxHeight = contentToShow.scrollHeight + 'px';
    }
  });
}
