from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from currency.models import Rate, ContactUs
from currency.forms import RateForm


# Index functions
def index_page(request):
    return render(request, 'index.html')


# Rate list functions
def rate_list(request):

    context = {
        'rate_list': Rate.objects.all(),
    }

    return render(request, 'rate_list.html', context=context)


def create_rate_list(request):

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

    context = {'form': form}

    return render(request, 'create_rate_list.html', context=context)


def update_rate_list(request, rate_id):

    # try:
    #     rate_instance = Rate.objects.get(id=rate_id)
    # except Rate.DoesNotExist:
    #     raise Http404
    #  # or

    rate_instance = get_object_or_404(Rate, id=rate_id)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=rate_instance)

    context = {'form': form}

    return render(request, 'update_rate_list.html', context=context)


def rate_details(request, rate_id):

    rate_instance = get_object_or_404(Rate, id=rate_id)
    context = {'instance': rate_instance}

    return render(request, 'rate_details.html', context=context)


def rate_delete(request, rate_id):

    rate_instance = get_object_or_404(Rate, id=rate_id)
    context = {'instance': rate_instance}
    if request.method == "POST":
        rate_instance.delete()
        return HttpResponseRedirect('/rate/list/')

    return render(request, 'rate_delete.html', context=context)


# Contact us functions
def contact_us(request):

    context = {
        'contact_us': ContactUs.objects.all(),
    }

    return render(request, 'contact_us.html', context=context)
