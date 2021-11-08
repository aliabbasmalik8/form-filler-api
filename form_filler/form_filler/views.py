from io import BytesIO

from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.

from rest_framework import views
from django.http import HttpResponse

from .serializers import RequestSerializer


class ExampleViewSet(views.APIView):

    def post(self, *args, **kwargs):
        serializer = RequestSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        ctx = serializer.validated_data
        template = get_template('temp.html')
        html = template.render(ctx)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=filled-form.pdf'
        pisa.CreatePDF(html, dest=response)
        return response
