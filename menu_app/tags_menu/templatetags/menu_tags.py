from django import template
from django.urls import reverse, resolve
from ..models import MenuItem
from django.utils.html import mark_safe

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    menu_items = MenuItem.objects.filter(menu_name=menu_name).prefetch_related('children').order_by('order')
    menu_tree = build_menu_tree(menu_items)
    return {'menu_tree': menu_tree, 'current_url': current_url}

def build_menu_tree(menu_items):
    menu_dict = {}
    for item in menu_items:
        menu_dict[item.id] = {'item': item, 'children': []}
        parent_id = item.parent_id
        if parent_id is not None:
            menu_dict[parent_id]['children'].append(menu_dict[item.id])
    menu_tree = []
    for item in menu_dict.values():
        if item['item'].parent_id is None:
            menu_tree.append(item)
    return menu_tree