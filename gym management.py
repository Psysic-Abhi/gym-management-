### common part of both the programs   

import mysql.connector 
print("Admin Login Panel")
us = input("Enter your SQL User ID: ")
ps = input("Enter your SQL password: ")

# Main project(code for doing all the operation in database gym_management)

try:
    db = mysql.connector.connect(
    host="localhost",
    user=str(us),
    password=str(ps),
    database="gym_management"
    )

    cursor = db.cursor()

# Members   

    def add_member(first_name, last_name, age, gender, phone, email, join_date, membership_plan):
        try:
            sql = "INSERT INTO members (first_name, last_name, age, gender, phone, email, join_date, membership_plan) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (first_name, last_name, age, gender, phone, email, join_date, membership_plan)
            cursor.execute(sql, values)
            db.commit() 
            print("Member added successfully!")
        except mysql.connector.Error as err:
            print(f"Error adding member: {err}")

    def view_members():
        try:
            cursor.execute("SELECT * FROM members")
            members = cursor.fetchall()
            for member in members:
                print(member)
        except mysql.connector.Error as err:
            print(f"Error viewing members: {err}")

    def update_member(member_id, first_name=None, last_name=None, age=None, phone=None, email=None):
        try:
            sql = "UPDATE members SET "
            fields = []
            values = []

            if first_name:
                fields.append("first_name = %s")
                values.append(first_name)
            if last_name:
                fields.append("last_name = %s")
                values.append(last_name)
            if age:
                fields.append("age = %s")
                values.append(age)
            if phone:
                fields.append("phone = %s")
                values.append(phone)
            if email:
                fields.append("email = %s")
                values.append(email)

            sql += ", ".join(fields)
            sql += " WHERE member_id = %s"
            values.append(member_id)

            cursor.execute(sql, tuple(values))
            db.commit()
            print("Member updated successfully!")
        except mysql.connector.Error as err:
            print(f"Error updating member: {err}")
            
# Plans

    def add_plan(plan_name, duration_months, cost):
        try:
            sql = "INSERT INTO plans(plan_name, duration_months, cost) VALUES (%s, %s, %s)"
            values = (plan_name, duration_months, cost)
            cursor.execute(sql, values)
            db.commit()
            print("Plan added successfully!")
        except mysql.connector.Error as err:
            print(f"Error adding plan: {err}")
        
    def view_plans():
        try:
            cursor.execute("SELECT * FROM plans")
            plans = cursor.fetchall()
            for plan in plans:
                print(plan)
        except mysql.connector.Error as err:
            print(f"Error viewing plans: {err}")

    def update_plan(plan_id, plan_name=None, duration_months=None, cost=None):
        try:
            sql = "UPDATE plans SET "
            fields = []
            values = []

            if plan_name:
                fields.append("plan_name = %s")
                values.append(plan_name)
            if duration_months:
                fields.append("duration_months = %s")
                values.append(duration_months)
            if cost:
                fields.append("cost = %s")
                values.append(cost)

            sql += ", ".join(fields)
            sql += " WHERE plan_id = %s"
            values.append(plan_id)

            cursor.execute(sql, tuple(values))
            db.commit()
            print("Plan updated successfully!")
        except mysql.connector.Error as err:
            print(f"Error updating plan: {err}")

    def delete_plan(plan_id):
        try:
            query = "DELETE FROM plans WHERE plan_id = %s"
            value = (plan_id,)
            cursor.execute(query, value)
            db.commit()
            print("Plan deleted successfully!")
        except mysql.connector.Error as err:
            print(f"Error deleting plan: {err}")

