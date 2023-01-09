from django import template


from generation.models import Category, Menu

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, name):

    # Get all categories from menu
    categories = Category.objects.filter(menu=Menu.objects.get(title=name).pk)

    category_list = {}

    for category in categories:
        category_list[category.parent_id] = {}

    for category in categories:
        for keys in category_list:
            if category.parent_id == keys:
                category_list[keys][category] = {}

    for key, value in category_list.items():
        for values in value:
            if values.id in category_list.keys():
                category_list[key][values] = category_list[values.id]

    keys = list(category_list.keys())
    for key in keys:
        if key is not None:
            category_list.pop(key, None)

    loaded_context = {
        'category_list': category_list[None]
    }

    return loaded_context


@register.inclusion_tag('menu.html', takes_context=True)
def draw_subcategory(context, object):

    data = context['category_list'][object]

    loaded_context = {
        'category_list': data
    }

    return loaded_context
