from django.shortcuts import render
from .models import Event
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'events/home.html', context)


def about(request):
    return render(request, 'events/about.html')


class EventListView(ListView):
    model = Event
    template_name = 'events/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'events'
    ordering = ['-start_date']


class EventDetailView(DetailView):
    model = Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'description', 'start_date', 'end_date']

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'description', 'start_date', 'end_date']

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.organizer:
            return True
        return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.organizer:
            return True
        return False
