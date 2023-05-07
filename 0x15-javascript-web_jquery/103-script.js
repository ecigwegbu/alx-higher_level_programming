// Write a JavaScript script that fetches and prints how to say “Hello”
// depending on the language - display when button or ENTER pressed
// https://www.fourtonfish.com/hellosalut/hello/
$(function () {
  $('INPUT#btn_translate').on('click', clkFunc);
  $('INPUT#language_code').on('change', chgFunc);
  function chgFunc () {
    clkFunc();
  }
  function clkFunc () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' +
      `${$('INPUT#language_code').val()}`;
    $.getJSON(url)
      .done(function (json) {
        $('DIV#hello').text(json.hello);
      });
  }
});
