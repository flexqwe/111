from django.forms import ModelForm
from app.models import Contact,Courses,Kurslar,Portfolio


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'


class CoursesForm(ModelForm):

    class Meta:
        model = Courses
        fields = '__all__'
class KurslaForm(ModelForm):

    class Meta:
        model = Kurslar
        fields = '__all__'