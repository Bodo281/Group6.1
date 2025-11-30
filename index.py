sales = [
    {"branch": "Nairobi", "item": "Laptop", "category": "Electronics",
     "price": 780, "quantity": 4, "discount": 0.05, "date": "2025-01-03"},

    {"branch": "Nairobi", "item": "Phone", "category": "Electronics",
     "price": 520, "quantity": 6, "discount": 0.10, "date": "2025-01-03"},

    {"branch": "Mombasa", "item": "Headphones", "category": "Accessories",
     "price": 150, "quantity": 10, "discount": 0.00, "date": "2025-01-04"},

    {"branch": "Nakuru", "item": "Laptop", "category": "Electronics",
     "price": 780, "quantity": 2, "discount": 0.00, "date": "2025-01-04"},

    {"branch": "Nairobi", "item": "Tablet", "category": "Electronics",
     "price": 310, "quantity": 3, "discount": 0.10, "date": "2025-01-05"},

    {"branch": "Mombasa", "item": "Phone", "category": "Electronics",
     "price": 520, "quantity": 4, "discount": 0.00, "date": "2025-01-05"},

    {"branch": "Nakuru", "item": "Keyboard", "category": "Accessories",
     "price": 80, "quantity": 12, "discount": 0.15, "date": "2025-01-05"},

    {"branch": "Nairobi", "item": "Monitor", "category": "Electronics",
     "price": 260, "quantity": 5, "discount": 0.05, "date": "2025-01-06"},

    {"branch": "Mombasa", "item": "Tablet", "category": "Electronics",
     "price": 310, "quantity": 2, "discount": 0.00, "date": "2025-01-06"},
]

# Extracting unique items sold across all branches

unique_items = list({sale['item'] for sale in sales})
print(unique_items)

# Compute total revenue per item

item_net_revenue = {item: sum((sale["price"]*sale["quantity"])*(1 - sale["discount"]) for sale in sales if sale["item"] == item)for item in unique_items}
print(item_net_revenue)

# Identify high performing items

top_items = [item for item, item_net_revenue in item_net_revenue.items() if item_net_revenue > 2000]
print(top_items)

#Filter sales for high performing items

filtered_sales = [sale for sale in sales if sale["item"] in top_items]
print(filtered_sales)

# Compute total quantity sold per branch

branch_quantities = {
    branch : sum(sale["quantity"] for sale in sales if sale["branch"] == branch)
    for branch in {sale["branch"] for sale in filtered_sales}
 }

#Determine the Most Successful Branch, returning branch name

highest_total_quantity = max(branch_quantities, key = branch_quantities.get)
print(highest_total_quantity)