from model.group import Group


def test_edit_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="dfdfd", header="dfdfdf", footer="dfdfdf"))
    app.group.edit(Group(name="edited", header="edited", footer="edited"))
