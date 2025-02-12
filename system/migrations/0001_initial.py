# Generated by Django 5.0.6 on 2024-06-24 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='名称')),
                ('desc', models.CharField(max_length=256, verbose_name='描述')),
                ('types', models.SmallIntegerField(default=10, verbose_name='轮播图属于哪个模块')),
                ('img', models.CharField(max_length=256, verbose_name='图片地址')),
                ('target_url', models.CharField(max_length=256, verbose_name='目标地址')),
                ('reorder', models.CharField(max_length=256, verbose_name='排序')),
                ('is_valid', models.SmallIntegerField(default=1, verbose_name='是否有效')),
                ('start_time', models.DateField(verbose_name='开始时间')),
                ('end_time', models.DateField(verbose_name='结束时间')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'trip_django',
                'ordering': ['-reorder'],
            },
        ),
    ]
