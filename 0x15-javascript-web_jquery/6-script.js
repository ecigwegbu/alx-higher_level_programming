// This code formats text to red after
// a user clicks DIV#red_header
$(function () {
  $('DIV#update_header').on('click', function () {
    $('header').text('New Header!!!');
  });
});
