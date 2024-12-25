import mysql.connector as c
con=c.connect(host="localhost",user="root",password="Subhash15@",database="hotel_management")
if con.is_connected():
    print("susscessfully connected")
    hotel=input("Do you want to add hotels (yes/no):")
if (hotel=="yes"):
    while True:
        cursor=con.cursor()
        hotel_id=int(input("enter the hotel_id:"))
        name=input("enter name of hotel:")
        address=input("enter the address:")
        city=input("enter the city:")
        state=input("enter the state:")
        country=input("enter the country:")
        phone=input("enter the phone no:")
        email=input("enter the email address:")
        query1="insert into hotels values({},'{}','{}','{}','{}','{}','{}','{}')".format(hotel_id,name,address,city,state,country,phone,email)
        cursor.execute(query1)
        con.commit()
        print("data saved")
        x=int(input("1-->Enter more\n2-->Exit\n Enter choice:"))
        if x==2:
            break
else:
    rooms=input("Do you want to add rooms (yes/no):")
    if (rooms=="yes"):
        while True:
            cursor=con.cursor()
            room_id=int(input("enter the room id:"))
            hotel_id=int(input("enter the hotel_id:"))
            room_number=input("enter the room number:")
            type=input("enter the type of room you want :")
            price=float(input("enter the price of the room selected:"))
            status=input("enter the status of the room:")
            query2="insert into Rooms values({},{},'{}','{}',{},'{}')".format(room_id,hotel_id,room_number,type,price,status)
            cursor.execute(query2)
            con.commit()
            print("data saved")
            x=int(input("1-->Enter more\n2-->Exit\n Enter choice:"))
            if x==2:
                break
    else:
        customer=input("Do you have new customers are there enter (yes/no):")
        if (customer=="yes"):
            while True:
                cursor=con.cursor()
                customer_id=int(input("enter the customer id:"))
                first_name=input("enter the first name of the customer:")
                last_name=input("enter the last name of the customer:")
                phone=input("enter the phone no. of the customer:")
                email=input("enter the email of the customer:")
                address=input("enter the address of the customer")
                query3="insert into customers values({},'{}','{}','{}','{}','{}')".format(customer_id,first_name,last_name,phone,email,address)
                cursor.execute(query3)
                con.commit()
                print("data saved")

                booking_id=int(input("enter the id for booking:"))
                room_id=int(input("enter the room id which is booked:"))
                customer_id=int(input("enter the customer id:"))
                check_in_date=input("enter the check in date:")
                check_out_date=input("enter the check out date:")
                status=input("enter the status of booking room:")
                query4="insert into bookings value({},{},{},'{}','{}','{}')".format(booking_id,room_id,customer_id,check_in_date,check_out_date,status)
                cursor.execute(query4)
                con.commit()
                print("data saved")

                payment_id=int(input("enter the payment id:"))
                booking_id=int(input("enter the id for booking:"))
                amount=float(input("enter the amount for the room:"))
                payment_date=input("enter the date of payment:")
                payment_method=input("enter the method of payment:")
                query5="insert into payments values({},{},{},'{}','{}')".format(payment_id,booking_id,amount,payment_date,payment_method)
                cursor.execute(query5)
                con.commit()
                print("data saved")
                x=int(input("1-->Enter more\n2-->Exit\n Enter choice:"))
                if x==2:
                    break
        else:
            print("no customers are there: Thank You")
            
                        
    
