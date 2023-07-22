from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import ContactView, ContactSuccessView


urlpatterns = [
    path('', views.index, name='leuport-index'),
    path('about', views.about, name='leuport-about'),
    path('contact', ContactView.as_view(), name='leuport-contact'),
    path('services', views.services, name='leuport-services'),
    path('works', views.works, name='leuport-works'),
    path('blog', views.blog, name='leuport-blog'),
    path('blogs', views.blogs, name='leuport-blogs'),
    path('success/', ContactSuccessView.as_view(), name="success"),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
