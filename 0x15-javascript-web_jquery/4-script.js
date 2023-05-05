// This code formats text to red after
// a user clicks DIV#red_header
$(function () {
  $('DIV#toggle_header').on('click', function () {
    $('header').toggleClass('red green');
  });
});
