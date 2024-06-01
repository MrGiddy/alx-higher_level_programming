// fetches and lists the title for all movies using a URL

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function (data, textStatus) {
  $.each(data.results, function (i, movie) {
    const title = document.createElement('li');
    title.innerText = movie.title;
    $('UL#list_movies').append(title);
  });
});
