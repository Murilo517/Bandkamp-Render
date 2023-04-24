from rest_framework.views import Request, Response, status
from django.shortcuts import get_object_or_404


class CreateBaseView:
    def create(self, request: Request) -> Response:

        """
        Registro de usuários
        """
        serializer = self.view_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
    
class ListBaseView:
    def list(self, request: Request) -> Response:
        queryset = self.view_queryset.all()
        serializer = self.view_serializer(queryset,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
class RetrieveBaseView:
    def retrieve(self, request: Request,*args,**kwargs) -> Response:
        url_param = kwargs.get(self.url_params_name)
        obj = get_object_or_404(self.view_queryset,pk=url_param)
        serializer = self.view_serializer(obj)
        return Response(serializer.data,status.HTTP_200_OK)

class UpdateBaseView:
    def update(self, request: Request,*args,**kwargs) -> Response:
        url_param = kwargs.get(self.url_params_name)
        obj= get_object_or_404(self.view_queryset,pk=url_param)
        serializer = self.view_serializer(obj,request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status.HTTP_200_OK)

class EraseBaseView:
    def erase(self, request: Request,*args,**kwargs) -> Response:
        url_param = kwargs.get(self.url_params_name)
        obj = get_object_or_404(self.view_queryset,pk=url_param)
        self.check_object_permissions(request,self.view_queryset)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)