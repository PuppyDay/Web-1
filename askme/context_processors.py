from app.models import Tag, Author


def default_tag(arg):
    tags = Tag.objects.all_tags()[:6]
    return {'tags': tags}


def default_members(arg):
    members = Author.objects.all()[:5]
    return {'members': members}
