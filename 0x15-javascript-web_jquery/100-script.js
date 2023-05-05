// Write a JavaScript script that updates the text
// color of the <header> element to red
// (#FF0000) without jQuery:
window.addEventListener('load', function () {
  document.querySelector('header')
    .setAttribute('style', 'color: #FF0000');
});
