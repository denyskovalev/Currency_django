
from currency.models import ContactUs


def get_contact_us():
    email_list = []
    for contact in ContactUs.objects.all():
        contact_us_str = f'ID: {contact.id}, Email to: {contact.email_to},' \
                          f' Email from: {contact.email_from}, Subject: {contact.subject},' \
                          f'Text message: {contact.message}'
        email_list.append(contact_us_str)

    return email_list
