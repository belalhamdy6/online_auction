import django_filters
from .models import Job
class CarFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug', 'owner', 'image', 'descreption', 'published_at', 'mileage', 'name', 'engine', 'bid_on', 'color',
                   'image_e', 'image_d', 'image_c', 'image_b', 'image_a')