# Attendance

    def add_attendance(member_id, date):
        try:
            sql = "INSERT INTO attendance(member_id, date) VALUES (%s, %s)"
            values = (member_id, date)
            cursor.execute(sql, values)
            db.commit()
            print("Attendance added successfully!")
        except mysql.connector.Error as err:
            print(f"Error adding attendance: {err}")

    def view_attendance():
        try:
            cursor.execute("SELECT attendance_id, date, first_name, last_name FROM attendance, members WHERE attendance.member_id = members.member_id")
            result = cursor.fetchall()
            for row in result:
                print(row)
        except mysql.connector.Error as err:
            print(f"Error viewing attendance: {err}")

    def delete_attendance(attendance_id):
        try:
            query = "DELETE FROM attendance WHERE attendance_id = %s"
            value = (attendance_id,)
            cursor.execute(query, value)
            db.commit()
            print("Attendance deleted successfully!")
        except mysql.connector.Error as err:
            print(f"Error deleting attendance: {err}")

# Payment

    def add_payment(member_id, amount):
        try:
            import datetime
            query = "INSERT INTO payments (member_id, amount, payment_date) VALUES (%s, %s, %s)"
            values = (member_id, amount, datetime.date.today())
            cursor.execute(query, values)
            db.commit()
            print("Payment added successfully!")
        except mysql.connector.Error as err:
            print(f"Error adding payment: {err}")

    def view_payments():
        try:
            cursor.execute("SELECT * FROM payments")
            result = cursor.fetchall()
            for row in result:
                print(row)
        except mysql.connector.Error as err:
            print(f"Error viewing payments: {err}")

    def delete_payment(payment_id):
        try:
            query = "DELETE FROM payments WHERE payment_id = %s"
            value = (payment_id,)
            cursor.execute(query, value)
            db.commit()
            print("Payment deleted successfully!")
        except mysql.connector.Error as err:
            print(f"Error deleting payment: {err}")

# Staff

    def add_staff(name, position, contact_number, hire_date, salary):
        try:
            query = "INSERT INTO staff (name, position, contact_number, hire_date, salary) VALUES (%s, %s, %s, %s, %s)"
            values = (name, position, contact_number, hire_date, salary)
            cursor.execute(query, values)
            db.commit()
            print("Staff added successfully!")
        except mysql.connector.Error as err:
            print(f"Error adding staff: {err}")

    def view_staff():
        try:
            cursor.execute("SELECT * FROM staff")
            result = cursor.fetchall()
            for row in result:
                print(row)
        except mysql.connector.Error as err:
            print(f"Error viewing staff: {err}")

    def update_staff(staff_id, name=None, position=None, contact_number=None, salary=None):
        try:
            sql = "UPDATE staff SET "
            fields = []
            values = []
            
            if name:
                fields.append("name = %s")
                values.append(name)
            if position:
                fields.append("position = %s")
                values.append(position)
            if contact_number:
                fields.append("contact_number = %s")
                values.append(contact_number)
            if contact_number:
                fields.append("salary = %s")
                values.append(salary)
            
            
            sql += ", ".join(fields)
            sql += " WHERE staff_id = %s"
            values.append(staff_id)

            cursor.execute(sql, tuple(values))
            db.commit()
            print("Staff updated successfully!")
        except mysql.connector.Error as err:
            print(f"Error updating staff: {err}")


    def delete_staff(staff_id):
        try:
            query = "DELETE FROM staff WHERE staff_id = %s"
            value = (staff_id,)
            cursor.execute(query, value)
            db.commit()
            print("Staff deleted successfully!")
        except mysql.connector.Error as err:
            print(f"Error deleting staff: {err}")

