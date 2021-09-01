from model.contact import Contact


def test_add_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact("ijijiji", "plplplpl", "rererere"))
    old_contact = app.contact.get_contact_list()
    contact = (Contact("edited", "edited", "edited"))
    contact.id = old_contact[0].id
    app.contact.edit(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
