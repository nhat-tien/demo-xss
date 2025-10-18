from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path

from vulnerable_app.views import auth, home, product, comment, customer


urlpatterns = [
    path('', home.index, name='home'),
    path('login/', auth.customer_login, name="login"),
    path('register/', auth.customer_register, name="register"),
    path('unsafe/product/', product.product_index_unsafe, name="product_index_unsafe"),
    path('unsafe/product/<int:product_id>/', product.product_detail_unsafe, name="product_detail_unsafe"),
    path('product/', product.product_index_safe, name="product_index"),
    path('product/<int:product_id>/', product.product_detail_safe, name="product_detail"),
    path('comment/<int:product_id>/', comment.add_comment, name="add_comment"),
    path('profile/', customer.profile, name="profile"),
    path('logout/', auth.logout_view, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
