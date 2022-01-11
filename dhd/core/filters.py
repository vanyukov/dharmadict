from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.db.models import Q
from django.db.models.query import QuerySet
from django.forms.fields import TypedMultipleChoiceField
from django_filters.filters import CharFilter, ChoiceFilter, OrderingFilter
from django_filters.filterset import FilterSet

from .models import Term, Meaning


class TermFilter(FilterSet):
    order_by = OrderingFilter(
        fields=(
            ("id", "id"),
            ("wylie", "wylie"),
            ("sa2ru1", "sa2ru1"),
            ("sa2en1", "sa2en1"),
            ("sa2ru2", "sa2ru2"),
            ("sa2en2", "sa2en2"),
            ("sa2ru3", "sa2ru3"),
            ("sa2en3", "sa2en3"),
            ("tibetan", "tibetan"),
            ("sanscrit", "sanscrit"),
        )
    )

    search = CharFilter("search", method="search_filter")

    def search_filter(self, queryset: QuerySet, name, value):
        if value == "":
            return queryset.none()
        # qval = Q(wylie__istartswith=value) | Q(sa2ru1__istartswith=value) | Q(sa2en1__istartswith=value) | Q(sa2ru2__istartswith=value) | Q(sa2en2__istartswith=value) | Q(sa2ru3__istartswith=value) | Q(sa2en3__istartswith=value) | Q(tibetan__istartswith=value) | Q(sanscrit__istartswith=value)
        # qval = Q(wylie__search=value) | Q(sa2ru1__search=value) | Q(sa2en1__search=value) | Q(sa2ru2__search=value) | Q(sa2en2__search=value) | Q(sa2ru3__search=value) | Q(sa2en3__search=value) | Q(tibetan__search=value) | Q(sanscrit__search=value)
        vector = SearchVector(
            "wylie",
            "sa2ru1",
            "sa2en1",
            "sa2ru2",
            "sa2en2",
            "sa2ru3",
            "sa2en3",
            "tibetan",
            "sanscrit",
            config="english",
        )
        query = SearchQuery(value)
        return queryset.annotate(rank=SearchRank(vector, query)).order_by("-rank")

    class Meta:
        model = Term
        fields = {
            "wylie": ["search"],
            "sa2ru1": ["search"],
            "sa2en1": ["search"],
            "sa2ru2": ["search"],
            "sa2en2": ["search"],
            "sa2ru3": ["search"],
            "sa2en3": ["search"],
            "tibetan": ["search"],
            "sanscrit": ["search"],
        }


class MeaningFilter(FilterSet):
    order_by = OrderingFilter(fields=(("id", "id"), ("meaning", "meaning"),))

    search = CharFilter("search", method="search_filter")

    def search_filter(self, queryset: QuerySet, name, value):
        if value == "":
            return queryset.none()
        #        qval = Q(meaning__icontains=value)
        # qval = Q(meaning__istartswith=value)
        qval = Q(meaning__search=value)
        # vector = SearchVector("meaning", "comment", config="russian")
        # query = SearchQuery(value)
        return queryset.filter(qval)
        # return queryset.annotate(rank=SearchRank(vector, query)).order_by("-rank")

    class Meta:
        model = Meaning
        fields = {
            "meaning": ["search"],
            # "comment": ["search"],
            # "meaning": ["icontains"],
        }

