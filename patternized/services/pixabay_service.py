import requests
from models.photo import Photo

class PixabayService:
    # URL base de la API de Pixabay.
    API_URL = "https://pixabay.com/api/"

    def search_photos(self, query, api_key):
        """
        Busqueda de fotos en la API de Pixabay utilizando un termino de busqueda.
        
        :param query: Termino de busqueda para encontrar fotos relevantes en Pixabay.
        """
        # Realiza la solicitud GET a la API.
        response = requests.get(self.API_URL, params={"q": query, "key": api_key})
        
        # Convierte la respuesta JSON en un diccionario de Python.
        data = response.json()
        
        return [
            Photo(
                id=item["id"],
                url=item["largeImageURL"],
                quality=self._calculate_quality(item)
            )
            for item in data["hits"]
        ]

    def _calculate_quality(self, photo_data):
        """
        Calcula la calidad de una foto basada en los datos proporcionados por la API de Pixabay.
        
        """
        # Suma el numero de likes y favoritos para determinar la calidad.
        return photo_data["likes"] + photo_data["favorites"]
