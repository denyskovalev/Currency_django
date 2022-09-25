
from django.urls import reverse
import pytest


def test_contact_us_get(client):
    response = client.get(reverse('currency:contact_us_create'))
    assert response.status_code == 200


def test_contact_us_post_empty(client):
    response = client.post(reverse('currency:contact_us_create'), data={})
    assert response.status_code == 200  # error
    assert response.context_data['form'].errors == {
        'email_from': ['This field is required.'],
        'email_to': ['This field is required.'],
        'subject': ['This field is required.'],
        'message': ['This field is required.']
    }


def test_contact_us_post_valid(client, mailoutbox):
    data = {
        'email_from': 'example@example.com',
        'email_to': 'example1@example.com',
        'subject': 'test subj',
        'message': 'test text'
    }
    response = client.post(reverse('currency:contact_us_create'), data=data)
    assert response.status_code == 302  # success
    assert response.headers['Location'] == '/currency/contact-us/'

    assert len(mailoutbox) == 1
    assert mailoutbox[0].subject == 'ContactUs from Currency Project'


@pytest.mark.parametrize('email_from', ('exampleexample.com', '123123', 'WADADADAD'))
def test_contact_us_post_invalid_email(client, email_from):
    data = {
        'email_from': email_from,
        'email_to': 'example1@example.com',
        'subject': 'test subj',
        'message': 'test text',
    }
    response = client.post(reverse('currency:contact_us_create'), data=data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'email_from': ['Enter a valid email address.']}

# python app/manage.py dumpdata currency.source > source.json
