console.log("js loaded !!!!......")

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

const btnPhoto = document.getElementById('showImages');
const btnPhoto1 = document.getElementById('showImages1');
const btnPhoto2 = document.getElementById('showImages2');

const showPhoto = document.getElementById('hidden-div');
const showPhoto1 = document.getElementById('hidden-div1');
const showPhoto2 = document.getElementById('hidden-div2');

const backButton = document.getElementById('backButton');

const hidePhoto = document.getElementById('container_flex');

btnPhoto.addEventListener('click', function () {
  // Add code to show the hidden div and hide the button, e.g., using CSS classes or inline style changes
  showPhoto.style.display = 'block'; // Show the hidden div
  showPhoto1.style.display = 'none'; // Show the hidden div
  showPhoto2.style.display = 'none'; // Show the hidden div
  hidePhoto.style.display = 'block';
});
btnPhoto1.addEventListener('click', function () {
  // Add code to show the hidden div and hide the button, e.g., using CSS classes or inline style changes
  showPhoto.style.display = 'none'; // Show the hidden div
  showPhoto1.style.display = 'block'; // Show the hidden div
  showPhoto2.style.display = 'none'; // Show the hidden div
  hidePhoto.style.display = 'block';
});
btnPhoto2.addEventListener('click', function () {
  // Add code to show the hidden div and hide the button, e.g., using CSS classes or inline style changes
  showPhoto.style.display = 'none'; // Show the hidden div
  showPhoto1.style.display = 'none'; // Show the hidden div
  showPhoto2.style.display = 'block'; // Show the hidden div
  hidePhoto.style.display = 'block';
});
backButton.addEventListener('click', function () {
  // Add code to show the hidden div and hide the button, e.g., using CSS classes or inline style changes
  showPhoto.style.display = 'none';
  showPhoto.style.display = 'none';
  hidePhoto.style.display = 'block';
  hidePhoto.classList.add("container_flex");
});