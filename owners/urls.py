from django.urls import path

from owners.views import OwnersView

urlpatterns = [
    path('viewO', OwnersView.as_view()),
]
