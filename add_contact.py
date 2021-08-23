# -*- coding: utf-8 -*-
from application import Application
from contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(login="admin", password="secret")
    app.create_contact(Contact("ijijiji", "plplplpl", "rererere"))
    app.logout()


def test_add_empty_contact(app):
    app.login(login="admin", password="secret")
    app.create_contact(Contact("", "", ""))
    app.logout()
