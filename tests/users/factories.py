import factory

from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    """Test User factory"""

    class Meta:
        model = User
        django_get_or_create = ("id",)

    id = factory.Faker("uuid4")
    password = factory.Faker(
        "password",
        length=10,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True,
    )
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    is_active = True
    is_staff = False


class SuperUserFactory(UserFactory):
    """Test super user factory, inherited from UserFactory"""

    is_staff = True
    is_superuser  = True