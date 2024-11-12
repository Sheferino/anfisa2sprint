from django.contrib import admin

# Register your models here.
from .models import Category, Topping, IceCream, Wrapper


class IceCreamAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'wrapper']
    list_editable = ['is_published', ]
    search_fields = ['title', ]
    list_filter = ['is_published',]
    empty_value_display = '-empty-'
    filter_horizontal = ('toppings',)


class WrapperAdmin(admin.ModelAdmin):
    list_display = ['title',]
    empty_value_display = 'Не задано'


class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = (IceCreamInline,)
    list_display = ('title', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Wrapper, WrapperAdmin)
