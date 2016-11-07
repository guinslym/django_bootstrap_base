from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
 	url(r'^$', TemplateView.as_view(template_name="home.html")),
]