from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views as core_views

urlpatterns = [
        url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
        url(r'^logout/$', auth_views.LogoutView.as_view(next_page="login"), name='logout'),
        url(r'^signup/$', core_views.signup, name='signup'),
        url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
        url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            core_views.activate, name='activate'),
]