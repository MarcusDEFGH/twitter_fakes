from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .serializers import TagSerializer
from tags.models import Tag


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    filter_backends = (SearchFilter,)

    def get_queryset(self):
        queryset = Tag.objects.filter(is_working=True)
        filter_args = ['name', 'is_active']
        query = {}

        for arg in filter_args:
            value = self.request.query_params.get(arg, None)
            if value is not None:
                query[arg] = value

        return queryset.filter(**query)

    def list(self, request, *args, **kwargs):
        return super(TagViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(TagViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(TagViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(TagViewSet, self).retrieve(request,
                                                *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(TagViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(TagViewSet, self).partial_update(request,
                                                      *args, **kwargs)
