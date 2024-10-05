from rest_framework.generics import CreateAPIView
from .serializer import BlogAbstractUserSerializer
from .models import BlogAbstractUser





class BlogAbstractUserApiView(CreateAPIView):
    queryset = BlogAbstractUser.objects.all()
    serializer_class = BlogAbstractUserSerializer
    


    """
    because you can not user Abstract user in the queryset you have to create a model user
    
    """




 


