from django.contrib import admin, auth
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from .models import *


class seo_admin(TranslationAdmin):
    save_on_top = True
    fieldsets = (
        ('Заголовок', {
            'fields': ('title',),
        }),
        ('Описание', {
            'fields': ('description',),
        }),
        ('Ключевые слова', {
            'fields': ('keywords',)
        })
    )
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class about_admin(TranslationAdmin):
    save_on_top = True
    fieldsets = (
        ('Наименование в меню', {
            'fields': ('menu_title',),
        }),
        ('Заголовок раздела', {
            'fields': ('title',),
        }),
        ('Текст', {
            'fields': ('text',)
        }),
    )
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class cooperation_admin(TranslationAdmin):
    save_on_top = True
    fieldsets = (
        ('Наименование в меню', {
            'fields': ('menu_title',),
        }),
        ('Заголовок', {
            'fields': ('title',),
        }),
        ('Кнопка "Позвонить в отдел продаж"', {
            'fields': ('sale_button',),
        }),
        ('Телефон отдела продаж', {
            'fields': ('sale_phone',),
        }),
        ('Заголовок "Дарим POSM материалы"', {
            'fields': ('posm_title',),
        }),
        ('Заголовок "Обсудим с вами"', {
            'fields': ('discuss_title',),
        }),
        ('Список из "Обсудим с вами"', {
            'fields': ('discuss_list',),
        }),
        ('Первое изображение', {
            'fields': ('image', 'display_image',),
        }),
        ('Второе изображение', {
            'fields': ('second_image', 'display_second_image',),
        }),
    )
    readonly_fields = ('display_image', 'display_second_image',)
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class vacancy_admin(TranslationAdmin):
    save_on_top = True
    fieldsets = (
        ('Наименование в меню', {
            'fields': ('menu_title',),
        }),
        ('Заголовок "Работа у нас"', {
            'fields': ('title',),
        }),
        ('Описание', {
            'fields': ('description',)
        }),
        ('Кнопка "Отправить"', {
            'fields': ('send_button',)
        }),
        ('Изображение', {
            'fields': ('image', 'display_image',)
        }),
    )
    readonly_fields = ('display_image',)
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class contacts_admin(TranslationAdmin):
    save_on_top = True
    fieldsets = (
        ('Наименование в меню', {
            'fields': ('menu_title',),
        }),
        ('Телефон для всех клиентов', {
            'fields': ('title_call', 'first_phone',),
        }),
        ('Телефон для оптовых клиентов', {
            'fields': ('title_client', 'second_phone',)
        }),
        ('Email', {
            'fields': ('title_email', 'email',)
        }),
        ('Ссылка на Instagram', {
            'fields': ('instagram',)
        }),
    )
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class intro_admin(TranslationAdmin):
    save_on_top = True
    readonly_fields = ('display_image',)
    fieldsets = (
        ('Заголовок', {
            'fields': ('title',),
        }),
        ('Подзаголовок', {
            'fields': ('subtitle',),
        }),
        ('Описание', {
            'fields': ('description',)
        }),
        ('Кнопка "Купить"', {
            'fields': ('buy_button',)
        }),
        ('Изображение', {
            'fields': ('image', 'display_image',),
        }),
    )
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False



class compound_items_admin(SortableInlineAdminMixin, TranslationStackedInline):
    model = compound_items
    ordering = ('order',)
    extra = 0
    fieldsets = (
        ('Заголовок', {
            'fields': ('title',),
        }),
        ('Описание', {
            'fields': ('description',),
        }),
        ('Изображение', {
            'fields': ('image', 'display_image',),
        }),
    )
    readonly_fields = ('display_image',)



class compound_admin(TranslationAdmin):
    inlines = [compound_items_admin]
    save_on_top = True
    fieldsets = (
        ('Заголовок "Из чего сэндвичи"', {
            'fields': ('title',),
        }),
        ('Наименование в нижней части сайта (ингредиенты)', {
            'fields': ('footer_title',),
        }),
    )
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class product_items_admin(SortableAdminMixin, TranslationAdmin):
    model = product_items
    ordering = ('order',)
    extra = 0

    list_display = ['title', 'description', 'color', 'image_tag',]
    fieldsets = (
        ('Заголовок', {
            'fields': ('title',),
        }),
        ('Описание', {
            'fields': ('description',),
        }),
        ('Изображение', {
            'fields': ('image', 'display_image', 'color', 'spicy_boolean',),
        }),
    )
    readonly_fields = ('display_image',)



class product_admin(TranslationAdmin):
    save_on_top = True
    fieldsets = (
        ('Наименование в верхнем меню', {
            'fields': ('menu_title',),
        }),
        ('Наименование в нижней части сайта (Продукты)', {
            'fields': ('footer_title',),
        }),
        ('Заголовок', {
            'fields': ('title',),
        }),
        ('Описание', {
            'fields': ('description',),
        }),
    )
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class general_admin(TranslationAdmin):
    save_on_top = True
    fieldsets = (
        ('Наименование в меню нижней части сайта "Сертификаты"', {
            'fields': ('footer_title_cert',),
        }),
        ('Заголовок "Мы работаем"', {
            'fields': ('title_work',),
        }),
        ('Дни работы', {
            'fields': ('work_days',),
        }),
        ('Часы работы', {
            'fields': ('work_time',),
        }),
        ('Наименование организации (ОсОО)', {
            'fields': ('org_name',),
        }),
        ('Кнопка "Брендбук"', {
            'fields': ('brandbook_button',),
        }),
        ('Заголовок "Для медийного сотрудничества"', {
            'fields': ('title_media',),
        }),
        ('Заголовок "Соглашение о конфиденциальности"', {
            'fields': ('title_confidence',),
        }),
        ('Кнопка "Наверх"', {
            'fields': ('up_button',),
        }),

    )
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(intro, intro_admin)
admin.site.register(seo, seo_admin)
admin.site.register(about, about_admin)
admin.site.register(compound, compound_admin)
admin.site.register(product, product_admin)
admin.site.register(product_items, product_items_admin)
admin.site.register(cooperation, cooperation_admin)
admin.site.register(vacancy, vacancy_admin)
admin.site.register(contacts, contacts_admin)
admin.site.register(general, general_admin)
admin.site.register(model_form)
