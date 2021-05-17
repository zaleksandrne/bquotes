from rest_framework import serializers

from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super(QuoteSerializer, self).to_representation(instance)
        domain_name = 'http://127.0.0.1:8010'
        full_path = domain_name + instance.image.url
        representation['image'] = full_path
        return representation

    class Meta:
        fields = '__all__'
        model = Quote
