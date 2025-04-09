from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from billing.models import Basket
from products.models import Product


class BasketView(View, LoginRequiredMixin):
    def get(self, request):
        basket, _ = Basket.objects.get_or_create(user=request.user)

        return render(
            request,
            'billing/basket.html',
            {'basket_items': list(basket.products.all().values()), 'total_amount': sum([product['price'] for product in list(basket.products.all().values())])},
        )

    def post(self, request, product_id):
        basket, _ = Basket.objects.get_or_create(user=request.user)

        basket.products.add(Product.objects.get(id=product_id))
        basket.save()
        return redirect('basket')
