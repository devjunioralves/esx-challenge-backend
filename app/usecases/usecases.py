from ..repositories.repositories import UrlRepository

class CreateUrlUseCase:
    def __init__(self, repository: UrlRepository):
        self.repository = repository

    def execute(self, url):
        return self.repository.create(url)

class ListUrlsUseCase:
    def __init__(self, repository: UrlRepository):
        self.repository = repository

    def execute(self):
        return self.repository.get_all()
    
class RetrieveUrlUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, pk):
        return self.repository.get_by_id(pk)

class UpdateUrlUseCase:
    def __init__(self, repository: UrlRepository):
        self.repository = repository

    def execute(self, url_id, data):
        url_instance = self.repository.get_by_id(url_id)
        return self.repository.update(url_instance, data)

class DeleteUrlUseCase:
    def __init__(self, repository: UrlRepository):
        self.repository = repository

    def execute(self, url_id):
        url_instance = self.repository.get_by_id(url_id)
        self.repository.delete(url_instance)
