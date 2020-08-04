from django.shortcuts import render


from django.contrib.auth.models import User, Group
from cms_application.models import Student,Professor,Admin,Course,Section,Announcement,Assignment, Enrollment,StudentAssignment
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import StudentSerializer,ProfessorSerializer,UserSerializer, GroupSerializer,AdminSerializer,CourseSerializer 
from rest_framework import generics
import json

# Create your views here.


# ViewSets define the view behavior
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet,generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, format=None):
        body = json.loads(request.body)
        serializer =StudentSerializer(data=body)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



    def put(self, request, *args, **kwargs):
        body=json.loads(request.body)
        user = Student.objects.get(username = request.user.username)
        serializer = serializers.StudentSerializer(instance=user, data=body)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def delete(self, request, *args, **kwargs):
        student= Student.objects.get(username = request.user.username)
        student.is_active = False
        student.save()
        return Response("admin successfully deleted", status=status.HTTP_202_ACCEPTED)   



class ProfessorViewSet(viewsets.ModelViewSet,generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset =Professor.objects.all()
    serializer_class =ProfessorSerializer

    def post(self, request, format=None):
        body = json.loads(request.body)
        serializer =Professor.Serializer(data=body)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def put(self, request, *args, **kwargs):
        body=json.loads(request.body)
        user = Professor.objects.get(username = request.user.username)
        serializer =Professor.Serializer(instance=user, data=body)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  


    def delete(self, request, *args, **kwargs):
        professor= Professor.objects.get(username = request.user.username)
        professor.is_active = False
        professor.save()
        return Response("admin successfully deleted", status=status.HTTP_202_ACCEPTED)



   
class AdminViewSet(viewsets.ModelViewSet,generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset =Admin.objects.all()
    serializer_class =AdminSerializer     

    
    def post(self, request, format=None):
        body = json.loads(request.body)
        serializer =Admin.Serializer(data=body)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    def put(self, request, *args, **kwargs):
        body=json.loads(request.body)
        user = Admin.objects.get(username = request.user.username)
        serializer =Admin.Serializer(instance=user, data=body)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def delete(self, request, *args, **kwargs):
        admin= Admin.objects.get(username = request.user.username)
        admin.is_active = False
        admin.save()
        return Response("admin successfully deleted", status=status.HTTP_202_ACCEPTED)    



class CourseViewSet(viewsets.ModelViewSet,generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset =Course.objects.all()
    serializer_class =CourseSerializer        

    def post(self, request, format=None):
        body = json.loads(request.body)
        serializer =Course.Serializer(data=body)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

    def put(self, request, *args, **kwargs):
        body=json.loads(request.body)
        user = Course.objects.get(username = request.user.username)
        serializer =Course.Serializer(instance=user, data=body)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def delete(self, request, *args, **kwargs):
        course= Course.objects.get(username = request.user.username)
        course.is_active = False
        course.save()
        return Response("course successfully deleted", status=status.HTTP_202_ACCEPTED) 
   