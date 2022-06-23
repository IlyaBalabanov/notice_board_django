from django.db import models
from user_auth.models import Account


class AccountNoticeRelation(models.Model):
    notice = models.ForeignKey('Notice', on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    is_in_favorite = models.BooleanField(default=False, null=True, blank=True)
    is_in_hidden = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f'{self.account.username} : {self.notice.title} [fav: {self.is_in_favorite}] [hid {self.is_in_hidden}]'


class Notice(models.Model):
    title = models.CharField(max_length=2000)
    text = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    relation = models.ManyToManyField('user_auth.Account', through='board.AccountNoticeRelation', related_name='relation')


    # def is_expired(self):
    #     return (datetime.today() - self.created.date()).days > 5

    def is_in_favorites(self, account):
        relation = AccountNoticeRelation.objects.filter(
            account=account,
            notice=self
        ).first()
        return relation.is_in_favorite

    def is_in_hidden(self, account):
        relation = AccountNoticeRelation.objects.filter(
            account=account,
            notice=self
        ).first()
        return relation.in_in_hidden

    def text_preview(self):
        return self.text[:100] + '...'

    def __str__(self):
        text = self.text
        if len(self.text) > 100:
            text = text[:100] + '...'
        return f'({self.author.username})[{self.title}] {text}'
