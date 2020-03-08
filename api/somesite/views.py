from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from api.somesite.serializers import *
from app.models import *
from django.http.response import *
from rest_framework.decorators import api_view
from allauth.account.views import ConfirmEmailView, confirm_email
from rest_framework.mixins import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

#class PostShortList(APIView):
#    permission_classes = [permissions.AllowAny],
#    def get(self,request, format=None):
#        post=Post.objects.all()
#        serializer=PostShortSerializer(post, many=False)
#        return (data=serializer.data)

class PostShortList(generics.ListAPIView):
    """Короткая инфа по посту для персика"""
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostShortSerializer

class CatList(generics.ListAPIView):
    """Список категорий"""
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class TagList(generics.ListAPIView):
    """Список тегов"""
    permission_classes = [permissions.AllowAny]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostList(generics.ListAPIView):
    """Список постов"""
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class CommentList(generics.ListAPIView):
    """Список комментов"""
    permission_classes = [permissions.AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CreatePost(generics.CreateAPIView):
    """Создание поста"""
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer

"""@api_view (['DELETE', 'POST'])
def delete(request, pk):
        try:
            getpk = DeletePostSerializer(data=request.data) # для post метода
            post=Post.objects.get(pk=pk) #для delete метода
        except:
            return  HttpResponse(status=404)
        if request.method == 'POST':
            post=Post.objects.get(pk=getpk)
            post.delete()
            return HttpResponse(status=204)
        elif request.method =='DELETE':
            post.delete()
            return HttpResponse(status=204)"""


class DeletePost(generics.ListAPIView):
#    http_method_names = ['DELETE']
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = DeletePostSerializer
    def get(self, request, id):
        try:
            post = Post.objects.get(pk=id)
            post.delete()
            return HttpResponse(status=204)
        except:
            return HttpResponse(status=404)
    def delete(self, request, id):
        try:
            post = Post.objects.get(pk=id)
            post.delete()
            return HttpResponse(status=204)
        except:
            return HttpResponse(status=404)
    #def post(self, request, id=None):
     #   serializer = DeletePost(data=request.data)


class UpdatePost(generics.UpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.defer('created_date')
    serializer_class = UpdatePostSerializer
    lookup_field = 'id'
    edit_date=timezone.now()

"""class PostsView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    def put(self, response):
        queryset= Post.objects.defer('created_date')
        serializer=UpdatePostSerializer(queryset, many=True)
        lookup_field = 'id'
        if serializer.is_valid:
            serializer.save()
        return Response(serializer.data)
    def post(self, request):
        serializer=CreatePostSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
            return Response(status=201)
        except:
            return Response(status=404)
    def patch(self, request, id):
        queryset = Post.objects.defer('created_date')
        serializer_class = UpdatePostSerializer
        lookup_field = 'id'"""


"""class PostsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get(self, request, *args, **kwargs):
        queryset=Post.objects.all()
        serializer= PostSerializer(queryset, many=True)
        return Response(serializer.data)"""


class PostsView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = TestCreatePostSerializer

class Testposts(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.defer('created_date')
    serializer_class = UpdatePostSerializer
    lookup_field = 'id'

    def post(self, request, id):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    """from rest.mixins.py
    def perform_create(self, serializer):
        serializer.save()
    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
    def get(request, *args, **kwargs):
        return ListModelMixin.list(request, *args, **kwargs)

    def post(request, *args, **kwargs):
        return CreateModelMixin.create(request, *args, **kwargs)"""


"""class FavoritePost(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = FavoritePost.allobjects.all()
    serializer_class = FavoritePostSerializer
    lookup_field = 'users_id'
    def get(self,request, users_id):
        posts = FavoritePost.allobjects.filter(users_id=users_id)
        serializer = FavoritePostSerializer(posts, many=True)
        return Response(serializer.data)"""


class FavoritePostById(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = FavoritePost.allobjects.all()
    serializer_class = FavoritePostListSerializer
    def get(self, request):
        user=request.user.pk
        posts = FavoritePost.allobjects.filter(users_id=user)
        serializer = FavoritePostListSerializer(posts, many=True)
        return Response(serializer.data)
    def post(self, request):
        user = request.user.pk
        dat=request.data
        print(dat)
        posts = FavoritePost.allobjects.filter(users_id=user)
        serializer = FavoritePostListSerializer(data=request.data)
        #print(serializer)
        """При передаче несуществующего id в posts вернётся 201, необходимо реализовать
        проверку каждого переданного значения. Временно контроль их на фронте"""
        if serializer.is_valid():
            serializer.save(users_id=user)
        return Response(status=201)




















