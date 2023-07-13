


from django.urls import path, include
from pollapp import views

urlpatterns = [
    path('', views.pollindex.as_view(), name='pollindex'),
    path('details/<int:id>', views.details.as_view(), name='polldetails'),
    path('previouspost/<int:id>', views.previouspost.as_view(), name='pollprevious'),
    path('nextpost/<int:id>', views.nextpost.as_view(), name='pollnextpost'),
    path('results/<int:id>', views.results.as_view(), name='pollresults'),
    path('resultsall', views.resultsall.as_view(), name='pollresultsall'),
    path('searchresultsall', views.searchresultsall.as_view(), name='searchresultsall'),
    path('create', views.create.as_view(), name='pollcreate'),
    path('pollsearch', views.pollsearch.as_view(), name='pollsearch'),
]

