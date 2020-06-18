"""questionbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from core import views as core_views

urlpatterns = [
    path('', core_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('core/profile/', core_views.profile_page, name='profile_page'),
    path('core/<int:question_pk>/', core_views.question_detail, name='question_detail'),
    path('core/new_question/', core_views.new_question, name='new_question'),
    path('core/<int:question_pk>/new_answer/', core_views.new_answer, name='new_answer'),
    path('core/<int:question_pk>/delete', core_views.delete_question, name='delete_question'),
    path('core/search', core_views.search_questions, name="search_questions"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
