from django.urls import path, include
from api import docs

urlpatterns = [
    path("docs/", include(docs.urlpatterns)),
]
