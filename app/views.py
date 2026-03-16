from django.urls import reverse_lazy
from django.views.generic import  FormView, ListView, TemplateView

from app.form import ContactForm, CoursesForm
from app.models import Portfolio


class IndexView(TemplateView):
    template_name = 'index.html'


class CourseView(TemplateView):
    template_name = 'courses.html'


class CoursesView(FormView):
    form_class = CoursesForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class KurslarView(TemplateView):
    template_name = 'courses.html'


class MentorsView(TemplateView):
    template_name = 'mentors.html'


class PortfolioView(ListView):
    template_name = 'portfolio.html'
    context_object_name = 'portfolios'
    queryset = Portfolio.objects.all()
    paginate_by = 3


class TeamView(TemplateView):
    template_name = 'team.html'
