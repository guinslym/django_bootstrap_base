from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.views.generic import TemplateView

from .views import HomeView

urlpatterns = [
 	url(r'^$', HomeView.as_view() ),
]