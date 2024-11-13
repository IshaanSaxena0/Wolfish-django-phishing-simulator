from django.urls import path
from .views import *
from . import views
# app_name = "mailer"

urlpatterns = [
    path('', MailView, name="mail-view"),
    path('login/', Login, name="login"),
    path('logout/', logout_view, name="logout"),
    path('add-smtp/', SenderAddView, name="add-sender-view"),
    path('list-mails/', SenderListView, name="list-sender-view"),
    path('detail-mail/<id>/', SenderDetailView, name="detail-sender"),
    path('user-data/<mail_unq_id>/<user_unq_id>/', UserDetailView, name="user-detail"),
    path('temp/', RenderTemplate, name="render-template"),
    path('render-template/<url_slug>/<render_id>', DynamicTemplate, name="dyn-template"),
    #path('send-test-email/', views.test_email_view, name='send_test_email'),
    #path('debug-email/', views.debug_email_view, name='debug-email'),
    path('dynamic-template/<str:url_slug>/<str:render_id>/', views.DynamicTemplate, name='dynamic-template'),
    path('render-template/<str:url_slug>/', views.RenderTemplate, name='render-template'),
    path('dynamic-template/<str:url_slug>/', views.DynamicTemplate, name='dynamic-template'),
    path('fake-login/', views.fake_login, name='fake_login'),
]