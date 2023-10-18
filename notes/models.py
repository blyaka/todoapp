from django.db import models
from django.urls import reverse
from accounts.models import CustomUser
import uuid

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    note_title = models.CharField('Заметка', max_length=200)
    note_text = models.TextField('Что сделать')
    pub_date = models.DateField('Дата создания', auto_now=True)
    do_before = models.DateField('Сделать до', blank=True, )
    pub_author = models.ForeignKey(CustomUser, verbose_name='Автор', on_delete=models.CASCADE, related_name='usernote')
    is_active = models.BooleanField('Сделано', default=False)


    class Meta:
        permissions = [('NoteOwner', 'Can see notes')]

    def __str__(self):
        return self.note_title

    def get_absolute_url(self):
        return reverse('note', args = [str(self.id)])


