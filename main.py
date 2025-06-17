import pandas as pd
from employee_system.employee import Employee, Manager
from employee_system import salary
from employee_system import data_handler
from employee_system.visualizer import plot_avg_scores, plot_rating_distribution

#Below Empty list, for storing the data
employee_records = []

#Below Menu to show everytime, when entering the data
menu = """
========== EMPLOYEE MANAGEMENT SYSTEM ==========
1. Add New Employee
2. Add New Manager
3. View All Employees
4. Update Performance Score
5. View Rating Report
6. Salary Statistics
7. Export All Data to CSV
8. Show Performance Chart
9. Show Rating Distribution
10. Exit
"""
#below function takes the productivity, teamwork and communication  inputs of an employee 
def get_scores(is_manager=False):
    scores = {}
    scores["productivity"] = int(input("Productivity: "))
    scores["teamwork"] = int(input("Teamwork: "))
    scores["communication"] = int(input("Communication: "))
    if is_manager: # this if checks whether he is an manager or not, it is added because to take the input of his/her leadership performance
        scores["leadership"] = int(input("Leadership: "))
    return scores

#Below loop continues to run infinitly until you enter 10. This loop is kept to continuously add the data or view the data of a company
while True:
    print(menu)
    choice = input("Choose option: ")

    #To enter the employee details, you need to press 1. Those details are added to the list
    if choice == "1":
        name = input("Name: ")
        dept = input("Department: ")
        sal = float(input("Salary: "))
        scores = get_scores()
        emp = Employee(name, dept, sal, scores)
        employee_records.append(emp.display_info())
        print(f"Added Employee {emp.emp_id}, Avg Score: {emp.avg_score:.2f}, Rating: {emp.rating}")

    #To enter the manager details, you need to press 2. Those details are added to the list
    elif choice == "2":
        name = input("Name: ")
        dept = input("Department: ")
        sal = float(input("Salary: "))
        team_size = int(input("Team size: "))
        scores = get_scores(is_manager=True)
        mgr = Manager(name, dept, sal, scores, team_size)
        employee_records.append(mgr.display_info())
        print(f"Added Manager {mgr.emp_id}, Avg Score: {mgr.avg_score:.2f}, Rating: {mgr.rating}")

    #To view the details of all the employees and managers, you need to enter 3
    elif choice == "3":
        df = pd.DataFrame(employee_records)
        print(df)

    #To update the any employee details, then press 4
    elif choice == "4":
        eid = input("Enter Employee ID to update: ")
        df = pd.DataFrame(employee_records)
        index = df[df["emp_id"] == eid].index
        if index.empty:
            print("Employee not found!")
            continue
        is_manager = "team_size" in df.columns and not pd.isna(df.loc[index[0], "team_size"])
        scores = get_scores(is_manager)
        if is_manager:
            obj = Manager(
                df.loc[index[0], "name"],
                df.loc[index[0], "department"],
                df.loc[index[0], "salary"],
                scores,
                df.loc[index[0], "team_size"]
            )
        else:
            obj = Employee(
                df.loc[index[0], "name"],
                df.loc[index[0], "department"],
                df.loc[index[0], "salary"],
                scores
            )
        employee_records[index[0]] = obj.display_info()
        print("Performance updated.")

    #To View Rating Report of all the employees, then press 5
    elif choice == "5":
        df = pd.DataFrame(employee_records)
        print(df[["emp_id", "name", "avg_score", "rating"]])

    #To get Salary Statistics of each department of the company, then press 6
    elif choice == "6":
        df = pd.DataFrame(employee_records)
        stats = salary.salary_statistics(df)
        print(stats)

    #To Export All Data to CSV, then press 7
    elif choice == "7":
        df = pd.DataFrame(employee_records)
        data_handler.export_to_csv(df)
        print("Data exported to employees.csv")

    #To view Show Performance Chart of each employee, then press 8
    elif choice == "8":
        df = pd.DataFrame(employee_records)
        plot_avg_scores(df)

    #To view Show Rating Distribution, then press 9
    elif choice == "9":
        df = pd.DataFrame(employee_records)
        plot_rating_distribution(df)

    #To exit press 10
    elif choice == "10":
        print("Exiting... Bye!")
        break

    else:
        print("Invalid option.")
