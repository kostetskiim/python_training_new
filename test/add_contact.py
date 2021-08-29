# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact("ijijiji", "plplplpl", "rererere"))


def test_add_empty_contact(app):
    app.contact.create(Contact("", "", ""))


