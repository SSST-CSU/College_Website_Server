# Generated by Django 2.0.2 on 2018-05-20 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivalArticles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '文章的栏目',
                'verbose_name_plural': '文章的栏目',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(verbose_name='创建时间')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('author', models.CharField(max_length=30, verbose_name='作者')),
                ('editor', models.CharField(max_length=30, verbose_name='编辑')),
                ('content', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='栏目名称')),
            ],
            options={
                'verbose_name': '栏目',
                'verbose_name_plural': '栏目',
            },
        ),
        migrations.CreateModel(
            name='ArticleStat',
            fields=[
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ArticleManagement.Article', verbose_name='文章')),
                ('stat', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': '文章是状态',
                'verbose_name_plural': '文章的状态',
            },
        ),
        migrations.AddField(
            model_name='archivalarticles',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArticleManagement.Article', verbose_name='文章'),
        ),
        migrations.AddField(
            model_name='archivalarticles',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArticleManagement.Column', verbose_name='栏目'),
        ),
    ]
