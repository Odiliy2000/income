from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('outcome', 'Outcome'),
    )

    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - ${self.amount} on {self.date.strftime('%Y-%m-%d')}"
