from adapters.photo_provider_adapter import PixabayAdapter, UnsplashAdapter
from ranking_algorithms.ranking_strategy import Top10Ranking, TrendingRanking, CustomRanking

class BromeliaPictInventory:
    def __init__(self, ranking_strategy, pixabay_api_key, unsplash_api_key):
        """
        Inicializa BromeliaPictInventory con la estrategia de ranking seleccionada
        y las claves de API para los proveedores de fotos.

        """
        # Adaptador de Pixabay usando la clave de API.
        self.pixabay_adapter = PixabayAdapter(pixabay_api_key)

        # Adaptador de Unsplash usando la clave de API.
        self.unsplash_adapter = UnsplashAdapter(unsplash_api_key)

        # Asigna la estrategia de ranking que se utilizara.
        self.ranking_strategy = ranking_strategy

    def get_top_photos(self, query):
        """
        Obtiene y rankea las mejores fotos de Pixabay y Unsplash basandose en la 
        estategia selecionada. 
        
        """

        # Obtiene las fotos de Pixabay usando el adaptador.
        pixabay_photos = self.pixabay_adapter.search_photos(query)

        # Obtiene las fotos de Unsplash usando el adaptador.
        unsplash_photos = self.unsplash_adapter.search_photos(query)

        # Combina las fotos de ambos proveedores.
        all_photos = pixabay_photos + unsplash_photos

        # Aplica la estrategia de ranking seleccionada para ordenar las fotos.
        return self.ranking_strategy.rank(all_photos)