#Equipmemt

    def add_equipment(name, conditions, seller_number, purchase_date, amount):
        try:
            query = "INSERT INTO equipment (name, conditions, seller_number, purchase_date, amount) VALUES (%s, %s, %s, %s, %s)"
            values = (name, conditions, seller_number, purchase_date, amount)
    
            cursor.execute(query, values)
            db.commit()
    
            print("Equipment added successfully!")
        except mysql.connector.Error as err:
            print(f"Error adding equipment: {err}")

    def view_equipment():
        try:
            cursor.execute("SELECT * FROM equipment")
            result = cursor.fetchall()
    
            for row in result:
                print(row)
        except mysql.connector.Error as err:
            print(f"Error viewing equipment: {err}")

    def update_equipment(equipment_id, name=None, conditions=None, seller_number=None, purchase_date=None, amount=None):
        try:
            sql = "UPDATE equipment SET "
            fields = []
            values = []

            if name:
                fields.append("name = %s")
                values.append(name)
            if conditions:
                fields.append("conditions = %s")
                values.append(conditions)
            if seller_number:
                fields.append("seller_number = %s")
                values.append(seller_number)
            if purchase_date:
                fields.append("purchase_date = %s")
                values.append(purchase_date)
            if amount:
                fields.append("amount = %s")
                values.append(amount)
    
            sql += ", ".join(fields)
            sql += " WHERE equipment_id = %s"
            values.append(equipment_id)

            cursor.execute(sql, tuple(values))
            db.commit()
            print("Equipment updated successfully!")
        except mysql.connector.Error as err:
            print(f"Error updating equipment: {err}")

    def delete_equipment(equipment_id):
        try:
            query = "DELETE FROM equipment WHERE equipment_id = %s"
            value = (equipment_id,)
    
            cursor.execute(query, value)
    
            print("Equipment deleted successfully!")
        except mysql.connector.Error as err:
            print(f"Error deleting equipment: {err}")

