from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .utils import current_npv
from .serializer import NPVSerializer


class NPVAPIView(APIView):

    serializer_class = NPVSerializer

    def get(self, request):
        npv = current_npv()
        year = 2050
        return Response({'npv': npv, 'year': year})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        npv = 0
        rate = 0.2
        year = 2050
        if serializer.is_valid():
            rate = serializer.validated_data.get('rate')
            year = serializer.validated_data.get('year')
            npv = current_npv(rate, year)
            return Response({'npv': npv, 'year': year, 'rate': rate})
        else:
            return Response({'message': '', 'error': serializer.errors}, status=HTTP_400_BAD_REQUEST)
