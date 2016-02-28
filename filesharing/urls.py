from django.conf.urls import url, include
import filesharing.views as views

urlpatterns = [
    url(r'd/([0-9]{2})$', views.download),
    url(r'^', views.main),

]
