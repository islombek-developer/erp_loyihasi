from django.urls import path
from  .views import HomeView,DetailView,Categoryes,CartDetailView,delete

app_name = 'shop'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('product/',CartDetailView.as_view(),name='cart'),
    path('detail/<int:id>/',DetailView.as_view(),name='detail'),
    path('categor/<int:id>/',Categoryes.as_view(),name='categor'),
    path('delete/<int:id>/',delete,name='delete'),

]