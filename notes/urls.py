from django.urls import path
from notes import views
from notes.views import NoteViewSet, UserViewSet, CommentViewSet, CourseViewSet


note_list = NoteViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

note_detail = NoteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

course_list = CourseViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

course_detail = CourseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

urlpatterns = [
    path('notes/', note_list, name='note-list'),
    path('notes/<int:pk>/', note_detail, name='note-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('comments/', comment_list, name='comment-list'),
    path('comments/<int:pk>', comment_detail, name='comment-detail'),
    path('courses/', course_list, name='course-list'),
    path('courses/<int:pk>', course_detail, name='course-detail'),
]
