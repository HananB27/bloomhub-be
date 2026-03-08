"""Smoke tests so pytest collects at least one test (CI requires tests to run)."""

import pytest
from django.conf import settings


def test_settings_loaded():
    """Django settings module is loaded."""
    assert settings.SECRET_KEY
    assert "django.contrib.admin" in settings.INSTALLED_APPS


@pytest.mark.django_db
def test_database_connection():
    """Database is reachable (no-op if using SQLite)."""
    from django.db import connection

    connection.ensure_connection()
