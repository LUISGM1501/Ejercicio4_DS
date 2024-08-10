from abc import ABC, abstractmethod
from services.pixabay_service import PixabayService
from services.unsplash_service import UnsplashService

# Intefaz abstracta , que será utilizada por los adaptadores.
class PhotoProviderAdapter(ABC):
    @abstractmethod
    def search_photos(self, query: str):
        """
        Metodo abstracto para buscar fotos.
        Debe ser implementado por las clases adaptadoras segun sus apis.

        """
        pass


# Adaptador para la API de Pixabay.
class PixabayAdapter(PhotoProviderAdapter):
    def __init__(self, api_key):
        """
        Inicializa el adaptador de Pixabay con la clave de API y configura el servicio.
        
        """
        self.service = PixabayService() 
        self.api_key = api_key 

    def search_photos(self, query: str):
        """
        Bussqueda de fotos usando la API de Pixabay.
        
        """
        return self.service.search_photos(query, self.api_key)

# Adaptador para la API de Unsplash.
class UnsplashAdapter(PhotoProviderAdapter):
    def __init__(self, api_key):
        """
        Inicializa el adaptador de Unsplash con la clave de API y configura el servicio.
        
        """
        self.service = UnsplashService() 
        self.api_key = api_key  

    def search_photos(self, query: str):
        """
        Busqueda de fotos usando la API de Unsplash.
        
        """
        return self.service.search_photos(query, self.api_key)

