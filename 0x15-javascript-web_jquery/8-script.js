$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const movieList = $('#list_movies');
  const movieTitles = data.results.map(movie => `<li>${movie.title}</li>`);
  movieList.append(movieTitles.join(''));
});
