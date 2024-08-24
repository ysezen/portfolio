from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameter', 'updated_date', 'created_date']
    list_filter = ['name', 'description', 'parameter', 'updated_date', 'created_date']
    list_editable = ['description', 'parameter']
    ordering = ['name', 'description', 'parameter', 'updated_date', 'created_date']
    list_per_page = 25

    class Meta:
        model = GeneralSetting


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'title', 'email', 'phone', 'country', 'updated_date', 'created_date']
    search_fields = ['firstname', 'lastname', 'title', 'email', 'phone', 'country']
    list_filter = ['firstname', 'lastname', 'title', 'email', 'phone', 'country']
    list_display_links = ['firstname']
    ordering = ['id']
    list_per_page = 25

    class Meta:
        model = Customer


@admin.register(Introductions)
class IntroductionsAdmin(admin.ModelAdmin):
    list_display = ['cid', 'get_customer_name', 'skill', 'knowledge', 'updated_date', 'created_date']

    def get_customer_name(self, obj):
        return f'{obj.cid.firstname} {obj.cid.lastname}'

    get_customer_name.short_description = 'Customer Name'


@admin.register(Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ['cid', 'order', 'type', 'name', 'percentage']
    search_fields = ['type', 'name']
    list_filter = ['type', 'name']
    list_editable = ['order', 'type', 'name', 'percentage']
    ordering = ['order']
    list_per_page = 25

    class Meta:
        model = Knowledge


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = [ 'cid', 'order', 'name', 'level', 'percentage']
    search_fields = ['name', 'level']
    list_filter = ['name', 'level']
    list_editable = ['order', 'name', 'level', 'percentage']
    ordering = ['order']
    list_per_page = 25

    class Meta:
        model = Language


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['cid', 'company_name', 'job_title', 'job_location', 'start_date', 'end_date', 'description',
                    'updated_date', 'created_date']
    search_fields = ['company_name', 'job_title', 'job_location', 'start_date', 'end_date', 'description']
    list_filter = ['company_name', 'job_title', 'job_location', 'start_date', 'end_date', 'description']
    list_editable = ['company_name', 'job_title', 'job_location', 'start_date', 'end_date', 'description']
    ordering = ['start_date']
    list_per_page = 25

    class Meta:
        model = Experience


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['cid', 'name', 'organization', 'date']
    search_fields = ['name', 'organization']
    list_filter = ['name', 'organization', 'date']
    list_editable = ['name', 'organization', 'date']
    ordering = ['-date']
    list_per_page = 25

    class Meta:
        model = Certification


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['cid', 'school_name', 'major', 'icon', 'start_date', 'end_date']
    search_fields = ['school_name']
    list_filter = ['school_name']
    list_editable = ['school_name', 'major', 'icon', 'start_date', 'end_date']
    ordering = ['-start_date']
    list_per_page = 25

    class Meta:
        model = Education


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'updated_date', 'created_date']
    search_fields = ['name', 'email', 'message', 'updated_date', 'created_date']
    list_filter = ['name', 'email', 'message', 'updated_date', 'created_date']
    list_editable = ['email', 'message']
    ordering = ['name', 'email', 'message', 'updated_date', 'created_date']
    list_per_page = 25

    class Meta:
        model = Message


@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'file', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'file', 'updated_date', 'created_date']
    list_filter = ['name', 'description', 'file', 'updated_date', 'created_date']
    list_editable = ['description', 'file']
    ordering = ['name', 'description', 'file', 'updated_date', 'created_date']
    list_per_page = 25

    class Meta:
        model = ImageSetting


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'link', 'icon', 'description', 'updated_date', 'created_date']
    search_fields = ['link', 'icon', 'description']
    list_filter = ['order', 'link', 'icon', 'description']
    list_editable = ['order', 'link', 'icon', 'description']
    ordering = ['order']
    list_per_page = 25

    class Meta:
        model = SocialMedia


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'cid', 'order', 'type', 'slug', 'button_text', 'file', 'description', 'updated_date', 'created_date']
    search_fields = ['order', 'slug', 'button_text', 'file', 'description']
    list_filter = ['order', 'slug', 'button_text', 'file', 'description']
    list_editable = ['order', 'slug', 'button_text', 'file', 'description']
    ordering = ['order']
    list_per_page = 25

    class Meta:
        model = Document

