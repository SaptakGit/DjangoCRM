from django.urls import path
from .views import lead_list, lead_detail, lead_create, lead_update, lead_delete, LeadListView, LeadDetailView, \
    LeadCreateView, LeadUpdateView, LeadDeleteView, AssignAgentView

app_name = "leads"

urlpatterns = [
    # path('', lead_list, name='lead-list'),
    path('', LeadListView.as_view(), name='lead-list'),
    # path('<int:pk>/', lead_detail, name='lead-detail'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    # path('<int:pk>/update/', lead_update, name='lead-update'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    # path('<int:pk>/delete/', lead_delete, name='lead-delete'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent'),
    # path('create/', lead_create, name='lead-create'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
]
