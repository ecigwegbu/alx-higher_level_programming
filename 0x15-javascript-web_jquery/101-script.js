// Write a JavaScript script that fetches from https://fourtonfish.com
// /hellosalut/?lang=fr and displays the value of hello from that fetch
// in the HTML tag DIV#hello
$(function () {
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', function () {
    $('UL.my_list').children().last().remove();
  });
  $('DIV#clear_list').on('click', function () {
    $('UL.my_list').empty();
  });
});
