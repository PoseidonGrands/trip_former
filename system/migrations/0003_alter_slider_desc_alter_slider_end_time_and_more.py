# Generated by Django 5.0.6 on 2024-06-24 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_alter_slider_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='desc',
            field=models.CharField(max_length=256, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='end_time',
            field=models.DateField(null=True, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='reorder',
            field=models.CharField(max_length=256, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='start_time',
            field=models.DateField(null=True, verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='types',
            field=models.SmallIntegerField(default=10, null=True, verbose_name='轮播图属于哪个模块'),
        ),
    ]
