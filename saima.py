#1.Scenario: You have a list of user dictionaries, and you want to quickly filter out the users who are currently inactive.
users=[{"username":"alice","active": True},
       {"username":"bob","active": False},
       {"username":"charlie","active": True},
       {"username":"diana","active": False}]
active_users = list(filter(lambda user: user["active"],users))
print(active_users)
# 2. Sorting a List of Products by Price
# Scenario: You are building an e-commerce sorting feature and need to sort a list of products from cheapest to most expensive.

products=[
    {"name":"laptop","price":999.99},
    {"name":"mouse","price":25.50},
    {"name":"keyboard","price":75.00}]
sorted_products= sorted(products,key=lambda p: p["price"])
print(sorted_products)

# 3. Applying a Discount to Prices
# Scenario: A flash sale requires applying a 20% discount across an entire list of item prices.
prices =[100, 250,50,500]
discounted_prices=list(map(lambda price: price * 0.8,prices))
print(discounted_prices)