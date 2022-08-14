
from django.urls import reverse_lazy

from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm
from django.views import generic
from django.core.mail import send_mail


# Index class
class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rate_count'] = Rate.objects.count()
        return context


# Rate list classes
class RateListView(generic.ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(generic.CreateView):
    queryset = Rate.objects.all()
    template_name = 'create_rate_list.html'
    form_class = RateForm
    success_url = reverse_lazy('rate_list')


class RateUpdateView(generic.UpdateView):
    queryset = Rate.objects.all()
    template_name = 'update_rate_list.html'
    form_class = RateForm
    success_url = reverse_lazy('rate_list')


class RateDeleteView(generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('rate_list')


class RateDetailsView(generic.DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_details.html'


# Contact classes
class ContactUsView(generic.ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contact_us.html'


# Source classes
class SourceShowView(generic.ListView):
    queryset = Source.objects.all()
    template_name = 'source_show.html'


class ContactUsCreateView(generic.CreateView):
    model = ContactUs
    success_url = reverse_lazy('contact_us')
    template_name = 'contact_us_create.html'
    fields = (
        'email_from',
        'email_to',
        'subject',
        'message',
    )

    def form_valid(self, form):
        response = super().form_valid(form)

        subject = 'ContactUs from Currency Project'
        body = f'''
        Subject from client: {self.object.subject}
        Date: {self.object.created}
        Message: {self.object.message}
        Wants to contact
        '''

        send_mail(
            subject,
            body,
            self.object.email_from,
            [self.object.email_to],
            fail_silently=False,
        )

        return response


class SourceCreateView(generic.CreateView):
    queryset = Source.objects.all()
    template_name = 'source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('source_show')


class SourceUpdateView(generic.UpdateView):
    queryset = Source.objects.all()
    template_name = 'source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('source_show')


class SourceDeleteView(generic.DeleteView):
    queryset = Source.objects.all()
    template_name = 'source_delete.html'
    success_url = reverse_lazy('source_show')


class SourceDetailsView(generic.DetailView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'

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
