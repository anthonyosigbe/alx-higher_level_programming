// Use jQuery's ajax method to retrieve the movie data from the URL.

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: function (response) {
    // Loop through each movie in the response.
    $.each(response.results, function (index, movie) {
      // Append each movie title as a list item to UL#list_movies
      $('#list_movies').append(`<li>${movie.title}</li>`);
    });
  }
});
