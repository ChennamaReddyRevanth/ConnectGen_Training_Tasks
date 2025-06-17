import numpy as np
from .performance import PerformanceEvaluator


#The below class is used to add the employee details
class Employee:
    emp_counter = 1

    def __init__(self, name, department, salary, performance_scores): #Constructor assigns variables to the instance objects
        self.emp_id = f"E{Employee.emp_counter:03d}"
        Employee.emp_counter += 1
        self.name = name
        self.department = department
        self.salary = salary
        self.performance_scores = performance_scores

        evaluator = PerformanceEvaluator(self.performance_scores, is_manager=False)
        self.avg_score = evaluator.calculate_average()
        self.rating = evaluator.assign_rating(self.avg_score)

    def display_info(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary,
            "avg_score": round(self.avg_score, 2),
            "rating": self.rating
        }

#The below class is used to add the Manager details
class Manager(Employee):
    def __init__(self, name, department, salary, performance_scores, team_size):#Constructor assigns variables to the instance objects
        self.team_size = team_size
        self.performance_scores = performance_scores
        super().__init__(name, department, salary, performance_scores)

        evaluator = PerformanceEvaluator(self.performance_scores, is_manager=True)
        self.avg_score = evaluator.calculate_average()
        self.rating = evaluator.assign_rating(self.avg_score)

    def display_info(self):
        base = super().display_info()
        base["team_size"] = self.team_size
        return base