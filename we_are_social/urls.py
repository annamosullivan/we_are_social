from django.conf.urls import url, include
from django.contrib import admin
from .settings import MEDIA_ROOT
from home import views
from contact import views
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from products import views as product_views
from accounts.views import register, profile, login, logout, cancel_subscription, subscriptions_webhook
from threads import views as forum_views
from polls import api_views
from threads import api_views as thread_api_views


urlpatterns = [
    # url(r'^$', views.get_index()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('reusable_blog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),

    # Auth URLs
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    # Stripe URLS
    url(r'^cancel_subscription/$', cancel_subscription, name='cancel_subscription'),
    url(r'^subscriptions_webhook/$', subscriptions_webhook, name='subscriptions_webhook'),

    # Paypal URLs
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return/$', paypal_views.paypal_return),
    url(r'^paypal-cancel/$', paypal_views.paypal_cancel),
    url(r'^products/$', product_views.all_products),

    # Blog URLs
    url(r'^blog/', include('reusable_blog.urls')),

    # Forum URLs
    url(r'^forum/$', forum_views.forum),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', forum_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/$', forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$',forum_views.delete_post, name='delete_post'),
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$',forum_views.thread_vote, name='cast_vote'),

    # REST URLs
    url(r'^threads/polls/$', api_views.PollViewSet.as_view()),
    url(r'^threads/polls/(?P<pk>[\d]+)$', api_views.PollInstanceView.as_view(), name='poll-instance'),
    url(r'^threads/polls/vote/(?P<thread_id>\d+)/$', api_views.VoteCreateView.as_view(), name='create_vote'),
    url(r'^post/update/(?P<pk>[\d+]+)/$', thread_api_views.PostUpdateView.as_view(), name="update-poll"),
    url(r'post/delete/(?P<pk>[\d]+)/$', thread_api_views.PostDeleteView.as_view(), name='delete-poll'),

    # Contact URL
    url(r'^contact$', views.contact, name='contact'),
]
