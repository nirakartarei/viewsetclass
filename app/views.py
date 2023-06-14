from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from app.models import *
from app.serializers import *
from rest_framework.response import Response
class productVS(ViewSet):
    def list(self,request):
        PQS=Product.objects.all()
        PS=productserializers(PQS,many=True)
        return Response (PS.data)
    def create(self,request):
        PS=productserializers(data=request.data)
        if PS.is_valid():
            PS.save()
            return Response( {'success':'data was successfully created'})
        else:
            return Response({'failed':'data is invalid'})
    def retrieve(self,request,pk):
        PQS=Product.objects.get(pk=pk)
        PSO=productserializers(PQS) 
        return Response(PSO.data) 
    def update(self,request,pk):
        PQS=Product.objects.get(pk=pk)
        PS=productserializers(PQS,data=request.data)
        if PS.is_valid():
            PS.save()
            return Response({'success':'data has been updated'})
        
    def partial_update(self,request,pk):
        PQS=Product.objects.get(pk=pk)
        PS=productserializers(PQS,data=request.data,partial=True)
        if PS.is_valid():
            PS.save()
            return Response({'success':'data has been updated'})
    def destroy(self,request,pk):
        PSQ=Product.objects.get(pk=pk)
        PSQ.delete()
        return Response ({'sucess':'data has been delected'})



  
