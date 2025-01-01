from rest_framework.decorators import api_view
from rest_framework.response import Response

from VehiclesApp.models import Tool
from VehiclesApp.serializers.tools import ToolSerializer


@api_view(["GET"])
def get_tools(request):
    tools = [
        Tool("hammer", "Mastercraft"),
        Tool("wrench", "Husky"),
    ]
    serializer = ToolSerializer(tools, many=True)
    content = {"tools": serializer.data}

    return Response(content)
