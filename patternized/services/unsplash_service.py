import requests
from models.photo import Photo

class UnsplashService:
    # URL base de la API de Unsplash.
    API_URL = "https://api.unsplash.com/"

    def search_photos(self, query, api_key):
        """
        Busqueda de fotos en la API de Unsplash utilizando un termino de busqueda.
        
        """
        # Realiza la solicitud GET a la API de Unsplash.
        response = requests.get(self.API_URL, params={"query": query, "client_id": api_key})
        
        # Convierte la respuesta JSON en un diccionario de Python.
        data = response.json()
        
        return [
            Photo(
                id=item["id"],
                url=item["urls"]["regular"],
                quality=self._calculate_quality(item) 
            )
            for item in data["results"]
        ]

    def _calculate_quality(self, photo_data):
        """
        Calcula la calidad de una foto basada en los datos proporcionados por la API de Unsplash.
        
        """
        # Suma el numero de likes y descargas para determinar la calidad de la foto.
        return photo_data["likes"] + photo_data["downloads"]
