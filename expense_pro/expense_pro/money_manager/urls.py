from django.urls import path
from money_manager import views


app_name='money_manager'
urlpatterns=[
    path("ind/",views.index,name='index'),
    path("analysis/",views.chart_view,name='chart_view'),
    path("add/",views.add,name='add'),
    path('view/<int:exp_id>/',views.view,name="view"),
    path('edit/<int:exp_id>/',views.edit,name='edit'),
    path('del/<int:exp_id>/',views.delete,name="delete"),
    path('action/<int:exp_id>/',views.handle_action,name="handle_action"),
]  