from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from products.forms import ReviewForm
from products.models import Product, Review


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object

        avg_rating = product.reviews.aggregate(Avg('rating'))['rating__avg']
        context['avg_rating'] = round(avg_rating, 1) if avg_rating else None

        return context


@login_required
def create_review(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product', pk=product.id)
    else:
        form = ReviewForm()

    return render(request, 'products/review.html', {'form': form, 'product': product})
