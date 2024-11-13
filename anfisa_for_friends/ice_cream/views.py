from django.shortcuts import render, get_object_or_404

from ice_cream.models import IceCream


def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    ice_cream_detail = get_object_or_404(IceCream.objects.select_related('category', 'wrapper').filter(is_published=True, category__is_published=True), pk=pk)

    context = {'ice_cream': ice_cream_detail, }
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    ice_cream_list = IceCream.objects.select_related('category').filter(
        is_published=True, category__is_published=True).order_by('category__title')
    context = {'ice_cream_list': ice_cream_list}
    return render(request, template, context)
