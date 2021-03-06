# Generated by Django 3.0.8 on 2021-02-11 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=150)),
                ('amount_of_upvotes', models.PositiveSmallIntegerField(default=0)),
                ('author_name', models.CharField(blank=True, max_length=150)),
            ],
            options={
                'ordering': ['creation_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(blank=True, default='', max_length=150)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_id', to='news.Post')),
            ],
            options={
                'ordering': ['creation_date'],
            },
        ),
    ]
