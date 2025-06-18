from datetime import timedelta
from django.utils.timezone import now
from .models import Item

def expiry_notifications(request):
    if request.user.is_authenticated:
        today = now().date()
        warning_date = today + timedelta(days=90)
        expiring_items = Item.objects.filter(exp_date__lte=warning_date, exp_date__gte=today)
        return {'expiring_items': expiring_items, 'expiring_count': expiring_items.count()}
    return {}