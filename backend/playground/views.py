from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer
from django.db.models import Q, F, Value, Func, ExpressionWrapper
from django.db.models.aggregates import Count, Max, Min, Avg
from tags.models import TaggedItem


def say_hello(request):
    # queryset = Product.objects.all()
    # queryset = Product.objects.get(pk=1)
    # try:
    #     queryset = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    # queryset = Product.objects.filter(pk=0).first()  # None if empty
    # queryset = Product.objects.filter(pk=0).exists()

    # queryset = Product.objects.filter(unit_price=20)
    # queryset = Product.objects.filter(unit_price__gt=20)
    # queryset = Product.objects.filter(unit_price__range=(20, 30))
    # queryset = Product.objects.filter(collection__id=2)
    # queryset = Product.objects.filter(title__icontains='coffee')
    # queryset = Product.objects.filter(last_update__year=2021)
    # queryset = Product.objects.filter(description__isnull=True)
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # queryset = Product.objects.filter(Q(inventory__lt=10) & Q(unit_price__lt=20))

    # queryset = Product.objects.filter(inventory=F('unit_price'))
    
    # queryset = Product.objects.order_by('title')
    # queryset = Product.objects.latest('title')
    # queryset = Product.objects.order_by('unit_price' ,'-title').reverse()

    # queryset = Product.objects.all()[:5]

    # queryset = Product.objects.values('id', 'title', 'collection__title')
    # queryset = Product.objects.values_list('id', 'title', 'collection__title')     # tuples insted dict

    # queryset = Product.objects.only('id', 'title')
    # queryset = Product.objects.defer('id', 'title')

    # select_related (1)
    # prefetch_related (n)
    # queryset = Product.objects.all()
    # queryset = Product.objects.select_related('collection').all()
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()

    # result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))

    # queryset = Customer.objects.annotate(is_new=Value(True))

    # queryset = Customer.objects.annotate(
    #     full_name = Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )

    # queryset = Customer.objects.annotate(
    #     order_count = Count('order')
    # )

    # discounted_price = ExpressionWrapper(
    #     F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(
    #     discounted_price = discounted_price
    # )

    queryset = TaggedItem.objects.get_tags_for(Product, 1)

    return render(request, 'hello.html', {'name': 'mohsen','result': list(queryset)})
