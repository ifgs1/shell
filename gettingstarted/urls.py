from django.conf.urls import include, url
from django.contrib import admin
import hello.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^register', hello.views.registerManager, name='registerManager'),
    url(r'^login', hello.views.loginUser, name='login'),
    url(r'^islogged', hello.views.isLoggedUser, name='isLoggedUser'),
    url(r'^logout', hello.views.logoutUser, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ride', hello.views.createRide, name='createRide'),
    url(r'^joinride', hello.views.joinRide, name='joinRide'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
