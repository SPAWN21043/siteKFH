from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class AboutAsInfo(models.Model):
    pass


def load_img_slider(filename):
    return f'slider_img/home/{filename}'


class SliderImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    img = models.ImageField(verbose_name='Картинка для слайдера', upload_to=load_img_slider)
    description = models.CharField(max_length=250, verbose_name='Описание на фото')

    class Meta:
        verbose_name = 'Фото для слайдера на главной'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.description


# Модель для главной страницы с фото для слайдера
class MainPageInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150, verbose_name='Title для страницы')
    info_description = CKEditor5Field(verbose_name='Описание для главной страницы', config_name='extends')
    img = models.ManyToManyField(SliderImage, related_name='slider_image')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
