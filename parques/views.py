import os
import json
from django.shortcuts import render, get_object_or_404

# Load JSON data from the app's data directory
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'parques.json')
with open(DATA_PATH, 'r', encoding='utf-8') as f:
    PARQUES = json.load(f)


def home(request):
    # show a few featured parks
    featured = PARQUES[:3]
    return render(request, 'parques/home.html', {'featured': featured})


def parques_list(request):
    return render(request, 'parques/parques_list.html', {'parques': PARQUES})


def parque_detail(request, park_id):
    parque = next((p for p in PARQUES if p.get('id') == park_id), None)
    if not parque:
        # 404
        from django.http import Http404
        raise Http404('Parque no encontrado')
    return render(request, 'parques/parque_detail.html', {'parque': parque})


def actividades(request):
    actividades = [
        {'titulo': 'Trekking', 'descripcion': 'Rutas de trekking recomendadas en distintos parques.'},
        {'titulo': 'Avistamiento de aves', 'descripcion': 'Lugares y temporadas para observar aves nativas.'},
        {'titulo': 'Fotografía de naturaleza', 'descripcion': 'Consejos y miradores fotográficos.'},
    ]
    return render(request, 'parques/actividades.html', {'actividades': actividades})


def contacto(request):
    return render(request, 'parques/contacto.html')
