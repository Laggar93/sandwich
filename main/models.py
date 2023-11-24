from django.db import models
from sandwich.functions import get_file_path, resize_img, intro_image
from ckeditor.fields import RichTextField
from django.utils.functional import cached_property
from django.utils.html import format_html
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from colorfield.fields import ColorField


class seo(models.Model):
    title = models.CharField('Заголовок', max_length=1000)
    description = models.CharField('Описание', max_length=1000, blank=True)
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)

    def __str__(self):
        return 'SEO'

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'


class intro(models.Model):
    title = models.CharField('Заголовок', max_length=1000)
    subtitle = models.CharField('Подзаголовок', max_length=1000, blank=True)
    description = models.TextField('Описание', blank=True)
    buy_button = models.CharField('Кнопка "Купить"', max_length=1000)

    image = models.ImageField('Изображение', upload_to=get_file_path)
    image_thumbnail = ImageSpecField(source='image',
                                             processors=[ResizeToFill(804, 918)],
                                             format='PNG',
                                             options={'quality': 100})

    def __str__(self):
        return 'Вступление'

    class Meta:
        verbose_name = 'Вступление'
        verbose_name_plural = 'Вступление'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="300">', img=self.image.url)
    display_image.short_description = 'Предпросмотр изображения'


class about(models.Model):
    menu_title = models.CharField('Наименование в меню', max_length=1000)
    title = models.CharField('Заголовок раздела', max_length=1000)
    text = models.TextField('Текст', blank=True)

    def __str__(self):
        return 'О нас'

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class compound(models.Model):

    title = models.CharField('Заголовок "Из чего сэндвичи"', max_length=1000)
    footer_title = models.CharField('Наименование в нижней части сайта (ингредиенты)', max_length=1000)

    def __str__(self):
        return 'Из чего сэндвичи?'

    class Meta:
        verbose_name = 'Из чего сэндвичи?'
        verbose_name_plural = 'Из чего сэндвичи?'


class compound_items(models.Model):

    order = models.IntegerField('Порядок')
    compound = models.ForeignKey(compound, on_delete=models.CASCADE, related_name='compound_items')

    title = models.CharField('Заголовок', max_length=1000)
    description = models.TextField('Описание', blank=True)

    image = models.ImageField('Изображение', upload_to=get_file_path)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(210, 210)],
                                     format='PNG',
                                     options={'quality': 100})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = 'Булочка'
        verbose_name_plural = 'Булочки'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="300">', img=self.image.url)
    display_image.short_description = 'Предпросмотр изображения'



class product(models.Model):

    menu_title = models.CharField('Наименование в верхнем меню', max_length=1000)
    footer_title = models.CharField('Наименование в нижней части сайта (Продукты)', max_length=1000)
    title = models.CharField('Заголовок', max_length=1000)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return 'Продукция'

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'


class product_items(models.Model):

    order = models.IntegerField('Порядок')
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name='product_items')

    title = models.CharField('Заголовок', max_length=1000)
    description = models.TextField('Описание', blank=True)

    image = models.ImageField('Изображение', upload_to=get_file_path)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(325, 717)],
                                     format='PNG',
                                     options={'quality': 100})
    color = ColorField('Цвет', default='#FF0000')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="300">', img=self.image.url)
    display_image.short_description = 'Предпросмотр изображения'


class cooperation(models.Model):

    menu_title = models.CharField('Наименование в меню', max_length=1000)
    title = models.TextField('Заголовок')
    sale_button = models.CharField('Кнопка "Позвонить в отдел продаж"', max_length=1000)
    sale_phone = models.CharField('Телефон отдела продаж', max_length=1000)

    posm_title = models.CharField('Заголовок "Дарим POSM материалы"', max_length=1000)
    discuss_title = models.CharField('Заголовок "Обсудим с вами"', max_length=1000)
    discuss_list = RichTextField('Список из "Обсудим с вами"')

    image = models.ImageField('Первое изображение', upload_to=get_file_path)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(500, 375)],
                                     format='PNG',
                                     options={'quality': 100})
    second_image = models.ImageField('Второе изображение', upload_to=get_file_path)
    second_image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(325, 717)],
                                     format='PNG',
                                     options={'quality': 100})

    def __str__(self):
        return 'Сотрудничество'

    class Meta:
        verbose_name = 'Сотрудничество'
        verbose_name_plural = 'Сотрудничество'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="300">', img=self.image.url)
    display_image.short_description = 'Предпросмотр первого изображения'

    @cached_property
    def display_second_image(self):
        return format_html('<img src="{img}" width="300">', img=self.second_image.url)
    display_second_image.short_description = 'Предпросмотр второго изображения'


class vacancy(models.Model):

    menu_title = models.CharField('Наименование в меню', max_length=1000)
    title = models.CharField('Заголовок "Работа у нас"', max_length=1000)
    description = models.TextField('Описание', blank=True)
    send_button = models.CharField('Кнопка "Отправить"', max_length=1000)
    image = models.ImageField('Изображение', upload_to=get_file_path)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(500, 375)],
                                     format='PNG',
                                     options={'quality': 100})

    def __str__(self):
        return 'Работа у нас / Вакансии'

    class Meta:
        verbose_name = 'Работа у нас / Вакансии'
        verbose_name_plural = 'Работа у нас / Вакансии'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="300">', img=self.image.url)
    display_image.short_description = 'Предпросмотр изображения'



class contacts(models.Model):

    menu_title = models.CharField('Наименование в меню', max_length=1000)
    title_call = models.CharField('Заголовок "Хочу позвонить"', max_length=1000)
    first_phone = models.CharField('Телефон для связи', max_length=1000)
    title_client = models.CharField('Заголовок "Оптовым клиентам"', max_length=1000)
    second_phone = models.CharField('Телефон для оптовых клиентов', max_length=1000)
    title_email = models.CharField('Заголовок "Связаться с нами"', max_length=1000)
    email = models.EmailField('Email')
    instagram = models.URLField('Ссылка на Instagram')

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class general(models.Model):

    footer_title_cert = models.CharField('Наименование в меню нижней части сайта "Сертификаты"', max_length=1000)
    title_work = models.CharField('Заголовок "Мы работаем"', max_length=1000)
    work_days = models.CharField('Дни работы', max_length=1000)
    work_time = models.CharField('Часы работы', max_length=1000)
    org_name = models.CharField('Наименование организации (ОсОО)', max_length=1000)
    brandbook_button = models.CharField('Кнопка "Брендбук"', max_length=1000)
    title_media = models.CharField('Заголовок "Для медийного сотрудничества"', max_length=1000)
    title_confidence = models.CharField('Заголовок "Соглашение о конфиденциальности"', max_length=1000)
    up_button = models.CharField('Кнопка "Наверх"', max_length=1000)

    def __str__(self):
        return 'Общее'

    class Meta:
        verbose_name = 'Общее'
        verbose_name_plural = 'Общее'
