from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path('admin/', admin.site.urls),
    path('api/army/', include('WFB_Army.urls')),
    path('api/stratagem/', include('WFB_Stratagem.urls')),
    path('api/match/', include('WFB_Match.urls')),
    path('api/user/', include('WFB_User.urls')),
    path('api/scenario/', include('WFB_Scenario.urls')),
    path('api/objective/', include('WFB_Objective.urls')),
    path('api/match-request/', include('WFB_MatchRequest.urls')),
    path('api/personal-objective/', include('WFB_PersonalObjectives.urls')),
    path('api/army-list/', include('WFB_ArmyList.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

