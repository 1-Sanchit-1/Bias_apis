# from django.urls import path
# from .views import contact_form_submission_list

# urlpatterns = [
#     path('contact/', contact_form_submission_list, name='contact_form_submission_list'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactFormSubmissionViewSet

router = DefaultRouter()
router.register(r'contact', ContactFormSubmissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
