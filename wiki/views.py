from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.views.generic import FormView
from .forms import FriendlyForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from wiki.models import Page


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {'pages': pages})

class PageDetailView(DetailView):
    """ Renders a specific page based on its slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })


class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'content', 'author']
    template_name = 'new.html'



class ContactView(FormView):
    form_class = FriendlyForm
    template_name = 'contact-us.html'
    success_url = reverse_lazy('contact-us')

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        return super(ContactView, self).form_valid(form)

    def send_mail(self, valid_data):
        # Send mail logic
        print(valid_data)
        pass

