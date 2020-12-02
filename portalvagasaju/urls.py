from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portal-vagas-aju/', include('appportalvagasaju.urls')),
    path('', RedirectView.as_view(url='/portal-vagas-aju/', permanent=True))

]
