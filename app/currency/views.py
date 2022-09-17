
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django_filters.views import FilterView

from currency.resources import RateResource
from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm
from currency.tasks import send_contact_us_email

from currency.utils import IsSuperuserRequiredMixin
from currency.filters import RateFilter


# Index class
class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rate_count'] = Rate.objects.count()
        return context


# Rate list classes
class RateListView(FilterView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'rate_list.html'
    paginate_by = 7
    filterset_class = RateFilter

    def get_context_data(self, *args, **kwargs):
        context: dict = super().get_context_data(*args, **kwargs)

        # remove page param from query_string
        filters_params = self.request.GET.copy()
        if self.page_kwarg in filters_params:
            del filters_params[self.page_kwarg]  # self.page_kwarg == 'page'

        context['filters_params'] = filters_params.urlencode()
        context['page_size'] = self.get_paginate_by()

        return context

    def get_paginate_by(self, queryset=None):
        if 'page_size' in self.request.GET:
            paginate_by = self.request.GET['page_size']
        else:
            paginate_by = self.paginate_by

        return paginate_by


class RateCreateView(generic.CreateView):
    queryset = Rate.objects.all()
    template_name = 'create_rate_list.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')


class DownloadRateView(generic.View):
    def get(self, request):
        csv_content = RateResource().export().csv
        return HttpResponse(csv_content, content_type='text/csv')


class RateUpdateView(IsSuperuserRequiredMixin, generic.UpdateView):
    queryset = Rate.objects.all()
    template_name = 'update_rate_list.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')


class RateDeleteView(IsSuperuserRequiredMixin, generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')


class RateDetailsView(generic.DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_details.html'


# Source classes
class SourceShowView(generic.ListView):
    queryset = Source.objects.all()
    template_name = 'source_show.html'


# Contact classes
class ContactUsView(generic.ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contact_us.html'


class ContactUsCreateView(generic.CreateView):
    model = ContactUs
    success_url = reverse_lazy('currency:contact_us')
    template_name = 'contact_us_create.html'
    fields = (
        'email_from',
        'email_to',
        'subject',
        'message',
    )

    def form_valid(self, form):
        response = super().form_valid(form)

        send_contact_us_email.delay(self.object.subject, self.object.email_from)

        return response


class SourceCreateView(generic.CreateView):
    queryset = Source.objects.all()
    template_name = 'source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_show')


class SourceUpdateView(generic.UpdateView):
    queryset = Source.objects.all()
    template_name = 'source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_show')


class SourceDeleteView(generic.DeleteView):
    queryset = Source.objects.all()
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source_show')


class SourceDetailsView(generic.DetailView):

    queryset = Source.objects.all()
    template_name = 'source_details.html'


# Rest example
# def api_get_rate_list(request):
#     queryset = Rate.objects.all()
#     response_content = []
#
#     for rate in queryset:
#         response_content.append({
#             'id': rate.id,
#             'buy': float(rate.buy),
#             'sale': float(rate.sale),
#         })
#     # return HttpResponse(json.dumps(response_content), content_type='application/json')
#     return JsonResponse(response_content, safe=False)

# Source functions
# def source_show(request):
#
#     context = {
#         'source_list': Source.objects.all(),
#     }
#
#     return render(request, 'source_show.html', context=context)
#
#
# def source_create(request):
#
#     if request.method == 'POST':
#         form = SourceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/source/show/')
#     elif request.method == 'GET':
#         form = SourceForm()
#
#     context = {'form': form}
#
#     return render(request, 'source_create.html', context=context)
#
#
# def source_update(request, source_id):
#
#     source_instance = get_object_or_404(Source, id=source_id)
#
#     if request.method == 'POST':
#         form = SourceForm(request.POST, instance=source_instance)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/source/show/')
#     elif request.method == 'GET':
#         form = SourceForm(instance=source_instance)
#
#     context = {'form': form}
#
#     return render(request, 'source_create.html', context=context)
#
#
# def source_details(request, source_id):
#
#     source_instance = get_object_or_404(Source, id=source_id)
#     context = {'instance': source_instance}
#
#     return render(request, 'source_details.html', context=context)
#
#
# def source_delete(request, source_id):
#
#     source_instance = get_object_or_404(Source, id=source_id)
#     context = {'instance': source_instance}
#     if request.method == "POST":
#         source_instance.delete()
#         return HttpResponseRedirect('/source/show/')
#
#     return render(request, 'source_delete.html', context=context)
