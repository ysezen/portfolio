# Generated by Django 5.1 on 2024-08-21 20:16

import django.core.validators
import django.db.models.deletion
import portfolio.custom_storages
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('firstname', models.CharField(default='', help_text='This is the first name of the customer.', max_length=254, verbose_name='First Name')),
                ('middlename', models.CharField(blank=True, default='', help_text='This is the middle name of the customer.', max_length=254, verbose_name='Middle Name')),
                ('lastname', models.CharField(default='', help_text='This is the last name of the customer.', max_length=254, verbose_name='Last Name')),
                ('title', models.CharField(default='', help_text='This is the title of the customer.', max_length=254, verbose_name='Title')),
                ('email', models.EmailField(default='', help_text='This is the email of the customer.', max_length=254, verbose_name='Email')),
                ('phone', models.CharField(default='', help_text='This is the phone of the customer.', max_length=254, verbose_name='Phone')),
                ('birthdate', models.DateField(help_text='This is the birthdate of the customer.', verbose_name='Birthdate')),
                ('address', models.CharField(default='', help_text='This is the address of the customer.', max_length=254, verbose_name='Address')),
                ('city', models.CharField(default='', help_text='This is the city of the customer.', max_length=254, verbose_name='City')),
                ('country', models.CharField(default='', help_text='This is the country of the customer.', max_length=254, verbose_name='Country')),
                ('nationality', models.CharField(default='', help_text='This is the nationality of the customer.', max_length=254, verbose_name='Nationality')),
                ('description', models.CharField(blank=True, default='', help_text='This is the description of the customer.', max_length=254, verbose_name='Description')),
                ('image', models.ImageField(blank=True, default='', help_text='This is the image of the customer.', storage=portfolio.custom_storages.ImageSettingStorage(), upload_to='', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'db_table_comment': 'This table stores customer information.',
                'ordering': ['firstname', 'lastname'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('order', models.IntegerField(default=0, help_text='This is the order of the document.', verbose_name='Order')),
                ('slug', models.SlugField(blank=True, default='', help_text='This is the name of the document.', max_length=254, verbose_name='Slug')),
                ('button_text', models.CharField(blank=True, default='', help_text='This is the button text of the document.', max_length=254, verbose_name='Button Text')),
                ('file', models.FileField(blank=True, default='', help_text='This is the file of the document.', storage=portfolio.custom_storages.DocumentStorage(), upload_to='', verbose_name='File')),
                ('description', models.CharField(blank=True, default='', help_text='This is the description of the document.', max_length=254, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('name', models.CharField(blank=True, default='', max_length=254, unique=True)),
                ('description', models.CharField(blank=True, default='', max_length=254)),
                ('parameter', models.CharField(blank=True, default='', max_length=254)),
                ('long_description', models.TextField(blank=True, default='')),
            ],
            options={
                'verbose_name': 'General Setting',
                'verbose_name_plural': 'General Settings',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ImageSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('name', models.CharField(blank=True, default='', help_text='This is variable name for the image.', max_length=254, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', help_text='This is a description for the image.', max_length=254, verbose_name='Description')),
                ('file', models.ImageField(blank=True, default='', help_text='This is the image file.', storage=portfolio.custom_storages.MediaStorage(), upload_to='', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Image Setting',
                'verbose_name_plural': 'Image Settings',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('name', models.CharField(blank=True, default='', help_text='Name of the person who sent the message', max_length=254, verbose_name='Name')),
                ('email', models.EmailField(blank=True, default='', help_text='Email of the person who sent the message', max_length=254, verbose_name='Email')),
                ('message', models.TextField(blank=True, default='', help_text='Message content', verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('name', models.CharField(blank=True, default='', help_text='This is the name of the certification.', max_length=254, verbose_name='Certification Name')),
                ('organization', models.CharField(blank=True, default='', help_text='This is the name of the company.', max_length=254, verbose_name='Company Name')),
                ('date', models.DateField(help_text='This is the date of the certification.', verbose_name='Date')),
                ('description', models.TextField(blank=True, default='', help_text='This is the description of the certification.', verbose_name='Description')),
                ('icon', models.CharField(blank=True, default='', help_text='This is the icon of the certification.', max_length=254, verbose_name='Icon')),
                ('cid', models.ForeignKey(db_comment='This column stores the customer id.', default=1, on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
            ],
            options={
                'verbose_name': 'Certification',
                'verbose_name_plural': 'Certifications',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('school_name', models.CharField(blank=True, default='', help_text='This is the name of the school.', max_length=254, verbose_name='School Name')),
                ('major', models.CharField(blank=True, default='', help_text='This is the major of the school.', max_length=254, verbose_name='Major')),
                ('icon', models.CharField(blank=True, default='', help_text='This is the icon of the education.', max_length=254, verbose_name='Icon')),
                ('start_date', models.DateField(help_text='This is the start date of the education.', verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, default=None, help_text='This is the end date of the education.', null=True, verbose_name='End Date')),
                ('description', models.TextField(blank=True, default='', help_text='This is the description of the education.', verbose_name='Description')),
                ('cid', models.ForeignKey(db_comment='This column stores the customer id.', default=1, on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('company_name', models.CharField(blank=True, default='', help_text='This is the name of the company.', max_length=254, verbose_name='Company Name')),
                ('job_title', models.CharField(blank=True, default='', help_text='This is the position of the experience.', max_length=254, verbose_name='Job Title')),
                ('job_location', models.CharField(blank=True, default='', help_text='This is the location of the experience.', max_length=254, verbose_name='Job Location')),
                ('start_date', models.DateField(help_text='This is the start date of the experience.', verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, default=None, help_text='This is the end date of the experience.', null=True, verbose_name='End Date')),
                ('description', models.TextField(blank=True, default='', help_text='This is the description of the experience.', verbose_name='Description')),
                ('icon', models.CharField(blank=True, default='', help_text='This is the icon of the experience.', max_length=254, verbose_name='Icon')),
                ('cid', models.ForeignKey(db_comment='This column stores the customer id.', default=1, on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='Introductions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('about', models.TextField(blank=True, db_comment='This column stores the about information of the customer.', default='', help_text='This is the about of the customer.', verbose_name='About')),
                ('skill', models.TextField(blank=True, default='', help_text='This is the skill of the customer.', verbose_name='Skill')),
                ('knowledge', models.TextField(blank=True, default='', help_text='This is the knowledge of the customer.', verbose_name='Knowledge')),
                ('language', models.TextField(blank=True, default='', help_text='This is the language of the customer.', verbose_name='Language')),
                ('experience', models.TextField(blank=True, default='', help_text='This is the experience of the customer.', verbose_name='Experience')),
                ('education', models.TextField(blank=True, default='', help_text='This is the education of the customer.', verbose_name='Education')),
                ('certification', models.TextField(blank=True, default='', help_text='This is the certification of the customer.', verbose_name='Certification')),
                ('contact', models.TextField(blank=True, default='', help_text='This is the contact of the customer.', verbose_name='Contact')),
                ('interest', models.TextField(blank=True, default='', help_text='This is the interest of the customer.', verbose_name='Interest')),
                ('cid', models.ForeignKey(db_comment='This column stores the customer id.', on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
            ],
            options={
                'verbose_name': 'Introduction',
                'verbose_name_plural': 'Introductions',
                'db_table_comment': 'This table stores introduction of customers.',
                'ordering': ['cid'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('order', models.IntegerField(default=0, help_text='This is the order of the language.', verbose_name='Order')),
                ('name', models.CharField(blank=True, default='', help_text='This is the name of the language.', max_length=254, verbose_name='Language Name')),
                ('level', models.CharField(blank=True, default='', help_text='This is the level of the language.', max_length=254, verbose_name='Language Level')),
                ('percentage', models.IntegerField(default=50, help_text='This is the level of the language.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Percentage')),
                ('cid', models.ForeignKey(db_comment='This column stores the customer id.', default=1, on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('order', models.IntegerField(default=0, help_text='This is the order of the social media.', verbose_name='Order')),
                ('link', models.URLField(blank=True, default='', help_text='This is the link of the social media.', max_length=254, verbose_name='Link')),
                ('icon', models.CharField(blank=True, default='', help_text='This is the icon of the social media.', max_length=254, verbose_name='Icon')),
                ('description', models.TextField(blank=True, default='', help_text='This is the description of the icon.', verbose_name='Description')),
                ('cid', models.ForeignKey(db_comment='This column stores the customer id.', default=1, on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
            ],
            options={
                'verbose_name': 'Social Media',
                'verbose_name_plural': 'Social Media',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('order', models.IntegerField(default=0, help_text='This is the order of the knowledge.', verbose_name='Order')),
                ('type', models.CharField(blank=True, default='', help_text='This is the type of the knowledge.', max_length=254, verbose_name='Knowledge Type')),
                ('name', models.CharField(blank=True, default='', help_text='This is the name of the knowledge.', max_length=254, verbose_name='Knowledge Name')),
                ('percentage', models.IntegerField(default=50, help_text='This is the level of the knowledge.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Percentage')),
                ('description', models.CharField(blank=True, default='', help_text='This is the description of the knowledge.', max_length=254, verbose_name='Description')),
                ('cid', models.ForeignKey(db_comment='This column stores the customer id.', default=1, on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
            ],
            options={
                'verbose_name': 'Knowledge',
                'verbose_name_plural': 'Knowledges',
                'ordering': ['order', 'type', 'percentage'],
                'indexes': [models.Index(fields=['order', 'type', 'percentage'], name='core_knowle_order_271393_idx')],
            },
        ),
    ]
