from django.contrib import admin
from django.urls import path, reverse
from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.utils.html import format_html
from django.middleware.csrf import get_token
from django.utils.safestring import mark_safe
from .models import Stock, StockMovement
from .services import apply_movement,InsufficientStockError

FORM_HTML = """
<html><body style="font-family:sans-serif;max-width:420px;margin:60px auto">
<h2>{title}</h2>
<p>{subtitle}</p>
<form method="post">
    <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
    <p><label>Quantity<br><input type="number" name="quantity" min="1" required autofocus></label></p>
    {error}
    <button type="submit">{button_label}</button>
    <a href="{cancel_url}" style="margin-left:10px">Cancel</a>
</form>
</body></html>
"""

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("variant", "quantity", "reorder_level", "location", "adjust_links")
    readonly_fields = ("variant", "quantity")

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj = None):
        return False
    
    def adjust_links(self, obj):
        return format_html(
            '<a href="{}">Receive</a> &nbsp;|&nbsp; <a href="{}">Issue</a>',
            f'{obj.pk}/receive/', f'{obj.pk}/issue/',
        )
    adjust_links.short_description = "Adjust Stock"

    def get_urls(self):
        custom = [
            path("<int:pk>/receive/", self.admin_site.admin_view(self.receive_view)),
            path("<int:pk>/issue/", self.admin_site.admin_view(self.issue_view))
        ]
        return custom + super().get_urls()

    def receive_view(self,request,pk):
        return self._adjust(request,pk, direction=1, title="Receive Stock", button_label="Receive")

    def issue_view(self, request,pk):
        return self._adjust(request, pk, direction=-1, title="Issue Stock",button_label="Issue")

    def _adjust(self,request,pk,direction, title,button_label):
        stock = get_object_or_404(Stock, pk=pk)
        cancel_url = reverse("admin:inventory_stock_changelist")
        error = ""

        if request.method == "POST":
            quantity = int(request.POST.get("quantity",0))
            note = request.POST.get("note","")
            try:
                apply_movement(
                    variant=stock.variant,
                    delta=quantity*direction,
                    movement_type=StockMovement.Type.IN if direction >0 else StockMovement.Type.OUT,
                    reason=StockMovement.Reason.MANUAL if direction >0 else StockMovement.Reason.DAMAGE,
                    user=request.user,
                    note=note,
                )
                self.message_user(request, f"{title}: {quantity} units on {stock.variant.sku}.")
                return redirect(cancel_url)
            except InsufficientStockError as exc:
                error = f"<p style='color:red'>{exc}</p>"

        html = FORM_HTML.format(
            title=title,
            subtitle=f"{stock.variant.sku} - currently {stock.quantity} on hand",
            csrf_token=get_token(request),
            error=error,
            button_label=button_label,
            cancel_url=cancel_url,
        )
        return HttpResponse(html)

@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ("created_at", "variant", "movement_type", "reason", "quantity", "balance_after","reference")

    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj = None):
        return False
    def has_delete_permission(self, request, obj = None):
        return False