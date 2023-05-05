// This code formats text to red after
// a user clicks DIV#red_header
$(function () {
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
