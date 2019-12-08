from rest_framework import generics
from devfest_api import serializers,models

class HallList(generics.ListCreateAPIView):

	serializer_class =serializers.HallSerializer
	queryset =  models.Hall.objects.all()

class SpeakerList(generics.ListCreateAPIView):

	serializer_class = serializers.SpeakerSerializer
	queryset =  models.Speaker.objects.all()

class AttendeeList(generics.ListCreateAPIView):

	serializer_class = serializers.AttendeeSerializer
	queryset =  models.Attendee.objects.all()

class ConferenceList(generics.ListCreateAPIView):

	serializer_class = serializers.ConferenceSerializer
	queryset =  models.Conference.objects.all()




