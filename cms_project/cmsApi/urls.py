from django.urls import include, path
from rest_framework import routers
from . import views
from .views import StudentViewSet,UserViewSet,ProfessorViewSet,AdminViewSet,CourseViewSet,SectionViewSet,AnnouncementViewSet,AssignmentViewSet,EnrollmentViewSet,StudentAssignmentViewSet
from rest_framework import renderers





#Binding ViewSets to URLs explicitly

student_list = StudentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

student_detail = StudentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

professor_list =ProfessorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

professor_detail =ProfessorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


student_highlight =StudentViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

professor_highlight =ProfessorViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

admin_list =AdminViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

admin_detail = AdminViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
admin_highlight = AdminViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

course_list =CourseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

course_detail =CourseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

course_highlight =CourseViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])



section_list =SectionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

section_detail = SectionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

section_highlight =SectionViewSet.as_view({
    'get': 'highlight'
},
 renderer_classes=[renderers.StaticHTMLRenderer])




announcement_list =AnnouncementViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

announcement_detail =AnnouncementViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

announcement_highlight =AnnouncementViewSet.as_view({
    'get': 'highlight'
},
 renderer_classes=[renderers.StaticHTMLRenderer])






assignment_list =AssignmentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

assignment_detail =AssignmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

assignment_highlight =AssignmentViewSet.as_view({
    'get': 'highlight'
},
 renderer_classes=[renderers.StaticHTMLRenderer])



enrollment_list =EnrollmentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

enrollment_detail =EnrollmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

enrollment_highlight =EnrollmentViewSet.as_view({
    'get': 'highlight'
},
 renderer_classes=[renderers.StaticHTMLRenderer])




assignment_list =AssignmentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

assignment_detail =AssignmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

assignment_highlight =AssignmentViewSet.as_view({
    'get': 'highlight'
},
 renderer_classes=[renderers.StaticHTMLRenderer])



studentAssignment_list =StudentAssignmentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

studentAssignment_detail =StudentAssignmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

studentAssignment_highlight =StudentAssignmentViewSet.as_view({
    'get': 'highlight'
},
 renderer_classes=[renderers.StaticHTMLRenderer])





user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


# Routers provide an easy way of automatically determining the URL conf
# Create a router and register our viewsets with it.

router = routers.DefaultRouter()


router.register(r'admin', views.AdminViewSet)

router.register(r'users', views.UserViewSet)


router.register(r'groups', views.GroupViewSet)


router.register(r'student', views.StudentViewSet)

router.register(r'professor', views.ProfessorViewSet)



router.register(r'course', views.CourseViewSet)

router.register(r'section', views.SectionViewSet)

router.register(r'announcement', views.AnnouncementViewSet)

router.register(r'assignment', views.AssignmentViewSet)

router.register(r'enrollment', views.EnrollmentViewSet)

router.register(r'studentAssignment', views.StudentAssignmentViewSet)




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# register the views with the URL conf as usual.
# The API URLs are now determined automatically by the router
urlpatterns = [

    path('', include(router.urls)),

    path('students/', student_list, name='student-list'),

    path('students/<int:pk>/', student_detail, name='student-detail'),
    
    path('professors/', professor_list, name='professor-list'),

    path('professors/<int:pk>/', professor_detail, name='professor-detail'),

    
    path('admin/', admin_list, name='user-list'),

    path('admin/<int:pk>/', admin_detail, name='user-detail'),


    path('course/', course_list, name='user-list'),

    path('course/<int:pk>/', course_detail, name='user-detail'),


     path('section/', section_list, name='user-list'),

    path('section/<int:pk>/', section_detail, name='user-detail'),


    path('announcement/', announcement_list, name='user-list'),

    path('announcement/<int:pk>/', announcement_detail, name='user-detail'),


    path('assignment/', assignment_list, name='user-list'),

    path('assignment/<int:pk>/', assignment_detail, name='user-detail'),


    path('enrollment/',enrollment_list, name='user-list'),

    path('enrollment/<int:pk>/', enrollment_detail, name='user-detail'),



    path('studentAssignment/',studentAssignment_list, name='user-list'),

    path('studentAssignment/<int:pk>/', studentAssignment_detail, name='user-detail'),


    path('users/', user_list, name='user-list'),

    path('users/<int:pk>/', user_detail, name='user-detail'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]