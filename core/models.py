from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from portfolio.custom_storages import MediaStorage, DocumentStorage, ImageSettingStorage

# Create your models here.


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',
    )

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        unique=True,
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    long_description = models.TextField(
        default='',
        blank=True,
    )

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ['name']


class Customer(AbstractModel):
    firstname = models.CharField(
        default='',
        max_length=254,
        blank=False,
        null=False,
        verbose_name='First Name',
        help_text='This is the first name of the customer.',
    )
    middlename = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Middle Name',
        help_text='This is the middle name of the customer.',
    )
    lastname = models.CharField(
        default='',
        max_length=254,
        blank=False,
        null=False,
        verbose_name='Last Name',
        help_text='This is the last name of the customer.',
    )
    title = models.CharField(
        default='',
        max_length=254,
        blank=False,
        null=False,
        verbose_name='Title',
        help_text='This is the title of the customer.',
    )
    email = models.EmailField(
        default='',
        max_length=254,
        blank=False,
        null=False,
        verbose_name='Email',
        help_text='This is the email of the customer.',
    )
    phone = models.CharField(
        default='',
        max_length=254,
        blank=False,
        null=False,
        verbose_name='Phone',
        help_text='This is the phone of the customer.',
    )
    birthdate = models.DateField(
        verbose_name='Birthdate',
        help_text='This is the birthdate of the customer.',
    )
    address = models.CharField(
        default='',
        max_length=254,
        blank=False,
        null=False,
        verbose_name='Address',
        help_text='This is the address of the customer.',
    )
    city = models.CharField(
        default='',
        max_length=254,
        blank=False,
        null=False,
        verbose_name='City',
        help_text='This is the city of the customer.',
    )
    country = models.CharField(
        default='',
        max_length=254,
        blank=False,
        null=False,
        verbose_name='Country',
        help_text='This is the country of the customer.',
    )
    nationality = models.CharField(
        default='',
        max_length=254,
        blank=False,
        null=False,
        verbose_name='Nationality',
        help_text='This is the nationality of the customer.',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='This is the description of the customer.',
    )
    image = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='This is the image of the customer.',
        blank=True,
        storage=ImageSettingStorage(),
    )

    def __str__(self):
        return f'Customer: {self.firstname} {self.lastname}'

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['firstname', 'lastname']
        db_table_comment = 'This table stores customer information.'


class Introductions(AbstractModel):
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE, db_comment='This column stores the customer id.')
    about = models.TextField(
        default='',
        blank=True,
        verbose_name='About',
        help_text='This is the about of the customer.',
        db_comment='This column stores the about information of the customer.'
    )
    skill = models.TextField(
        default='',
        blank=True,
        verbose_name='Skill',
        help_text='This is the skill of the customer.',
    )
    knowledge = models.TextField(
        default='',
        blank=True,
        verbose_name='Knowledge',
        help_text='This is the knowledge of the customer.',
    )
    language = models.TextField(
        default='',
        blank=True,
        verbose_name='Language',
        help_text='This is the language of the customer.',
    )
    experience = models.TextField(
        default='',
        blank=True,
        verbose_name='Experience',
        help_text='This is the experience of the customer.',
    )
    education = models.TextField(
        default='',
        blank=True,
        verbose_name='Education',
        help_text='This is the education of the customer.',
    )
    certification = models.TextField(
        default='',
        blank=True,
        verbose_name='Certification',
        help_text='This is the certification of the customer.',
    )
    contact = models.TextField(
        default='',
        blank=True,
        verbose_name='Contact',
        help_text='This is the contact of the customer.',
    )
    interest = models.TextField(
        default='',
        blank=True,
        verbose_name='Interest',
        help_text='This is the interest of the customer.',
    )

    def __str__(self):
        return f'Introduction: {self.about}'

    class Meta:
        verbose_name = 'Introduction'
        verbose_name_plural = 'Introductions'
        ordering = ['cid']
        db_table_comment = 'This table stores introduction of customers.'


class Knowledge(AbstractModel):
    cid = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        default=1,
        db_comment='This column stores the customer id.'
    )
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
        help_text='This is the order of the knowledge.',
    )
    type = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Knowledge Type',
        help_text='This is the type of the knowledge.',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Knowledge Name',
        help_text='This is the name of the knowledge.',
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='This is the level of the knowledge.',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='This is the description of the knowledge.',
    )

    def __str__(self):
        return f'Knowledge: {self.name}'

    class Meta:
        verbose_name = 'Knowledge'
        verbose_name_plural = 'Knowledges'
        ordering = ['order', 'type', 'percentage']
        indexes = [
            models.Index(fields=['order', 'type', 'percentage']),
        ]


