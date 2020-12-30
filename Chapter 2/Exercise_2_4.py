"""Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies?"""

bookCost = 24.95
TotalBooks = 60.0

def cost(TotalBooks):
   bulkBookCost = ((bookCost * 0.60) * TotalBooks)
   shippingCost = (3.0 + (0.75 * (TotalBooks - 1)))
   totalCost = bulkBookCost + shippingCost
   print('The total cost is: $', totalCost)

cost(TotalBooks)
