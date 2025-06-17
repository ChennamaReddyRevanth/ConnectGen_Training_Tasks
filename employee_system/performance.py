import numpy as np

class PerformanceEvaluator:
    def __init__(self, scores: dict, is_manager=False):
        self.scores = scores.copy()
        self.is_manager = is_manager

    #Below function calculates the average of each employee's performance scores
    def calculate_average(self):
        if self.is_manager and "leadership" in self.scores:
            self.scores["leadership"] *= 1.5
        return np.mean(list(self.scores.values()))
    
    #Below function, assign rating to the each employee according to the performance scores (productivity, teamwork and communication)
    def assign_rating(self, avg=None):
        if avg is None:
            avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

