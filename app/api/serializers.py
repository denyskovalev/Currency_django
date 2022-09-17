from rest_framework import serializers

from currency.models import Rate, Source, ContactUs


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'currency_type',
            'base_currency_type',
            'buy',
            'sale',
            'created',
            'source',
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'source_name',
            'source_url',
            'created',
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'email_to',
            'subject',
            'message',
            'date_message',
        )
