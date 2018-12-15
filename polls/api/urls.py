from django.conf.urls import url, include
from rest_framework import routers
from polls.api import views

router = routers.DefaultRouter()
router.register(r'polls', views.PollsList, base_name='polls')
router.register(r'detail', views.PollDetail, base_name='detail')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]