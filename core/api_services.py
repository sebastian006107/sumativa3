import requests
import time

# Caché simple
_cache = {
    'ofertas': None,
    'timestamp': 0
}
_CACHE_DURATION = 1800  # 30 minutos en segundos

def get_game_deals(limit=12):
    """
    Obtiene ofertas de juegos desde CheapShark API con caché simple
    """
    current_time = time.time()
    
    # Si el caché está vacío o ha expirado
    if _cache['ofertas'] is None or (current_time - _cache['timestamp']) > _CACHE_DURATION:
        url = f"https://www.cheapshark.com/api/1.0/deals?pageSize={limit}&sortBy=savings"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            _cache['ofertas'] = response.json()
            _cache['timestamp'] = current_time
        except Exception as e:
            print(f"Error al obtener ofertas: {e}")
            if _cache['ofertas'] is None:
                _cache['ofertas'] = []
    
    return _cache['ofertas']