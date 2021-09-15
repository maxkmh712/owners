from django.urls  import path
from owners.views import DogsView, OwnersView

urlpatterns = [
    path('/owner', OwnersView.as_view()),
    path('/dog', DogsView.as_view()),
]
