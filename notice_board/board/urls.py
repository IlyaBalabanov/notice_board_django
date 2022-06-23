from django.conf.urls.static import static
from django.urls import path

from board.views import home, notice, create, Relation, favorites
from notice_board import settings

urlpatterns = [
    path('', home),
    path('notice/<int:notice_pk>/', notice),
    path('create', create),
    path('relation', Relation.as_view()),
    path('favorites', favorites),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

