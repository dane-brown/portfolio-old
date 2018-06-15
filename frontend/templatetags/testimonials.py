from django import template
from testimonials.models import Testimonial

register = template.Library()


class GetTestimonial(template.Node):

    def render(self,context):

        testimonials = Testimonial.objects.filter().order_by('id')

        context["testimonials"] = testimonials
        return ''

    @register.tag(name="get_testimonials")
    def get_testimonials(parser, token):
        return GetTestimonial()
