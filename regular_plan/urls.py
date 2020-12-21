from django.urls import include, path
from rest_framework import routers
from regular_plan.Views.views import RegularPlanPublishListView, RegularPlanView

"""
api_router = routers.DefaultRouter()

api_router.register(r"publish", RegularPlanPublishListView, 'publish')
api_router.register(r"", RegularPlanView)


urlpatterns = [
    path('', include(api_router.urls))
]
"""

urlpatterns = [
    path('publish/', RegularPlanPublishListView.as_view({'get': 'list'}), name='publish-true'),
    #path('', RegularPlanView.as_view(), name='regular-plan'),
]