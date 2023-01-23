from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie


# Create your views here.
def index(request):
    # Movie.objects.all()
    # Django will generate a SQL statement like this: SELECT * FROM movies_movie

    # Movie.objects.filter(release_year=1984)
    # This will generate a SQL statement like this: SELECT * FROM movies_movie WHERE release_year=2009

    # Movie.objects.get(id=1)
    # We use this statement to get a single object, by a keyword argument. In this case "id".

    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])
    # return HttpResponse

    return render(request, 'movies/index.html', {'movies': movies})

    # return HttpResponse("Hello World!")


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()

    # return HttpResponse(movie_id)
