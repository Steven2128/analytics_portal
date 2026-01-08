# Django
from django.shortcuts import render
from django.views import View

class DashboardView(View):
    def get(self, request):
        data = [
            {
                "fecha": "2026-01-07",
                "cliente": "Helena Gomez",
                "metrica": "Ventas",
                "valor": 120
            },
            {
                "fecha": "2024-02-21",
                "cliente": "Pablo Alvarez",
                "metrica": "Clientes",
                "valor": 90
            },
            {
                "fecha": "2026-02-20",
                "cliente": "Sandra Muñoz",
                "metrica": "Ingresos",
                "valor": 437
            },
            {
                "fecha": "2021-12-12",
                "cliente": "Edgar Morales",
                "metrica": "Pedidos",
                "valor": 83782
            },
            {
                "fecha": "203-06-01",
                "cliente": "Daniel Ballesteros",
                "metrica": "Costos",
                "valor": 2832
            }
        ]

        return render(request, 'dashboard/dashboard.html', {
            "titulo": "Dashboard",
            "data": data
        })
