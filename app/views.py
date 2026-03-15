from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from app.form import ContactForm,CoursesForm


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


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'


class TeamView(TemplateView):
    template_name = 'team.html'