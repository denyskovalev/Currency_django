import string
import random

from currency.models import Rate, ContactUs


def get_password(length: int = 10) -> str:

    password = ''
    chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        password += random.choice(chars)

    return password


def get_contact_us():
    email_list = []
    for contact in ContactUs.objects.all():
        contact_us_str = f'ID: {contact.id}, Email to: {contact.email_to},' \
                          f' Email from: {contact.email_from}, Subject: {contact.subject},' \
                          f'Text message: {contact.message}'
        email_list.append(contact_us_str)

    return email_list


def get_rate_list():
    rates_list = []
    for rate in Rate.objects.all():
        rate_string = f'ID: {rate.id}, sale: {rate.sale}, buy: {rate.buy}'
        rates_list.append(rate_string)

    return rates_list
