from django.core.checks import messages
from rest_framework import viewsets
from .models import TestDafiti
from .serializers import ProdutoSerializer
from django.shortcuts import render
import csv, io


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = TestDafiti.objects.all()
    serializer_class = ProdutoSerializer


def DafitiUpload(request):
    template_name = "api/upload.html"
    prompt = {
        'Ordem': 'produto, quantidade, valor'
    }

    if request.method == "GET":
        return render(request, template_name, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Esta file não é csv')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=';', quotechar='|'):
        product_id = column[0]
        produto = column[1]
        quantidade = int(column[2])
        valor = float(column[3].replace(',', '.'))
        _, created = TestDafiti.objects.update_or_create(
            product_id=product_id,
            produto=produto,
            quantidade=quantidade,
            valor=valor,
        )
    context = {}
    return render(request, template_name, context)