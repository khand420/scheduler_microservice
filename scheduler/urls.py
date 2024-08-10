from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import JobViewSet

from .views import JobListCreateView, JobDetailView


# router = DefaultRouter()
# router.register(r'jobs', JobViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('jobs/', JobListCreateView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
]