from django.urls import path
from . import views

# movies/
# movies/1/details

# app_name = "movies"

urlpatterns = [
    path("", views.index, name="movies_index"),  # We are using an empty string that represents the root of this app.
    path("<int:movie_id>", views.detail, name="movies_detail")
]