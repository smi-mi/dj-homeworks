from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Бренд')
    model = models.CharField(max_length=50, verbose_name='Модель')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Обзорная статья'
        verbose_name_plural = 'Обзорные статьи'

    def __str__(self):
        return str(self.car) + ' ' + self.title

