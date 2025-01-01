from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from ArtifactsApp.models import Artifact
from PeopleApp.models import Person
from VehiclesApp.models import Vehicle
from PeopleApp.serializers import PersonSerializer
from VehiclesApp.serializers.vehicles import VehicleSerializer


@api_view(["GET"])
def listing(request):
    queryset_titles = Person.objects.filter(title="Him")
    queryset_vehicles = Vehicle.objects.all()

    context = {
        "request": request,
    }

    # context used for parsing url field, if classes viewsets.ModelViewSet does this automatically
    vehicles_serializer = VehicleSerializer(
        queryset_vehicles, many=True, context=context
    )
    person_serializer = PersonSerializer(queryset_titles, many=True)

    result = {
        "doctors": person_serializer.data,
        "vehicles": vehicles_serializer.data,
    }

    return Response(result)


class TitlesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    def list(self, request):
        queryset_titles = Person.objects.filter(title="Him")
        person_serializer = PersonSerializer(queryset_titles, many=True)

        results = {
            "doctors": person_serializer.data,
        }

        return Response(results)


class MassDeleteArtifactsViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    @action(detail=False, methods=["delete"])
    def mass_delete(self, request, pk=None):
        for artifact_id in request.POST["ids"].split(","):
            Artifact.objects.get(id=artifact_id).delete()
        
        return Response()