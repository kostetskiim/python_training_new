from model.contact import Contact


def test_add_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.edit(Contact("edited", "edited", "edited"))
    app.session.logout()