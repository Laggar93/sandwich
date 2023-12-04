from modeltranslation.translator import translator, TranslationOptions
from .models import *


class SeoTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords',)
    required_languages = {'en': ('title',),
                          'ru': ('title',),
                          'kk': ('title',),
                          }


class IntroTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description', 'buy_button',)
    required_languages = {'en': ('title', 'buy_button',),
                          'ru': ('title', 'buy_button',),
                          'kk': ('title', 'buy_button',),
                          }


class AboutTranslationOptions(TranslationOptions):
    fields = ('menu_title', 'title', 'text',)
    required_languages = {'en': ('menu_title', 'title',),
                          'ru': ('menu_title', 'title',),
                          'kk': ('menu_title', 'title',),
                          }


class CompoundTranslationOptions(TranslationOptions):
    fields = ('title', 'footer_title',)
    required_languages = {'en': ('title', 'footer_title',),
                          'ru': ('title', 'footer_title',),
                          'kk': ('title', 'footer_title',),
                          }


class CompoundItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
    required_languages = {'en': ('title',),
                          'ru': ('title',),
                          'kk': ('title',),
                          }


class ProductTranslationOptions(TranslationOptions):
    fields = ('menu_title', 'footer_title', 'title', 'description',)
    required_languages = {'en': ('menu_title', 'footer_title', 'title',),
                          'ru': ('menu_title', 'footer_title', 'title',),
                          'kk': ('menu_title', 'footer_title', 'title',),
                          }


class ProductItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
    required_languages = {'en': ('title',),
                          'ru': ('title',),
                          'kk': ('title',),
                          }


class CooperationTranslationOptions(TranslationOptions):
    fields = ('menu_title', 'title', 'sale_button', 'posm_title', 'discuss_title', 'discuss_list',)
    required_languages = {'en': ('menu_title', 'title', 'sale_button', 'posm_title', 'discuss_title', 'discuss_list',),
                          'ru': ('menu_title', 'title', 'sale_button', 'posm_title', 'discuss_title', 'discuss_list',),
                          'kk': ('menu_title', 'title', 'sale_button', 'posm_title', 'discuss_title', 'discuss_list',),
                          }


class ContactsTranslationOptions(TranslationOptions):
    fields = ('menu_title', 'title_call', 'title_client', 'title_email',)
    required_languages = {'en': ('menu_title', 'title_call', 'title_client', 'title_email',),
                          'ru': ('menu_title', 'title_call', 'title_client', 'title_email',),
                          'kk': ('menu_title', 'title_call', 'title_client', 'title_email',),
                          }


class VacancyTranslationOptions(TranslationOptions):
    fields = ('menu_title', 'title', 'description', 'send_button',)
    required_languages = {'en': ('menu_title', 'title', 'send_button',),
                          'ru': ('menu_title', 'title', 'send_button',),
                          'kk': ('menu_title', 'title', 'send_button',),
                          }


class GeneralTranslationOptions(TranslationOptions):
    fields = ('footer_title_cert', 'title_work', 'work_days', 'org_name', 'brandbook_button', 'title_media', 'title_confidence', 'up_button', 'success_form', 'error_form',)
    required_languages = {'en': ('footer_title_cert', 'title_work', 'work_days', 'org_name', 'brandbook_button', 'title_media', 'title_confidence', 'up_button', 'success_form', 'error_form',),
                          'ru': ('footer_title_cert', 'title_work', 'work_days', 'org_name', 'brandbook_button', 'title_media', 'title_confidence', 'up_button', 'success_form', 'error_form',),
                          'kk': ('footer_title_cert', 'title_work', 'work_days', 'org_name', 'brandbook_button', 'title_media', 'title_confidence', 'up_button', 'success_form', 'error_form',),
                          }


class FormTranslationOptions(TranslationOptions):
    fields = ('name', 'year', 'phone', 'department',)
    required_languages = {'en': ('name', 'year', 'phone', 'department',),
                          'ru': ('name', 'year', 'phone', 'department',),
                          'kk': ('name', 'year', 'phone', 'department',),
                          }


class DepartmentsTranslationOptions(TranslationOptions):
    fields = ('department',)
    required_languages = {'en': ('department',),
                          'ru': ('department',),
                          'kk': ('department',),
                          }


translator.register(seo, SeoTranslationOptions)
translator.register(intro, IntroTranslationOptions)
translator.register(about, AboutTranslationOptions)
translator.register(compound, CompoundTranslationOptions)
translator.register(compound_items, CompoundItemsTranslationOptions)
translator.register(product_items, ProductItemsTranslationOptions)
translator.register(product, ProductTranslationOptions)
translator.register(cooperation, CooperationTranslationOptions)
translator.register(contacts, ContactsTranslationOptions)
translator.register(vacancy, VacancyTranslationOptions)
translator.register(general, GeneralTranslationOptions)
translator.register(form_translation, FormTranslationOptions)
translator.register(departments, DepartmentsTranslationOptions)
