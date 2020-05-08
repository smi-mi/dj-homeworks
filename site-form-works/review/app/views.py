from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


class ProductView(View):
    template = 'app/product_detail.html'

    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        reviews = Review.objects.filter(product__id=pk).all()

        context = {
            'form': ReviewForm,
            'product': product,
            'reviews': reviews,
            'is_review_exist': pk in request.session.get('reviewed_products', []),
        }

        return render(request, self.template, context)

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        reviews = Review.objects.filter(product__id=pk).all()

        form = ReviewForm(request.POST)
        Review.objects.create(text=form.data['text'], product=product)
        if request.session.get('reviewed_products'):
            request.session['reviewed_products'] += [pk]
        else:
            request.session['reviewed_products'] = [pk]

        context = {
            'product': product,
            'reviews': reviews,
            'is_review_exist': True,
        }

        return render(request, self.template, context)
