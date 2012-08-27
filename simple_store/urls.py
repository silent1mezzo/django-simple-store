from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'simple_store.views.index', name='store'),
    url(r'^category/(?P<slug>[-\w]+)/$', 'simple_store.views.category', name='category'),
    url(r'^product/(?P<slug>[-\w]+)/$', 'simple_store.views.product', name='product'),
    url(r'^cart/$', 'simple_store.views.cart', name='cart'),
)