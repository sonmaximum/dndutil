"""dndutil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from dndpimp import views as dndpimp_views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from dndpimp.backends import MyRegistrationView

urlpatterns = [
	url(r'^$', dndpimp_views.index, name='home'),
	#url(r'^accounts/profile/$', dndpimp_views.index, name='home'),
	url(r'^about/$',
		TemplateView.as_view(template_name='about.html'),
		name='about'),
	url(r'contact/$',
		TemplateView.as_view(template_name='contact.html'),
		name='contact'),
	url(r'^items/(?P<slug>[-\w]+)/$',
		dndpimp_views.item_detail,
		name='item_detail'),
	url(r'^items/(?P<slug>[-\w]+)/edit/$',
		dndpimp_views.edit_item,
		name='edit_item'),
	url(r'^accounts/password/reset/$', auth_views.password_reset,
		{'template_name': 'registration/password_reset_form.html'},
		name='password_reset'),
	url(r'^accounts/password/reset/done/$', 
		auth_views.password_reset_done,
		{'template_name': 'registration/password_reset_done.html'},
		name='password_reset_done'),
	url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		auth_views.password_reset_confirm,
		{'template_name': 'registration/password_reset_confirm.html'},
		name='password_reset_confirm'),
	url(r'^accounts/password/done/$', 
		auth_views.password_reset_complete,
		{'template_name': 'registration/password_reset_complete.html'},
		name='password_reset_complete'),
	url(r'^accounts/register/$', MyRegistrationView.as_view(), 
		name='registration_register'),
	url(r'^create_character/$', 
		dndpimp_views.create_character,
		name='create_character'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
]
