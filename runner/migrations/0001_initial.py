# Generated by Django 2.0.2 on 2021-03-20 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnvVar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='变量名')),
                ('value', models.CharField(max_length=100, verbose_name='变量值')),
                ('desc', models.CharField(default='', max_length=200, verbose_name='描述')),
                ('project_id', models.IntegerField(verbose_name='项目id')),
                ('env_name', models.CharField(max_length=20, verbose_name='环境名称')),
            ],
            options={
                'db_table': 'env_var',
            },
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='fixture名称')),
                ('desc', models.CharField(default='', max_length=500, verbose_name='fixture描述')),
                ('code', models.TextField(max_length=30000, verbose_name='代码')),
                ('creator_nickname', models.CharField(max_length=64, verbose_name='创建人昵称')),
                ('project_id', models.IntegerField(verbose_name='项目id')),
            ],
            options={
                'db_table': 'fixture',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='项目名称')),
                ('env_config', models.CharField(max_length=100, verbose_name='环境配置')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.AlterUniqueTogether(
            name='envvar',
            unique_together={('project_id', 'env_name', 'name')},
        ),
    ]