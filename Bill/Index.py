def Bill():
    import mysql.connector 
    conn=mysql.connector.connect(
    host="localhost",
    user="root",          #apna username 
    password="bhawna@2026",        #apna password
    database="day3"      #apna database
    )

    cur=conn.cursor()
    order_id=int(input("enter order id:"))
    product_name=input("enter product name:")
    price=int(input("enter product price:"))
    Quantity=int(input("enter quantity:"))
    
    Amount=price*Quantity
    sql="INSERT INTO store(order_id,Product_name,Price,Quatity,Amount) VALUES(%s,%s,%s,%s,%s)"
    values=(order_id,product_name,price,Quantity,Amount)
    cur.execute(sql,values)
    conn.commit()
    print("Data succesfully inserted into product table🤘🤘 ")
    
    Amount=price*Quantity
    # id = str(order_id)
    # ext="txt"
    # s=id + ext
    # x=open(s,"w")
    # # y=x.write(f"order_id:", {id} , "product name:",{product_name},"product price:",{price},"quantity:",{Quantity},"total:",{Amount})
    # y=x.write(
    # f"order_id: {id}, product name: {product_name}, "
    # f"product price: {price}, quantity: {Quantity}, total: {Amount}\n"
    filename = f"{order_id}.txt"
    with open(filename, "w") as f:
        f.write(
            f"Order ID: {order_id}\n"
            f"Product Name: {product_name}\n"
            f"Price: {price}\n"
            f"Quantity: {Quantity}\n"
            f"Total Amount: {Amount}\n"
        )

    print(f"Bill generated: {filename}")


print(Bill())
