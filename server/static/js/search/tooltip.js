let actionAnchors = document.getElementsByClassName('results-card__anchor');

for (const anchor of actionAnchors) {
  let closestTextDiv = anchor.closest('div.results-card__text');
  let tooltipDisplay = closestTextDiv.querySelector('#tooltip');

  anchor.addEventListener('mouseover', () => {
    let tooltipText = anchor.dataset.tooltip;
    tooltipDisplay.innerHTML = tooltipText;
    tooltipDisplay.style.opacity = '1';
  });

  anchor.addEventListener('mouseout', () => {
    tooltipDisplay.style.opacity = '0';
    tooltipDisplay.innerHTML = '';
  });
}
