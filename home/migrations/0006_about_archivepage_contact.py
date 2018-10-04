# Generated by Django 2.0.8 on 2018-10-03 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0005_workpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=256)),
                ('bold_text', models.CharField(blank=True, max_length=20)),
                ('one_liner', models.CharField(blank=True, help_text='One Liner Paragraph', max_length=256)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ArchivePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=256)),
                ('bold_text', models.CharField(blank=True, max_length=20)),
                ('one_liner', models.CharField(blank=True, help_text='One Liner Paragraph', max_length=256)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=256)),
                ('bold_text', models.CharField(blank=True, max_length=20)),
                ('one_liner', models.CharField(blank=True, help_text='One Liner Paragraph', max_length=256)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
