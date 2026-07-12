#inventory_manager_system
#File handling: using python to work with files.It includes create files,open files,write into files, read from files,update the file content,close the file,handle the file errors 
import re
import logging 

# product code FORMAT = PROD-001 , prod-123,PROD123
#pattern=r"(07\d{8}|+2547\d{8})
logging.basicConfig(
	filename="inventory.log",
	level=logging.INFO,
	format="%(levelname)s:%(message)s"
)
# INFO:Inventory saved to file
# ERROR: Inventory file not found 
inventory={
	"rice":{
		"quantity":20,
		"price":1500
	},
	"milk":{
		"quantity":15,
		"price":1200
	},
	"sugar":{
		"quantity":10,
		"price":1800
	}
}
# print(inventory)
print("Current Inventory")
print("--------------------")
#add a new product
def get_valid_product_code():
	while True:
		product_code=input("Enter the product code. Example PROD-123:")
		product_code= product_code.strip().upper()#prod-123
		pattern=r"PROD-\d{3}"
		if re.fullmatch(pattern,product_code):
			return product_code	
		print("Invalid product code ")
product_code=get_valid_product_code()

def get_valid_supplier_email():
	while True:
		email=input("Enter the supplier email:")
		email=email.strip().lower()
		pattern=r"[a-zA-Z0-9._%]+@[a-zA-Z0-9.-]+\.[a-zA]{2,}"
		if re.fullmatch(pattern,email):
			return email
		print("Invalid email supplier ")
		
while True:
	product_name=input("Enter the product name: ")
	product_name=product_name.strip().lower()
	if product_name!="":
		break 
	print("Product name cannot be empty")
print("Product name accepted")

quantity=input("Enter quantity: ")
if quantity.isdigit():
	quantity_input=int(quantity)
	print(f"quantity accepted:{quantity_input}")
else:
	print("Quantity must be a number")
	exit()

while True:
	price=input("Enter price:")
	try:
		price_input=float(price)
		if price_input>0:
			break
		else:
			print("Price must be greater than 0")
	except ValueError:
		print("Price must be a valid number")
print("Price accepted")
email=get_valid_supplier_email()

#add the new product in the inventory
inventory[product_name]={
	"quantity": quantity,
	"price":price
}
logging.info(f"Product added :{product_name}")
print ("Product added successfully")


for product_name,details in inventory.items():
	print(f"Product: {product_name}")
	print(f"Quantity: {details['quantity']}")
	print(f"Price: {details['price']}")

#update a product in the inventory 
product_to_update=input("Enter the product name to update quantity:")
product_to_update=product_to_update.strip().lower()
if product_to_update in inventory:
	new_quantity=int(input("Enter new quantity: "))
	inventory[product_to_update]["quantity"]=new_quantity
	logging.info(f"Product quantity updated:{product_to_update}")
	print("Product quantity has been updated ")
else:
	logging.warning(f"update failed.Product was not found:{product_to_update}")
	print("Product not found ")

#remove a product
product_to_remove=input("Enter the product name to remove: ")
product_to_remove=product_to_remove.strip().lower()

if product_to_remove in inventory:
	inventory.pop(product_to_remove)
	print("Product removed ")

else:
	print("Product not found")

#file handling: open()and close()
file=open("inventory.txt","w")#r,a,x

for product_name, details in inventory.items():
    file.write(f"{product_name},{details['quantity']},{details['price']}\n")

file.close()

print("Current inventory has been saved")
#read the whole file 
file=open("inventory.txt","r")
content=file.read()
file.close()
print("Inventory File Content")
print("=========================")
print(content)
# copy content from one file to another 
source_file=open("inventory.txt","r")
content1=source_file.read()
source_file.close()

destination_file=open("inventory2.txt","w")
destination_file.write(content)
destination_file.close()
print("Inventory file copied successfully")
#readline():read one line at a time
file=open("inventory.txt","r")	
product_1=file.readline()
product_2=file.readline()
file.close()
print ("First Product")
print(product_1)
print("Second Product")
print(product_2)
