from django.contrib.postgres.search import SearchQuery
from django.db.models import Q
from django.db.models.query import QuerySet
from django.forms.fields import TypedMultipleChoiceField
from django_filters.filters import CharFilter, ChoiceFilter, OrderingFilter
from django_filters.filterset import FilterSet

from .models import (Term, Meaning)

class TermFilter(FilterSet):
    order_by = OrderingFilter(
        fields = (
            ('id', 'id'),
            ('wylie', 'wylie'),
            ('sa2ru1', 'sa2ru1'),
            ('sa2en1', 'sa2en1'),
            ('sa2ru2', 'sa2ru2'),
            ('sa2en2', 'sa2en2'),
            ('sa2ru3', 'sa2ru3'),
            ('sa2en3', 'sa2en3'),
            ('tibetan', 'tibetan'),
            ('sanscrit', 'sanscrit'),
        )
    )

    search = CharFilter('search', method='search_filter')

    def search_filter(self, queryset:QuerySet, name, value):
        if value == "":
            return queryset.none()
        qval = Q(wylie__istartswith=value) | Q(sa2ru1__istartswith=value) | Q(sa2en1__istartswith=value) | Q(sa2ru2__istartswith=value) | Q(sa2en2__istartswith=value) | Q(sa2ru3__istartswith=value) | Q(sa2en3__istartswith=value) | Q(tibetan__istartswith=value) | Q(sanscrit__istartswith=value)
            
        return queryset.filter(qval)

    class Meta:
        model = Term
        fields = {
            "wylie": ["icontains"],
            "sa2ru1": ["icontains"],
            "sa2en1": ["icontains"],
            "sa2ru2": ["icontains"],
            "sa2en2": ["icontains"],
            "sa2ru3": ["icontains"],
            "sa2en3": ["icontains"],
            "tibetan": ["icontains"],
            "sanscrit": ["icontains"],
        }


class MeaningFilter(FilterSet):
    order_by = OrderingFilter(
        fields = (
            ('id', 'id'),
            ('meaning', 'meaning'),
        )
    )

    search = CharFilter('search', method='search_filter')

    def search_filter(self, queryset:QuerySet, name, value):
        if value == "":
            return queryset.none()
#        qval = Q(meaning__icontains=value)
        qval = Q(meaning__istartswith=value)
        return queryset.filter(qval)

    class Meta:
        model = Meaning
        fields = {
            "meaning": ["icontains"],
        }

