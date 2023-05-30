from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import StaticViewSitemap
#from django.urls import path, include

#from .views import HomeView, DetailsView, NewsletterView, IndexView, ContactView
from .views import *

sitemaps = {
    "static": StaticViewSitemap,
}

#app_games = "games"
app_name = "website"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('details.html', DetailsView.as_view(), name='details'),
    path('newsletter.html', NewsletterView.as_view(), name='newsletter'),
    path('index.html', IndexView.as_view(), name='index'),
    path('contact.html', ContactView.as_view(), name='contact'),
    #path("accounts/", include(("django.contrib.auth.urls", 'accounts'), namespace='accounts')),  # new

    path('signup.html', signupform, name = 'signup form'),

    path("sitemap.xml", sitemap,{"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap",),

]
