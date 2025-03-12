from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class Userview(APIView):

    def get(self,request):

        all_user = UserData.objects.all()
        userdata=[]

        for user in all_user:
            single_data ={
                "id"       :user.id,
                "user_name":user.user_name,
                "user_pass":user.user_pass,
            }
            userdata.append(single_data)

        return Response(userdata)

    def post(self,request):

        new_user = UserData(user_name=request.data["user_name"],user_pass=request.data["user_pass"])
    
        new_user.save()
        return Response("Data saved")

class UserviewByid(APIView):
    
    def get(self,request,id):

        user = UserData.objects.get(id=id)
        
        single_data ={
                "id"       :user.id,
                "user_name":user.user_name,
                "user_pass":user.user_pass,
            }

        return Response(single_data)
    
    def patch(self,request,id):

        user = UserData.objects.filter(id=id)

        user.update(user_name=request.data["user_name"],user_pass=request.data["user_pass"])

        return Response("Updated")
    
    def delete(self,request,id):

        user = UserData.objects.get(id=id)
        
        user.delete()

        return Response("Deleted")
    
class ProductView(APIView):

    def get(self,request):

        all_product= Product.objects.all()

        product= ItemSerializers(all_product,many=True)

        return Response(product.data)
    
    def post(self,request):

        add_product = ItemSerializers(data=request.data)
        if add_product.is_valid():
            add_product.save()

        return Response("Save Data")

class ProductViewbyId(APIView):

    def get(self,request,id):

        all_product = Product.objects.get(id=id)

        product = ItemSerializers(all_product).data

        return Response(product)
    
    def patch(self,request,id):

        all_product = Product.objects.get(id=id)

        product =ItemSerializers(all_product,data=request.data,partial=True)
        if product.is_valid():
            print(product)
            product.save()
        return Response("Updated")

class CategoryViewbyId(APIView):
    def post(self,request):
        all_Category=Category_view(data=request.data) 
        if all_Category.is_valid():
            all_Category.save()
            return Response("saved")
        
class CategoryDelete(APIView):
    def delete(self,request,id):
        datadelete=Category.objects.get(id=id)
        datadelete.delete()
        return Response("deleted")