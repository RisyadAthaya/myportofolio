from django import template

register = template.Library()

@register.filter(name="has_group_editor")
def has_group_editor(user):
    return user.groups.filter(name="Editor").exists()