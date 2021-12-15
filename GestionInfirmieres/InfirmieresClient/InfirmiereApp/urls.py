from django.urls import path
from . import views

urlpatterns = [
    path('infirmiere/', views.infirmiereApi),
    path('infirmiere/([0-9]+)', views.infirmiereApi),

    path('soin/', views.soinsApi),
    path('soin/([0-9]+)', views.soinsApi)
]
