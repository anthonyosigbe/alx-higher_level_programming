// Use jQuery's AJAX method to fetch the character name.

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  // Update the content of DIV#character with the fetched name
  $('#character').text(data.name);
});
