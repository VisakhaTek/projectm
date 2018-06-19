from django.template import Library


# convention for templatetags package is to create a variable
# named register that is an instance of django.templates.Library.
# See https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/
register = Library()

@register.filter(name='split')
def split(value, arg):
    return value.split(arg)

register.tag('split', split)