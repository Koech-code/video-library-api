# Generated by Django 4.1.1 on 2022-09-23 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='videos')),
                ('description', models.CharField(max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitorscomment', models.CharField(max_length=275, null=True)),
                ('status', models.BooleanField(default=True)),
                ('visitorspost', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='videoapiapp.video')),
            ],
        ),
    ]