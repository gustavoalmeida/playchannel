from django.db.models import Manager

class MovieManager(Manager):

    def ordered_asc(self):
        all = self.all()
        return all.order_by('title')

    def ordered_desc(self):
        all = self.all()
        return all.order_by('-title')