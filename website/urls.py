from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .views import (
    HomeView, DetailsView, NewsletterView,
    IndexView, ContactView, SignupView
)
from .sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

app_name = "website"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('details.html', DetailsView.as_view(), name='details'),
    path('newsletter.html', NewsletterView.as_view(), name='newsletter'),
    path('index.html', IndexView.as_view(), name='index'),
    path('contact.html', ContactView.as_view(), name='contact'),
    path('signup.html', SignupView.as_view(), name='signup'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]