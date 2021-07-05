# Generated by Django 3.2.4 on 2021-07-01 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name_of_test', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('quest', models.TextField(blank=True)),
                ('var1', models.CharField(max_length=255)),
                ('var2', models.CharField(max_length=255)),
                ('var3', models.CharField(max_length=255)),
                ('var4', models.CharField(max_length=255)),
                ('true_var', models.IntegerField()),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='testidforquest', to='site_with_tests.test')),
            ],
        ),
        migrations.CreateModel(
            name='Entering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_of_user', models.CharField(max_length=255)),
                ('quest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionid', to='site_with_tests.question')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='testidforentering', to='site_with_tests.test')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]