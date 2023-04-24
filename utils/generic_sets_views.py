from rest_framework.views import Request, Response
from utils.base_views import CreateBaseView, ListBaseView, RetrieveBaseView, UpdateBaseView, EraseBaseView
from utils.generic_views import GenericBaseView

class ListCreateGenericView(ListBaseView,CreateBaseView,GenericBaseView):
    def get(self, request: Request) -> Response:
        return super().list(request)

    def post(self, request: Request) -> Response:
        return super().create(request)


class RetrieveUpdateEraseView(RetrieveBaseView,UpdateBaseView,EraseBaseView,GenericBaseView):
    def get(self, request: Request,*args,**kwargs) -> Response:
        return super().retrieve(request,*args,**kwargs)
    def patch(self, request: Request,*args,**kwargs) -> Response:
        return super().update(request,*args,**kwargs)
    def delete(self, request: Request,*args,**kwargs) -> Response:
        return super().erase(request,*args,**kwargs)