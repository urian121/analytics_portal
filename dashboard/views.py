from django.shortcuts import render

# Create your views here.
def home(request):
    # Creando una lista de 20 diccionarios con datos ficticios
    datos_dashboard = [
        {
            "fecha": f"2026-01-{cliente:02d}",
            "cliente": f"Cliente {cliente}",
            "metrica": "Ventas",
            "valor": 500 + cliente * 50,
        }
        # itera cada número de 1 a 20
        for cliente in range(1, 21)
    ]
    
    return render(request, "dashboard/home.html", {"datos_dashboard": datos_dashboard})