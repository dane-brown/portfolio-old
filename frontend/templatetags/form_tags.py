from django import template
from frontend.forms import ContactForm

register = template.Library()


class GetContactForm(template.Node):

    def render(self, context):
        context['form'] = ContactForm()
        return ''

@register.tag(name="get_contact_form")
def get_contact_form(parser,token):
    return GetContactForm()
