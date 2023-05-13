class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        height_m = self.height / 100  # ubah cm ke m
        return self.weight / (height_m ** 2)

    def status(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"


def input_data():
    weight = float(input("Masukkan berat badan (kg): "))
    height = float(input("Masukkan tinggi badan (cm): "))
    return weight, height


def main():
    weight, height = input_data()
    bmi = BMI(weight, height)
    print("BMI Anda adalah:", bmi.calculate_bmi())
    print("Status berat badan Anda adalah:", bmi.status())


if __name__ == "__main__":
    main()
