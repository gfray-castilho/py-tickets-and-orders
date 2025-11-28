from django.db.models import QuerySet

from db.models import Movie

from django.db import transaction

from db.models import Movie

def get_movies(
    title = None,
    genres_ids: list[int] = None,
    actors_ids: list[int] = None,
) -> QuerySet:
    queryset = Movie.objects.all()


    if title is not None:
        queryset = queryset.filter(title__icontains=title)

    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


@transaction.atomic
def create_movie(**kwargs) -> Movie:
    movie = Movie.objects.create(**kwargs)
    return movie
