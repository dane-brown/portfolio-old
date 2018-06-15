from django import template
from projects.models import Project

register = template.Library()

class GetProjects(template.Node):

    def render(self, context):

        projects = Project.objects.filter().order_by('id')

        context["projects"] = projects
        return ''

    @register.tag(name="get_projects")
    def get_projects(parser, token):
        return GetProjects()
