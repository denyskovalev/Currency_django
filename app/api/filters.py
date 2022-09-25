import django_filters
from currency.models import Rate, Source, ContactUs


# gt, gte, lt, lte, isnull, [i]exact, [i]startswith, [i]endswith, [i]contains, date, in
class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'buy': ('gte', 'lte', 'gt', 'lt'),  # buy__gte, buy__lte
            'sale': ('gte', 'lte', 'gt', 'lt'),  # sale__gte, buy__lte
            'base_currency_type': ('exact', ),
            'currency_type': ('exact', ),
            'source': ('exact', ),
        }


class SourceFilter(django_filters.FilterSet):
    class Meta:
        model = Source
        fields = {
            'source_name': ('exact',),
            'created': ('gte', 'lte', 'gt', 'lt'),
        }


class ContactUsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = {
            'email_from': ('exact', ),
            'email_to': ('exact', ),
            'subject': ('exact', ),
            'date_message': ('gte', 'lte', 'gt', 'lt'),
        }
