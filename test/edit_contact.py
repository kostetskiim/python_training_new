from model.contact import Contact


def test_add_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact("ijijiji", "plplplpl", "rererere"))
    app.contact.edit(Contact("edited", "edited", "edited"))
