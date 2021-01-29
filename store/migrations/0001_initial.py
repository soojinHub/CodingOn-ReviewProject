# Generated by Django 3.1.5 on 2021-01-28 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='사용자')),
                ('userid', models.EmailField(max_length=128, verbose_name='아이디')),
                ('userpwd', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='가입일시')),
            ],
            options={
                'verbose_name': 'store 사용자',
                'verbose_name_plural': 'store 사용자들',
                'db_table': 'store_users',
            },
        ),
    ]
