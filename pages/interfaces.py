from abc import ABC, abstractmethod
from django.http import HttpRequest

class ImageStorage(ABC):
    @abstractmethod
    def store(self, request: HttpRequest):
        """Debe guardar la imagen y devolver la URL pública."""
        pass
