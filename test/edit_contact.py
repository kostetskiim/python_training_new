from model.contact import Contact


def test_add_contact(app):
    app.contact.edit(Contact("edited", "edited", "edited"))
