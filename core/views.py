import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from .models import Customer, Introductions, GeneralSetting, ImageSetting, Knowledge, Certification, Experience, \
    Education, Document, SocialMedia, Message
from .forms import ContactFormValidate
from .utils import OperationResult


def submit_contact_form(request):
    result = OperationResult()

    if request.method != "POST":
        result.set_error("Request method is not valid", 405)
        return render(request, 'index.html', {'result': result})
    try:
        contact_form_validate = ContactFormValidate(request.POST)
        if not contact_form_validate.is_valid():
            result.set_error("Contact form is not valid", 400)
            messages.error(request, result.message)
            return render(request, 'index.html', {'result': result})

        name = contact_form_validate.cleaned_data.get('name')
        email = contact_form_validate.cleaned_data.get('email')
        message = contact_form_validate.cleaned_data.get('message')

        Message.objects.create(
            name=name,
            email=email,
            message=message
        )

        email_result = contact_form_validate.sends_email()

        if email_result.http_status != 200:
            result.set_error("Failed to send email", 500)
            messages.error(request, "Failed to send email")
        else:
            result.set_data("Your message has been sent successfully.")
            messages.success(request, "Your message has been sent successfully.")

    except Exception as e:
        result.set_error("An unexpected error occurred", 500)
        messages.error(request, "An unexpected error occurred")

    # return render(request, 'index.html', {'result': result})
    return JsonResponse(result.to_dict())


def get_general_settings(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except GeneralSetting.DoesNotExist:
        obj = ''
    return obj


def get_customer_settings(cid):
    try:
        obj = Customer.objects.get(id=cid)
    except Customer.DoesNotExist:
        obj = ''
    return obj


def get_customer_introductions(cid):
    try:
        obj = Introductions.objects.get(cid_id=cid)
    except Introductions.DoesNotExist:
        obj = ''
    return obj


def get_customer_knowledges(cid, kl_type):
    try:
        if kl_type.startswith("-"):
            obj = Knowledge.objects.filter(cid_id=cid).exclude(type=kl_type[1:]).order_by('order')
        elif len(kl_type) > 0:
            obj = Knowledge.objects.filter(cid_id=cid).filter(type=kl_type).order_by('order')
        else:
            obj = Knowledge.objects.filter(cid_id=cid).order_by('order')
    except Knowledge.DoesNotExist:
        obj = ''
    return obj


def get_customer_experience(cid):
    try:
        obj = Experience.objects.filter(cid_id=cid).order_by('-start_date')
    except Experience.DoesNotExist:
        obj = ''
    return obj


def get_customer_certification(cid):
    try:
        obj = Certification.objects.filter(cid_id=cid).order_by('-date')
    except Certification.DoesNotExist:
        obj = ''
    return obj


def get_customer_education(cid):
    try:
        obj = Education.objects.filter(cid_id=cid).order_by('-start_date')
    except Certification.DoesNotExist:
        obj = ''
    return obj


def get_customer_social_media(cid):
    try:
        obj = SocialMedia.objects.filter(cid_id=cid)
    except SocialMedia.DoesNotExist:
        obj = ''
    return obj


def get_customer_resume(cid):
    try:
        obj = Document.objects.get(cid_id=cid, type='resume')
    except Document.DoesNotExist:
        obj = ''
    return obj


def get_image_settings(parameter):
    try:
        obj = ImageSetting.objects.get(name=parameter).file
    except ImageSetting.DoesNotExist:
        obj = ''
    return obj


def prettify_value(value):
    # Check if the input is a string
    if not isinstance(value, str):
        raise ValueError("Input must be a string")

    # Check if the input has the correct length
    if len(value) != 13:
        raise ValueError("Input must be a 13-digit string example +905433888888")

    # Format the string as +90 (XXX)-XXX-XXXX
    return f"{value[:3]} ({value[3:6]})-{value[6:9]}-{value[9:13]}"


def customer_navigate_address(adr1, city, country):
    return f'{adr1} {city} {country}'


def index(request):
    # General Settings
    site_author = get_general_settings('site_author')
    site_description = get_general_settings('site_description')
    site_distribution = get_general_settings('site_distribution')
    site_generator = get_general_settings('site_generator')
    site_keywords = get_general_settings('site_keywords')
    site_language = get_general_settings('site_language')
    site_rating = get_general_settings('site_rating')
    site_revisit_after = get_general_settings('site_revisit_after')
    site_title = get_general_settings('site_title')

    # Customer
    customer = get_customer_settings(1)
    if customer:
        customer.phone_prettify = prettify_value(customer.phone)
        customer.address_navigate = customer_navigate_address(
            customer.address, customer.city, customer.country)

    # Introduction of Sections
    introduction = get_customer_introductions(1)

    # Skill
    skills = get_customer_knowledges(1, "Skill")

    # Knowledge
    knowledges = get_customer_knowledges(1, "-Skill")

    # Languages
    languages = get_customer_knowledges(1, "Language")

    # Experience
    experiences = get_customer_experience(1)

    # Certifications
    certifications = get_customer_certification(1)

    # Education
    educations = get_customer_education(1)

    # Social Media
    social_medias = get_customer_social_media(1)

    # Resume
    resume = get_customer_resume(1)

    # Contact Form Validate
    contact_form_validate = ContactFormValidate()

    context = {
        # General Settings
        'site_author': site_author,
        'site_description': site_description,
        'site_distribution': site_distribution,
        'site_generator': site_generator,
        'site_keywords': site_keywords,
        'site_language': site_language,
        'site_rating': site_rating,
        'site_revisit_after': site_revisit_after,
        'site_title': site_title,

        # Customer
        'customer': customer,

        # Introduction
        'introduction': introduction,

        # Skill
        'skills': skills,

        # Knowledge
        'knowledges': knowledges,

        #  Language
        'languages': languages,

        # Experience
        'experiences': experiences,

        # Certifications
        'certifications': certifications,

        # Education
        'educations': educations,

        # Social Media
        'social_medias': social_medias,

        # Resume
        'resume': resume,

        # Contact Form Validate
        'contact_form_validate': contact_form_validate,

        # Image Settings
    }
    return render(request, 'index.html', context=context)


def redirect_url(request, slug_parameter):
    doc = get_object_or_404(Document, slug=slug_parameter)
    return redirect(doc.file.url)
