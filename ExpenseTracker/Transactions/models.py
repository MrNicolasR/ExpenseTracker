# Import 
from django.db import models


# Category Choices
categoryChoices = (
    ('T', 'Transportation'),
    ('H', 'Housing'),
    ('F', 'Food'),
    ('M', 'Miscellaneous'),
)

# Transactions Model
class Transactions(models.Model):
    # Transaction Name
    name = models.CharField(max_length=100, null=False)
    # Transaction Merchant
    merchant = models.CharField(max_length=100, null=False)
    # Transaction Amount
    amount = models.FloatField(null=False)
    # Transaction Discription
    description = models.TextField(null=True)
    # Tansaction Date
    date = models.DateTimeField(auto_now=True)
    # Transaction Category 
    category = models.CharField(choices=categoryChoices,max_length=3, null=False)

    def __str__():
        return self.name + ' ' + self.amount.str()
        
