"""
Module is responsible for template rendering
"""
import os

from jinja2 import Template


def render(template_name: str, dir_name: str = 'templates', **kwargs) -> str:
    """
    Forms template to render

    Args:
        template_name: name of template to render
        dir_name:

    Returns:
        rendered template as a string
    """
    app_dir = os.getcwd()
    app_name = 'my_simple_app'  # todo: resolve path in other way
    template_path = os.path.join(app_dir, app_name, dir_name, template_name)

    with open(template_path, encoding='utf-8') as file:
        template = Template(file.read())

    return template.render(**kwargs)

