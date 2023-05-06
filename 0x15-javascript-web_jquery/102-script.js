// Write a JavaScript script that fetches and prints how to say “Hello”
// depending on the language
// https://www.fourtonfish.com/hellosalut/hello/
$(function () {
  $('INPUT#btn_translate').on('click', function () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' +
    `${$('INPUT#language_code').val()}`;
    $.getJSON(url)
      .done(function (json) {
        $('DIV#hello').text(json.hello);
      });
  });
});
