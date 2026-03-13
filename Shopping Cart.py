#Shopping cart program of products, their prices and total bill
products=[]
prices=()
total=0

while True:
    product=input("Enter the product(q or Q to quit): ")
    if product.lower()=="q":
        break
    else:
        price=int(input("Enter it's price: "))
        products.append(product)
        prices= prices + (price,)

r=input("Do You want to remove any item/s (y/n): ")
while r=="y":
    name=input("Enter the product to remove: ")
    loc=products.index(name)
    products.remove(name)
    prices= prices[:loc] + prices[loc+1:]
    print("Product removed successfully")
    r=input("Do You want to remove any item/s (y/n): ")

n=len(products)
print("-----SHOPPING CART-----")
for i in range(0,n):
    print(f"{products[i]} - {prices[i]} Rs")
    total+=prices[i]

print("------------------------")
print(f"Total Price= {total} Rs")
    
    
    
        
