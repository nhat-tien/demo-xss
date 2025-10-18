import datetime
from django.shortcuts import get_object_or_404, redirect
from vulnerable_app.models import Comment, Product


def add_comment(req, product_id):
    if req.method == 'POST':
        if req.user.is_authenticated:
            product = get_object_or_404(Product, id=product_id)
            Comment.objects.create(
                customer=req.user,
                product=product,
                text=req.POST['text'],
                created_at=datetime.datetime.now()
            )

    return redirect('product_detail', product_id=product_id)
    
