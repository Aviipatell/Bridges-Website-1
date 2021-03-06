"""bridgesWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from joinOurTeam.views import joinOurTeam_page
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
import home.views
import articles.views
import about.views
import contact.views
import linktree.views
import mentorship.views
import joinOurTeam.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.homepage, name='home'),
    # path('articles/', articles.views.articles_page, name='articles-page'),
    path('articles/', include('articles.urls')),
    path('about/', include('about.urls')),
    path('contact/', contact.views.contactpage, name='contact-page'),
    path('linktree/', linktree.views.linktree_page, name='linktree'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('mentorship/', mentorship.views.mentorship_page, name='mentorship'),
    path('joinOurTeam/', joinOurTeam.views.joinOurTeam_page, name='join-our-team')
]
