from django.test import TestCase
from django.urls import reverse
import pytest

# Add a fixture for creating a test user object in the database
@pytest.fixture
def test_user(db, django_user_model):
    user = django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return user.username, user.password   # this returns a tuple

# Create your tests here.
def test_login_user(client, test_user):
    test_username, test_password = test_user  # this unpacks the tuple
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == False
