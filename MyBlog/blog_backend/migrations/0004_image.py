# Generated by Django 2.1.7 on 2019-05-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_backend', '0003_remove_paper_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ImageField(blank=True, null=True, upload_to='static/article_img/%Y/%m/%d/')),
            ],
        ),
    ]