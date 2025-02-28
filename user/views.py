from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

items=["This is first value"]
@api_view(['GET','POST'])
def item_list(request):
    if request.method == 'GET':
        return Response({'items':items})
    # return Response({'message':'Data is created'},status=201)

    if request.method == 'POST':
        data=request.data
        items.append(data)
        return Response({'message':'Data is created',"items":items},status=201)
    

@api_view(['GET','POST'])
def user_auth(request):
   if request.method =='GET':
    try:
        user_objet=User.objects.all()
        serializer=UserSerializer(user_objet,many=True)
        return Response({'data':serializer.data},status=200)
    except Exception as e:
        return Response({'message':'Data not found'},status=404)
    
    
   if request.method == 'POST':
        data=request.data
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data is created'},status=201)
        
        else:
            return Response(serializer.errors,status=400)
    



    
    