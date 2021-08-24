# -*- coding: utf-8 -*-
from fixture.application import Application
from model.contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.create(Contact("ijijiji", "plplplpl", "rererere"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.create(Contact("", "", ""))
    app.session.logout()
