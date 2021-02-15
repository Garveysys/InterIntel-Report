# from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, FormView
from .forms import SearchForm
from django.contrib.postgres.search import SearchVector



from .models import Car


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = SearchForm
    

class SearchResultsView(ListView):
    model = Car
    template_name = 'search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Car.objects.annotate(
            search1 = SearchVector('name', 'brand'),
        ).filter(search1=query)
        return object_list