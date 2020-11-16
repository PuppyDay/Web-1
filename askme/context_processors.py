from app.models import Tag, User


def default_tag(arg):
    tags = Tag.objects.all_tags()
    return {'tags': tags}


def default_members(arg):
    members = User.objects.all()[:3]
    return {'members': members}
