from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app.views import IndexView, CourseView, ContactView, KurslarView, PortfolioView
from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('courses/', CourseView.as_view(), name='courses'),
    path('contact/', ContactView.as_view(), name='contact'),
path('kurslar/', KurslarView.as_view(), name='kurslar'),
path('portfolio/', PortfolioView.as_view(), name='portfolio'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
