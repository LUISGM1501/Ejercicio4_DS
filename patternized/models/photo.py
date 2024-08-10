# Modelos de las fotos
class Photo:
    def __init__(self, id, url, quality=0, trending_score=0):
        self.id = id
        self.url = url
        self.quality = quality
        self.trending_score = trending_score

    def __repr__(self):
        return f"Photo(id={self.id}, url={self.url}, quality={self.quality}, trending_score={self.trending_score})"
