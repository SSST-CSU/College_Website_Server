# Generated by Django 2.0.2 on 2018-04-22 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RoomBorrowingApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ResourceBorrowingSystem.Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='UserManagement.User')),
            ],
        ),
        migrations.CreateModel(
            name='RoomBorrowingRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ResourceBorrowingSystem.Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='UserManagement.User')),
            ],
        ),
    ]
