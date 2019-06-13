from django.contrib.auth.forms import PasswordResetForm

from rest_framework import serializers

from .models import Card


class CardSerializer(serializers.HyperlinkedModelSerializer):
    card_number = serializers.CharField(max_length=16, write_only=True)
    cvv_number = serializers.CharField(max_length=3, write_only=True)

    class Meta:
        model = Card
        fields = "__all__"

    def validate_card_number(self, value):
        """
        Check if input card number is valid
        """

        card_numbers = value.lower()

        # check card number length
        if len(card_numbers) != 16:
            raise serializers.ValidationError("You must enter all 16 digits")

        # check card number
        for number in card_numbers:
            try:
                _number = int(number)
            except ValueError:
                raise serializers.ValidationError("You must enter a valid card number")

        return value

    def validate_cvv_number(self, value):
        """
        Check if input cvc number is valid
        """

        cvc_numbers = value.lower()

        # check card number length
        if len(cvc_numbers) != 3:
            raise serializers.ValidationError("You must enter all 3 digits")

        # check card number
        for number in cvc_numbers:
            try:
                _number = int(number)
            except ValueError:
                raise serializers.ValidationError("You must enter a valid cvc number")

        return value

    def create(self, validated_data):
        validated_data.pop("card_number")  # remove card number for safety
        validated_data.pop("cvv_number")  # remove cvv number for safety

        return Card.objects.create(**validated_data)
