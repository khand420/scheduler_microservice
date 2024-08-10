from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer


# jobs/views.py

from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
from .tasks import schedule_job

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        job = serializer.save()
        # Schedule the job using Celery
        schedule_job.delay(job.id)

# class JobDetailView(generics.RetrieveAPIView):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer



# class JobViewSet(viewsets.ModelViewSet):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer