from django.template import Library


# convention for templatetags package is to create a variable
# named register that is an instance of django.templates.Library.
# See https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/
register = Library()


@register.inclusion_tag('legal/copyright.html')
def copyright_disclaimer():
    """
    copyright can be included in any template, anywhere.
    """
    return
