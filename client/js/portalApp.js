const swapBtn = document.querySelectorAll('.card__swap');
const loginFace = document.getElementById('login');
const registerFace = document.getElementById('register');

function swapCard() {
  loginFace.classList.toggle('shown');
  loginFace.classList.toggle('hidden');
  registerFace.classList.toggle('shown');
  registerFace.classList.toggle('hidden');
}

for (const btn of swapBtn) {
  btn.addEventListener('click', swapCard);
}
