$('document').ready(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json',
    (data) => {
      $.each(data.results, (index, movie) => {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
      });
    });
});
