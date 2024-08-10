from abc import ABC, abstractmethod

# Interfaz abstract RankingStrategy, que se usara en los tipos de Ranking.
class RankingStrategy(ABC):
    @abstractmethod
    def rank(self, photos):
        """
        Metodo para ordenar una lista de fotos segun algun criterio.
        """
        pass

# Top10Ranking que selecciona las 10 mejores fotos segun calidad.
class Top10Ranking(RankingStrategy):
    def rank(self, photos):
        """
        Ordena las fotos por calidad en orden descendente y selecciona las 10 mejores.

        """
        return sorted(photos, key=lambda p: p.quality, reverse=True)[:10]

# TrendingRanking que selecciona las 10 mejores fotos basadas en su tendencia.
class TrendingRanking(RankingStrategy):
    def rank(self, photos):
        """
        Ordena las fotos por tendencia en orden descendente y selecciona las 10 mejores.

        """
        return sorted(photos, key=lambda p: p.trending_score, reverse=True)[:10]

# CustomRanking que permite al usuario definir su propio critirio.
class CustomRanking(RankingStrategy):
    def __init__(self, custom_criteria):
        """
        Inicializa la estrategia CustomRanking con un criterio de ranking personalizado.

        """
        self.custom_criteria = custom_criteria  # Almacena el criterio personalizado proporcionado por el usuario.

    def rank(self, photos):
        """
        Ordena las fotos utilizando el criterio personalizado proporcionado.

        """
        return sorted(photos, key=lambda p: self.custom_criteria(p), reverse=True)[:10]
