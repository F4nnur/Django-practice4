from django.db import models


# Create your models here.
class Question(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, blank=False, null=False)
    quest = models.TextField(blank=True)
    # сделать test_id null=true и переделать наследование id Вопросы -> Тесты -> прохождение
    test = models.ForeignKey('Test', on_delete=models.DO_NOTHING, related_name='testidforquest', null=True)
    var1 = models.CharField(max_length=255)
    var2 = models.CharField(max_length=255)
    var3 = models.CharField(max_length=255)
    var4 = models.CharField(max_length=255)
    var1_isTrue = models.BooleanField(default=False)
    var2_isTrue = models.BooleanField(default=False)
    var3_isTrue = models.BooleanField(default=False)
    var4_isTrue = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'


class Test(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    name_of_test = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Тесты'


class Entering(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    test = models.ForeignKey('Test', on_delete=models.DO_NOTHING, related_name='testidforentering')
    quest = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='questionid')
    answer_of_user = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Прохождение'
        verbose_name_plural = 'Прохождение'
