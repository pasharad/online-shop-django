from django.db.models import Manager

class BaseManager(Manager):
    def get_all(cls):
        return cls.all()
    
    def get_one(cls, pk):
        return cls.get(pk=pk)
    
    