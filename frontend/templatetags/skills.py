from django import template
from skills.models import Skill

register = template.Library()


class GetSkills(template.Node):

    def render(self,context):

        skills = Skill.objects.filter().order_by('id')

        context["skills"] = skills
        return ''

    @register.tag(name="get_skills")
    def get_skills(parser, token):
        return GetSkills()
