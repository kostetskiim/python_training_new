from model.group import Group


def test_delete_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="dfdfd", header="dfdfdf", footer="dfdfdf"))
    app.group.delete()
