from rest_framework.reverse import reverse
import pytest


def test_rates_get(api_client):
    response = api_client.get(reverse('api:rate-list'))
    assert response.status_code == 200
    assert response.json()['count']
    assert response.json()['results']


def test_rates_request_post_empty(api_client):
    response = api_client.post(reverse('api:rate-list'), data={})
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'source': ['This field is required.'],
    }


def test_contactus_api_get(api_client):
    response = api_client.get(reverse('api:contactus-list'))
    assert response.status_code == 200


def test_contactus_api_post_valid(api_client ,mailoutbox):
    response = api_client.post(reverse('api:contactus-list'), data={'subject': 'test1', 'email_from': 'test1'})
    assert response.status_code == 400  # errors
    assert response.json() == {
        'email_from': ['Enter a valid email address.'],
        'email_to': ['This field is required.'],
        'message': ['This field is required.']
    }
    assert len(mailoutbox) == 1
    assert mailoutbox[0].subject == 'ContactUs from Currency Project'


@pytest.mark.parametrize('email_from', ('exampleexample.com', '123123', 'WADADADAD'))
def test_contactus_api_post_invalid_email(api_client ,email_from):
    data = {
        'email_from': email_from,
        'email_to': 'example1@example.com',
        'subject': 'test subj',
        'message': 'test text',
    }
    response = api_client.post(reverse('api:contactus-list'), data=data)
    assert response.status_code == 400
    assert response.json() == {'email_from': ['Enter a valid email address.']}


@pytest.mark.parametrize('email_to', ('exampleexample.com', '123123', 'WADADADAD'))
def test_contactus_api_post_invalid_emailto(api_client ,email_to):
    data = {
        'email_from': 'example1@example.com',
        'email_to': email_to,
        'subject': 'test subj',
        'message': 'test text',
    }
    response = api_client.post(reverse('api:contactus-list'), data=data)
    assert response.status_code == 400
    assert response.json() == {'email_to': ['Enter a valid email address.']}
