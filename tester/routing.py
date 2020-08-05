from tornado.web import url

from . import views

urlpatterns = [
    url(r'/', views.MainView, name='main'),
    url(r'/moar/?', views.SecondaryView, name='secondary'),
]