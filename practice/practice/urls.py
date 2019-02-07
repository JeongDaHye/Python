from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

import myblog.views
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myblog.views.home, name="home"),
    path('myblog/<int:blog_id>',myblog.views.detail, name="detail"),
    path('myblog/new/', myblog.views.new, name="new"),
    path('myblog/create/', myblog.views.create, name="create"),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('newportfolio/', portfolio.views.newportfolio, name="newportfolio"),
    path('portfolio/make', portfolio.views.make, name="make"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
