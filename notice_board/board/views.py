import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Prefetch
from django.db.models import Q, Value, BooleanField, Case, When

from board.forms import NoticeForm
from board.models import Notice, AccountNoticeRelation
from django.views import View

from user_auth.models import Account


# TODO: auth required decorator
def home(request):
    context = {}
    if request.user.is_authenticated:
        account = request.user

        current_house = Q(
            author__address__city=account.address.city,
            author__address__population_centers=account.address.population_centers,
            author__address__street=account.address.street,
            author__address__house=account.address.house,
            author__address__building=account.address.building,
        )

        hidden = Q(
            accountnoticerelation__account=account,
            accountnoticerelation__is_in_hidden=True,
        )

        favorite = Q(
            accountnoticerelation__account=account,
            accountnoticerelation__is_in_favorite=True,
        )
        notices_set = (
            Notice
                .objects
                .select_related('author__address')
                .annotate(
                is_favorite=Case(
                    When(
                        favorite, then=Value(True, output_field=BooleanField(null=True)))
                ),
                is_hidden=Case(
                    When(
                        hidden, then=Value(True, output_field=BooleanField(null=True)))
                )
            )
                .filter(current_house)
        )

        context = {
            'notices': notices_set,
            'full': False
        }
    return render(request, 'board/home.html', context)


def notice(request, notice_pk):
    # TODO: get or 404
    context = {
        'notice': Notice.objects.get(pk=notice_pk),
        'full': True
    }
    return render(request, 'board/notice.html', context)


def create(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            # TODO: ???
            return redirect('/')
        else:
            return render(request, 'layouts/one_form.html', {'form': form})
    context = {
        'form': NoticeForm(),
    }
    return render(request, 'layouts/one_form.html', context)


def favorites(request):
    account = request.user

    hidden = Q(
        accountnoticerelation__account=account,
        accountnoticerelation__is_in_hidden=True,
    )

    favorite = Q(
        accountnoticerelation__account=account,
        accountnoticerelation__is_in_favorite=True,
    )
    notices_set = (
        Notice
            .objects
            .select_related('author__address')
            .annotate(
            is_favorite=Case(
                When(
                    favorite, then=Value(True, output_field=BooleanField(null=True)))
            ),
            is_hidden=Case(
                When(
                    hidden, then=Value(True, output_field=BooleanField(null=True)))
            )
        ).filter(favorite)
    )
    context = {'notices': notices_set}
    return render(request, 'board/home.html', context)


class Relation(View):
    class RelationMethods:
        Hide = 'hide'
        Favorite = 'favorite'

    def post(self, request):
        data = json.loads(request.body)

        method = data.get('method')
        pk = data.get('pk')

        notice = Notice.objects.get(pk=pk)
        account = request.user

        relation, _ = AccountNoticeRelation.objects.get_or_create(
            account=account,
            notice=notice
        )

        if method == self.RelationMethods.Hide:
            relation.is_in_hidden = True
        elif method == self.RelationMethods.Favorite:
            relation.is_in_favorite = True

        relation.save()

        return HttpResponse('check')
