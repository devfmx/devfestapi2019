from rest_framework import serializers
from .models import Hall,Attendee,Speaker,Conference

class HallSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hall
		fields =  ('__all__')

class SpeakerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Speaker
		fields =  ('__all__')

class AttendeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Attendee
		fields =  ('__all__')

class ConferenceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Conference
		fields =  ('__all__')