# Main Part

    if __name__ == "__main__":
        while True:
            print("\nGym Management System")
            print("Type the associate number for any of the related issues listed below")
            print("1.Member")
            print("2.Plans")
            print("3.Attendance")
            print("4.Payments")
            print("5.Staff")
            print("6.Equipments")
            print("7. Exit")

            choice = input("Enter your choice: ")

 
            if choice=="1":
            
                print("Type the letter associated with objective")
                print("a. Add Member")
                print("b. View Members")
                print("c. Update Member")
            
        
                choice1 = input("Enter your choice: ")
        
                if choice1 == "a":
                    try:
                        first_name = input("First Name: ")
                        last_name = input("Last Name: ")
                        age = int(input("Age: "))
                        gender = input("Gender: ")
                        phone= input("Phone No: ")
                        email = input("Email Id: ")
                        join_date = input("Join Date (YYYY-MM-DD): ")
                        membership_plan = input("Membership Plan (Silver/Gold/Diamond): ")
                        add_member(first_name, last_name, age, gender, phone, email, join_date, membership_plan)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")

                elif choice1 == "b":
                    view_members()
        
                elif choice1 == "c":
                    try:
                        member_id = int(input("Enter Member ID: "))
                        print("Leave fields blank if you don't want to update them.")
                        first_name = input("First Name: ")
                        last_name = input("Last Name: ")
                        age = input("Age: ")
                        age = int(age) if age else None
                        phone = input("Phone No: ")
                        email = input("Email ID: ")
                        update_member(member_id, first_name, last_name, age, phone, email)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")

                else:
                    print("Invalid choice! Please try again.")

            elif choice=="2":
                print("Type the letter associated with objective")
                print("a. Add Plan")
                print("b. View Plans")
                print("c. Update Plan")
                print("d. Delete Plan")

                choice1 = input("Enter your choice: ")

                if choice1 == "a":
                    try:
                        plan_name=input("Plan Name :")
                        duration_months=int(input("Duration in months :"))
                        cost=float(input("Enter cost :"))
                        add_plan(plan_name,duration_months,cost)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")

                elif choice1=="b":
                    view_plans()

                elif choice1=="c":
                    try:
                        plan_id=int(input("Enter Plan id:"))
                        print("Leave fields blank if you don't want to update them.")
                        plan_name=input("Enter Plan Name :")
                        duration_months=input("Enter duration in months :")
                        duration_months=int(duration_months) if duration_months else None
                        cost=input("Enter cost :")
                        cost=float(cost) if cost else None
                        update_plan(plan_id,plan_name,duration_months,cost)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")

                elif choice1 =='d':
                    try:
                        plan_id = int(input("Enter plan ID to delete: "))
                        delete_plan(plan_id)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")

                else:
                    print("Invalid choice! Please try again.")

            elif choice =="3":
                print("Type the letter associated with objective")
                print("a. Add Attendance")
                print("b. View Attendance")
                print("c. Delete Attendance")
            
        
                choice1 = input("Enter your choice: ")
        
                if choice1 == "a":
                    try:
                        member_id = int(input("Enter member ID: "))
                        date =input(" Present on (YYYY-MM-DD):")
                        add_attendance(member_id, date)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")
        
                elif choice1 == "b":
                    view_attendance()

                elif choice1 =="c":
                    try:
                        attendance_id = int(input("Enter Attendance ID to delete: "))
                        delete_attendance(attendance_id)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")

                else:
                    print("Invalid choice! Please try again.")

            elif choice =="4":
                print("\nManage Payments")
                print("a. Add Payment")
                print("b. View Payments")
                print("c. Delete Payment")

                choice1 = input("Enter your choice: ")
        
                if choice1 == 'a':
                    try:
                        member_id = int(input("Enter member ID: "))
                        amount = float(input("Enter amount: "))
                        add_payment(member_id, amount)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")

                elif choice1 == 'b':
                    view_payments()

                elif choice1 == 'c':
                    try:
                        payment_id = int(input("Enter payment ID to delete: "))
                        delete_payment(payment_id)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")

                else:
                    print("Invalid choice! Please try again.")
        
            elif choice=="5":
            
                print("Type the letter associated with objective")
                print("a. Add Staff")
                print("b. View Staff")
                print("c. Update Staff")
                print("d. Delete Staff")
            
        
                choice1 = input("Enter your choice: ")
        
                if choice1 == "a":
                    try:
                        name = input("Enter Name: ")
                        position = input("Enter position: ")
                        contact_number = input("Enter contact number: ")
                        hire_date = input("Joining Date (YYYY-MM-DD)")
                        salary = int(input("Enter Salary: "))
                        add_staff(name, position, contact_number, hire_date, salary)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")
        
                elif choice1 == "b":
                    view_staff()
        
                elif choice1 == "c":
                    try:
                        staff_id = int(input("Enter Staff ID: "))
                        print("Leave fields blank if you don't want to update them.")
                        name = input("Enter Name: ")
                        position = input("Enter position: ")
                        contact_number = input("Enter contact number: ")
                        salary = input("Enter New Salary: ")
                        update_staff(staff_id, name, position, contact_number, salary)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")

                elif choice1 == "d":
                    try:
                        staff_id = int(input("Enter Staff ID to delete: "))
                        delete_staff(staff_id)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")

                else:
                    print("Invalid choice! Please try again.")

            elif choice == "6":
                print("\nManage Equipment")
                print("a. Add Equipment")
                print("b. View Equipment")
                print("c. Update Equipment")
                print("d. Delete Equipment")
        
                choice = input("Enter your choice: ")
        
                if choice == 'a':
                    try:
                        name = input("Enter equipment name: ")
                        purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
                        conditions = input("Enter condition: ")
                        seller_number = int(input("Enter the seller code:"))
                        amount = float(input("Enter amount of equipment: "))
                        add_equipment(name, conditions, seller_number, purchase_date, amount)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")

                elif choice == 'b':
                    view_equipment()

                elif choice == 'c':
                    try:
                        equipment_id = int(input("Enter equipment ID to update: "))
                        name = input("Enter new name: ")
                        purchase_date = input("Enter new purchase date (YYYY-MM-DD): ")
                        conditions = input("Enter new condition: ")
                        seller_number = input("Enter the new seller code:")
                        amount = float(input("Enter amount of equipment: "))
                        update_equipment(equipment_id, name, conditions, seller_number, purchase_date, amount)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")

                elif choice == 'd':
                    try:
                        equipment_id = int(input("Enter equipment ID to delete: "))
                        delete_equipment(equipment_id)
                    except ValueError as err:
                        print(f"Error due to wrong type value in input: {err}")

                else:
                    print("Invalid choice! Please try again.")

            elif choice == "7":
                print("Thank You for using Gym Management System")
                break
       
            else:
                print("Invalid choice! Please try again.")

except mysql.connector.Error as err:
     print(f"Incorrect password entered: {err}")
     