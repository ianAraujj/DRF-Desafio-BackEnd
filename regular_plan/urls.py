from django.urls import path
from regular_plan.Views import views

urlpatterns = [
    path('publish/', views.RegularPlanPublishListView.as_view(), name="publish")
]