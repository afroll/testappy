class Film:
    def __init__(self, _id, title, duration):
        self._id = _id
        self.title = title
        self.duration = duration
    def save(self):
        pass
    def update_title(self, new_title):
        pass
    def update_duration(self, new_duration):
        pass
    def delete(self):
        pass
f = Film(1, 'LOTR', 220)
f.save()
f.update_title()
f.update_duration()
f.delete()
