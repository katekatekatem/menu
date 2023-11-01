from django import template

from menu.models import Menu


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = Menu.objects.filter(name=menu_name)

    def render_menu(menu_items):
        result = ''
        for item in menu_items:
            result += f'<li><a href="{item.url}">{item.name}</a>'
            children = item.children.all()
            if children:
                result += '<ul>'
                result += render_menu(children)
                result += '</ul>'
            result += '</li>'
        return result

    return render_menu(menu_items)
