


def test_delete_group(app):
    app.session.login(login="admin", password="secret")
    app.group.delete()
    app.session.logout()