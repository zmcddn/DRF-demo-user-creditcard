import pytest

from users.models import User
from .factories import UserFactory


@pytest.mark.django_db
def test_user_model():
    """ Test user model"""

    # create user model instance
    user = UserFactory(name="test user name")

    assert user.name == "test user name"
