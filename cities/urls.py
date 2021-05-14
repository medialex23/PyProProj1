from django.urls import path
#from .views import home
from .views import home, CityDetailView

urlpatterns = [
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('', home, name='home'),
#    path('<int:pk>/', home, name='home'),
#    path('<int:pk>/',CityDetailView.as_view(), name='home'),
]