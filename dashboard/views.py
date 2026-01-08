from django.shortcuts import render

# Create your views here.
def home(request):
    # Creando una lista de 20 diccionarios con datos ficticios
    datos_dashboard = [
        {
            "fecha": f"2026-01-{i:02d}",
            "cliente": f"Cliente {i}",
            "metrica": "Ventas",
            "valor": 500 + i * 50,
        }
        # itera cada número de 1 a 20
        for i in range(1, 21)
    ]
    return render(request, "dashboard/home.html", {"datos_dashboard": datos_dashboard})