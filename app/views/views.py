from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from ..repositories.repositories import UrlRepository
from ..usecases.usecases import CreateUrlUseCase, ListUrlsUseCase, UpdateUrlUseCase, DeleteUrlUseCase, RetrieveUrlUseCase
from ..serializers.serializers import UrlSerializer

class UrlViewSet(viewsets.ModelViewSet):
    repository = UrlRepository()

    def create(self, request, *args, **kwargs):
        try:
            use_case = CreateUrlUseCase(self.repository)
            serializer = UrlSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            url = use_case.execute(serializer.validated_data['url'])
            return Response(UrlSerializer(url).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        try:
            use_case = ListUrlsUseCase(self.repository)
            urls = use_case.execute()
            serializer = UrlSerializer(urls, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            use_case = RetrieveUrlUseCase(self.repository)
            url = use_case.execute(pk)
            if not url:
                raise NotFound(detail="URL not found")
            serializer = UrlSerializer(url)
            return Response(serializer.data)
        except NotFound as e:
            return Response({'detail': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            use_case = UpdateUrlUseCase(self.repository)
            serializer = UrlSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            url = use_case.execute(pk, serializer.validated_data)
            if not url:
                raise NotFound(detail="URL not found for update")
            return Response(UrlSerializer(url).data)
        except NotFound as e:
            return Response({'detail': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            use_case = DeleteUrlUseCase(self.repository)
            if not use_case.execute(pk):
                raise NotFound(detail="URL not found for deletion")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotFound as e:
            return Response({'detail': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
