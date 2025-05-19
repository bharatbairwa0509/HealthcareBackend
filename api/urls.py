from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView
from .views import *


urlpatterns = [
    # Auth
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  


    # Patient
    path('patients/', PatientListCreate.as_view()),
    path('patients/<int:pk>/', PatientDetail.as_view()),

    # Doctor
    path('doctors/', DoctorListCreate.as_view()),
    path('doctors/<int:pk>/', DoctorDetail.as_view()),

    # Mappings
    path('mappings/', MappingListCreate.as_view()),
    path('mappings/<int:pk>/', MappingDetail.as_view()),
    path('mappings/patient/<int:patient_id>/', PatientDoctorByPatient.as_view()),
]
