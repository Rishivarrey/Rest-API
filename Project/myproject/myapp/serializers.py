
from rest_framework import serializers
from myapp.models import advisor,user,bookingreq



class advisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = advisor
        fields = ( 'id',
                  'name',
                  'photourl',
                   'booking_id',
                   'bookingtime'
                   )
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ( 'id',
                   'name',
                   'email',
                   'password',
                   'login')

class bookingreqSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookingreq
        fields = ( 'id',
                   'user_id',
                   'advisor_id',
                   )