import pytest

from users.models import User
from .factories import UserFactory, SuperUserFactory


@pytest.mark.django_db
def test_user_model():
    """ Test user model"""

    # create user model instance
    user = UserFactory(name="test user name")

    assert user.name == "test user name"
    assert user.get_short_name() == user.first_name
    assert user.get_full_name() == "{} {}".format(user.first_name, user.last_name)
    assert user.get_username() == user.email


@pytest.mark.django_db
def test_superuser():
    """ Test superuser creation"""

    # create user model instance
    user = SuperUserFactory.create()

    assert user.is_staff == True
    assert user.is_superuser == True
