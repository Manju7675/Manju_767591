from django.urls import path
from . import views


urlpatterns = [
    # path('post',views.post),
    #            path("reel",views.reel1),
               path("",views.home,name='homefeed'),
               path('upload',views.upload,name='upload')
               ]

