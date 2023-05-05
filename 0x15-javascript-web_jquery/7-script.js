// download json data and extract a name field
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
    function (data) {
      $('DIV#character').text(`${data.name}`);
    },
    'json');
});
