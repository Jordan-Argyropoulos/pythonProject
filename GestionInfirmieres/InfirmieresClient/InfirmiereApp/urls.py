from django.urls import path
from . import views

urlpatterns = [
    path('infirmiere/', views.infirmiereApi),
    path('infirmiere/([0-9]+)/', views.infirmiereApi),

    path('soin/', views.ShowAll, name='soin-list'),
    path('soin-detail/<int:pk>/', views.ViewSoin, name='soin-detail'),
    path('soin-create/', views.CreateSoin, name='soin-create'),
    path('soin-update/<int:pk>/', views.updateSoin, name='soin-update'),
    path('soin-delete/<int:pk>/', views.deleteSoin, name='soin-delete'),
    #path('soin/', views.apiSoins),
    #path('soin/([0-9]+)', views.apiSoins)

    path('home/', views.home, name="home")
]
