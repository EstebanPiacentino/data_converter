from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.serializers import *
from django.utils import timezone
from django.conf import settings
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
import json

# Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

# Forms
from django.shortcuts import render
from django.core.files.base import ContentFile
import requests
from io import BytesIO, StringIO
import pandas as pd
from django.core.files import File


class ConvertData(APIView):

    #authentication_classes = [SessionAuthentication]
    #permission_classes = [IsAuthenticated] 

    def post(self, request):

        try:
            myfile = request.FILES['myfile']

        except:
            return render(request, 'not_valid.html')

        new_file = EventLog()
        new_file.spss_file.save('spss_file.sav', File(BytesIO(myfile.read())), save=True)
        new_file.save()

        print(new_file.spss_file.path)
        df = pd.read_spss(new_file.spss_file.path)

        new_file.delete()

        # Excel (Way too slow)

        #output = BytesIO()
        #print('excel writer')
        #writer = pd.ExcelWriter(output, engine='xlsxwriter')
        #print('to excel')
        #df.to_excel(writer, sheet_name='Data', encoding='utf-8', index=False)
        #print('save')
        #writer.save()

        #response = HttpResponse(output.getvalue(), content_type='application/vnd.ms-excel')
        #response['Content-Disposition'] = 'attachment; filename="spss_to_excel.xlsx"'

        # CSV

        output = StringIO()
        print('excel writer')
        print('to excel')
        df.to_csv(output, encoding='utf-8', index=False)
        response = HttpResponse(output.getvalue(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="spss_to_csv.csv"'

        return response

    def get(self, request):
        return render(request, 'upload.html')
