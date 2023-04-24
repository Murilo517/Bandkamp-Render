from rest_framework.views import APIView, Request, Response
from .base_views import CreateBaseView,ListBaseView,RetrieveBaseView,UpdateBaseView,EraseBaseView


class GenericBaseView(APIView):
    view_queryset = None
    view_serializer = None
    url_params_name = 'pk'

class CreateGenericView(CreateBaseView,GenericBaseView):
    def post(self, request: Request) -> Response:
        return super().create(request)

class ListGenericView(ListBaseView,GenericBaseView):
    def get(self, request: Request) -> Response:
        return super().list(request)
    
class RetrieveGenericView(RetrieveBaseView,GenericBaseView):
    def get(self, request: Request,*args,**kwargs) -> Response:
        return super().retrieve(request,*args,**kwargs)

class UpdateGenericView(UpdateBaseView,GenericBaseView):
    def patch(self, request: Request,*args,**kwargs) -> Response:
        return super().update(request,*args,**kwargs)
    
class EraseGenericView(EraseBaseView,GenericBaseView):
    def delete(self, request: Request,*args,**kwargs) -> Response:
        return super().erase(request,*args,**kwargs)