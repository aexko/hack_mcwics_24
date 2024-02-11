from django.contrib import admin
from django.urls import path, include
from bootstrap_colors.views import BootstrapColorsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("price-checker/", include("price_checker.urls"), name="home"),
    path("colors.css", BootstrapColorsView.as_view(), name="colors"),
]

