from django.conf.urls import url
# from .import views
from .views import myfunc,home_page

urlpatterns=[
	
	url(r'^$' , home_page),
	url(r'^data/$', myfunc)
]