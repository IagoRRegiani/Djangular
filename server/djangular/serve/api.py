from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .models import *

## API de Serializers Normais ###############

class AdministradorAPI(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    
class PessoaAPI(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('Name',)

    def get_serializer_class(self):
        metodo = self.request.method
        if metodo == 'PUT' or metodo == 'POST':
            return PessoaSerializer
        else:
            return GetPessoaSerializer


class CursoAPI(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('Name',)
    serializer_class = CursoSerializer
    

class TurmaAPI(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('Name',)

    def get_serializer_class(self):
        metodo = self.request.method
        if metodo == 'PUT' or metodo == 'POST':
            return TurmaSerializer
        else:
            return GetTurmaSerializer
    
class AulaAPI(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('Assunto',)

    def get_serializer_class(self):
        metodo = self.request.method
        if metodo == 'PUT' or metodo == 'POST':
            return AulaSerializer
        else:
            return GetAulaSerializer

## API de Serializers Relacionais ###############

class ColaboradorTurmaAPI(viewsets.ModelViewSet):
    queryset = ColaboradorTurma.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('Description',)

    def get_serializer_class(self):
        metodo = self.request.method
        if metodo == 'PUT' or metodo == 'POST':
            return ColaboradorTurmaSerializer
        else:
            return GetColaboradorTurmaSerializer

class PessoaAulaAPI(viewsets.ModelViewSet):
    queryset = PessoaAula.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id',)

    def get_serializer_class(self):
        metodo = self.request.method
        if metodo == 'PUT' or metodo == 'POST':
            return PessoaAulaSerializer
        else:
            return GetPessoaAulaSerializer