class Language(AbstractModel):
    cid = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        default=1,
        db_comment='This column stores the customer id.'
    )
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
        help_text='This is the order of the language.',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Language Name',
        help_text='This is the name of the language.',
    )
    level = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Language Level',
        help_text='This is the level of the language.',
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='This is the level of the language.',
    )

    def __str__(self):
        return f'Language: {self.name}'

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        ordering = ['order']


class Experience(AbstractModel):
    cid = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        default=1,
        db_comment='This column stores the customer id.'
    )
    company_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Company Name',
        help_text='This is the name of the company.',
    )
    job_title = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Title',
        help_text='This is the position of the experience.',
    )
    job_location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Location',
        help_text='This is the location of the experience.',
    )
    start_date = models.DateField(
        verbose_name='Start Date',
        help_text='This is the start date of the experience.',
    )
    end_date = models.DateField(
        default=None,
        blank=True,
        null=True,
        verbose_name='End Date',
        help_text='This is the end date of the experience.',
    )
    description = models.TextField(
        default='',
        blank=True,
        verbose_name='Description',
        help_text='This is the description of the experience.',
    )
    icon = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Icon',
        help_text='This is the icon of the experience.',
    )

    def __str__(self):
        return f'Experience: {self.company_name}'

    def start_date_pretty(self):
        return self.start_date.strftime('%b %Y')

    def end_date_pretty(self):
        return self.end_date.strftime('%b %Y') if self.end_date else 'Present'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ['start_date']


class Certification(AbstractModel):
    cid = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        default=1,
        db_comment='This column stores the customer id.'
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Certification Name',
        help_text='This is the name of the certification.',
    )
    organization = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Company Name',
        help_text='This is the name of the company.',
    )
    date = models.DateField(
        verbose_name='Date',
        help_text='This is the date of the certification.',
    )
    description = models.TextField(
        default='',
        blank=True,
        verbose_name='Description',
        help_text='This is the description of the certification.',
    )
    icon = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Icon',
        help_text='This is the icon of the certification.',
    )

    def __str__(self):
        return f'Certification: {self.name}'

    class Meta:
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'
        ordering = ['name']


class Education(AbstractModel):
    cid = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        default=1,
        db_comment='This column stores the customer id.'
    )
    school_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='School Name',
        help_text='This is the name of the school.',
    )
    major = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Major',
        help_text='This is the major of the school.',
    )
    icon = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Icon',
        help_text='This is the icon of the education.',
    )
    start_date = models.DateField(
        verbose_name='Start Date',
        help_text='This is the start date of the education.',
    )
    end_date = models.DateField(
        default=None,
        blank=True,
        null=True,
        verbose_name='End Date',
        help_text='This is the end date of the education.',
    )
    description = models.TextField(
        default='',
        blank=True,
        verbose_name='Description',
        help_text='This is the description of the education.',
    )

    def __str__(self):
        return f'Experience: {self.school_name}'

    def start_date_pretty(self):
        return self.start_date.strftime('%b %Y')

    def end_date_pretty(self):
        return self.end_date.strftime('%b %Y') if self.end_date else 'Present'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ['start_date']


class Message(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='Name of the person who sent the message'
    )
    email = models.EmailField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Email',
        help_text='Email of the person who sent the message'
    )
    message = models.TextField(
        default='',
        blank=True,
        verbose_name='Message',
        help_text='Message content'
    )

    def __str__(self):
        return f'Message: {self.name}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['-created_date']


class SocialMedia(AbstractModel):
    cid = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        default=1,
        db_comment='This column stores the customer id.'
    )
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
        help_text='This is the order of the social media.',
    )
    link = models.URLField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Link',
        help_text='This is the link of the social media.',
    )
    icon = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Icon',
        help_text='This is the icon of the social media.',
    )
    description = models.TextField(
        default='',
        blank=True,
        verbose_name='Description',
        help_text='This is the description of the icon.',
    )

    def __str__(self):
        return f'Social Media: {self.link}'

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'
        ordering = ['order']


class Document(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
        help_text='This is the order of the document.',
    )
    slug = models.SlugField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Slug',
        help_text='This is the name of the document.',
    )
    button_text = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Button Text',
        help_text='This is the button text of the document.',
    )
    file = models.FileField(
        default='',
        verbose_name='File',
        help_text='This is the file of the document.',
        blank=True,
        storage=DocumentStorage(),
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='This is the description of the document.',
    )

    def __str__(self):
        return f'Document: {self.slug}'

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ['order']


class ImageSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable name for the image.',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='This is a description for the image.',
    )
    file = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='This is the image file.',
        blank=True,
        storage=MediaStorage(),
    )

    def __str__(self):
        return f'Image Setting: {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ['name']
