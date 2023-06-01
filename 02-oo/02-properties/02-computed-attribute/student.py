

class BMICalculator:

    def __init__(self, weight_in_kg, height_in_m):
        self.weight_in_kg = weight_in_kg
        self.height_in_m = height_in_m

    @property
    def weigth(self):
        return self.weight_in_kg

    @property
    def heigth(self):
        return self.height_in_m

    @property
    def bmi(self):
        BMI = self.weight_in_kg / self.height_in_m ** 2
        return BMI

    @property
    def category(self):
        BMI = self.bmi
        if BMI <= 18.5:
            return "underweight"
        if 18.5 <= BMI and BMI <= 25:
            return "normal"
        else:
            return "overweight"
