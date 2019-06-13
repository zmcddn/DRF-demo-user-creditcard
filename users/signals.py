from django.contrib.auth import authenticate, login
from django.dispatch import receiver
from registration.signals import user_registered


@receiver(user_registered)
def activate_user(user, request, **kwargs):
    user.is_active = True
    user.save()
    user = authenticate(
        username=request.POST["username"], password=request.POST["password1"]
    )
    login(request, user)
