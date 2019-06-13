from django.contrib.auth.forms import PasswordResetForm

from rest_framework import serializers

from .models import User


class ChangePasswordSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for password change endpoint.
    """

    new_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ("new_password",)


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password_reset_form_class = PasswordResetForm

    def validate_email(self, value):
        self.reset_form = self.password_reset_form_class(data=self.initial_data)

        if not self.reset_form.is_valid():
            raise serializers.ValidationError(_("Error"))

        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("Invalid e-mail address"))

        return value

    def save(self):
        request = self.context.get("request")
        opts = {"use_https": request.is_secure(), "request": request}
        self.reset_form.save(**opts)


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # call create_user on user object.
        # Without this the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)

        return user

    class Meta:
        model = User
        fields = ("id", "name", "email", "first_name", "last_name", "auth_token")
        read_only_fields = ("auth_token",)
        extra_kwargs = {"password": {"write_only": True}}


class SignupUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=255, default="")

    def validate(self, data):
        if not data.get("password") or not data.get("confirm_password"):
            raise serializers.ValidationError({"password": "Password is required."})

        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )
        return data

    def create(self, validated_data):
        # call create_user on user object.
        # Without this the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)

        return user

    class Meta:
        model = User
        fields = (
            "id",
            "password",
            "confirm_password",
            "name",
            "email",
            "first_name",
            "last_name",
            "auth_token",
        )
        read_only_fields = ("auth_token",)
        extra_kwargs = {
            "password": {"write_only": True},
            "confirm_password": {"write_only": True},
        }
