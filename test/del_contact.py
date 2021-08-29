from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact("ijijiji", "plplplpl", "rererere"))
    app.contact.delete()
