from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer


@api_view(["GET"])
def get_people(request):
    queryset = Person.objects.all()
    serializer = PersonSerializer(queryset, many=True)
    content = {"people": serializer.data}

    return Response(content)
