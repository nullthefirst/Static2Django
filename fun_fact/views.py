from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .models import FunFactSubmission
from .forms import SubmissionForm

class Submission(CreateView):
    template_name = 'pages/submit.html'
    model = FunFactSubmission
    form_class = SubmissionForm
    
    def get_success_url(self):
        return reverse_lazy('fun:results')

class Results(ListView):
    template_name = 'pages/results.html'
    model = FunFactSubmission
    ordering = ['-id']
    context_object_name = 'submissions'
    

class ResultFocus(DetailView):
    template_name = 'pages/result-focus.html'
    model = FunFactSubmission
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result'] = FunFactSubmission.objects.get(pk=self.kwargs['pk'])
        return context
