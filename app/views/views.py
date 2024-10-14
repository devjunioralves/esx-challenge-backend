from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..repositories.repositories import UrlRepository
from ..usecases.usecases import CreateUrlUseCase, ListUrlsUseCase, UpdateUrlUseCase, DeleteUrlUseCase, RetrieveUrlUseCase
from ..serializers.serializers import UrlSerializer

class UrlViewSet(viewsets.ModelViewSet):
    repository = UrlRepository()

    def create(self, request, *args, **kwargs):
        use_case = CreateUrlUseCase(self.repository)
        serializer = UrlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = use_case.execute(serializer.validated_data['url'])
        return Response(UrlSerializer(url).data, status=status.HTTP_201_CREATED)


    def list(self, request, *args, **kwargs):
        use_case = ListUrlsUseCase(self.repository)
        urls = use_case.execute()
        serializer = UrlSerializer(urls, many=True)
        return Response(serializer.data)

    
    def retrieve(self, request, pk=None):
        use_case = RetrieveUrlUseCase(self.repository)
        url = use_case.execute(pk)
        serializer = UrlSerializer(url)
        return Response(serializer.data)


    def update(self, request, pk=None):
        use_case = UpdateUrlUseCase(self.repository)
        serializer = UrlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = use_case.execute(pk, serializer.validated_data)
        return Response(UrlSerializer(url).data)


    def destroy(self, request, pk=None):
        use_case = DeleteUrlUseCase(self.repository)
        use_case.execute(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

