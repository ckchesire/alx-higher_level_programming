$.get("https://swapi-api.alx-tools.com/api/films/?format=json",
    function(data, textStatus) {
        const movies = data.results;
        movies.forEach(function(movie){
            $('UL#list_movies').append('<li>' + movie.title); 
        });
    });
