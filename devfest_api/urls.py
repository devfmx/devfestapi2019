from django.urls import path
from devfest_api import views

urlpatterns = [
    path('hall/', views.HallList.as_view()),
	path('speaker/', views.SpeakerList.as_view()),
    path('attendee/', views.AttendeeList.as_view()),
    path('conference/', views.ConferenceList.as_view()),


]
