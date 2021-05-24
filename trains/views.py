from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from trains.forms import TrainForm
from trains.models import Train


def home(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 10)
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    form = TrainForm()
    context = {'page_obj': trains, 'form': form}
    return render(request, 'trains/home.html', context)


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Поїзд успішно створений!'


class TrainUpdateView(UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')


class TrainDeleteView(DeleteView):
    model = Train
    # template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, "Місто було успішно створене")
        return self.post(request, *args, **kwargs)

class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    context_object_name = 'object'
    template_name = 'trains/detail.html'
