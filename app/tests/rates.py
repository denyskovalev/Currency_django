
from django.urls import reverse


def test_rates_get(client):
    response = client.get(reverse('currency:rate_list'))
    assert response.status_code == 200


def test_rates_get_page(client):
    response = client.get(f"{reverse('currency:rate_list')}?page=2&page_size=1")
    assert response.status_code == 200
