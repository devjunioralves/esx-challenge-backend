from ..models.models import Url

class UrlRepository:
    def create(self, url):
        return Url.objects.create(url=url)

    def get_all(self):
        return Url.objects.all()

    def get_by_id(self, url_id):
        return Url.objects.get(id=url_id)

    def update(self, url_instance, data):
        url_instance.url = data.get('url', url_instance.url)
        url_instance.save()
        return url_instance

    def delete(self, url_instance):
        url_instance.delete()
