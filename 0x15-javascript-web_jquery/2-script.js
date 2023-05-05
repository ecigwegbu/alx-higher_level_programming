// This code formats text to red after
// a user clicks DIV#red_header
$('DIV#red_header').bind('click', function () {
  $('header').css('color', '#FF0000');
});
