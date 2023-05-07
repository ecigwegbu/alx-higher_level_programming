// Write a JavaScript script that fetches from https://fourtonfish.com
// /hellosalut/?lang=fr and displays the value of hello from that fetch
// in the HTML tag DIV#hello
$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr',
    function (data) {
      $('DIV#hello').text(`${data.hello}`);
    },
    'json');
});
