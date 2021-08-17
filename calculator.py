def get_name(text: str):
    return input(f"Input the {text}: ")


def calculator(list_number):
    while True:
        temp = []
        for c in range(len(list_number) - 1):
            addition = list_number[c] + list_number[c + 1]
            temp.append(addition)
        list_number = [take_least_number(n) for n in temp]
        if len(list_number) == 2:
            break
    return list_number


def take_least_number(n):
    return n % 10


def handphone_calculate(hape1: str, hape2: str):
    couple_number = "".join(hape1.upper().split()) + "".join(hape2.upper().split())
    couple_number = [int(n) for n in couple_number]
    couple_number = calculator(couple_number)
    result_number = float("".join([str(s) for s in couple_number]))
    return result_number


class CoupleCalculator:
    def __init__(self):
        self.constant = "TRUELOVE"
        self.couple_number = []

    def couple_calculate(self, name1: str, name2: str):
        couple_name = "".join(name1.upper().split()) + "".join(name2.upper().split())
        for w in self.constant:
            self.couple_number.append(couple_name.count(w))

        couple_number = [int(n) for n in self.couple_number]
        couple_number = calculator(couple_number)
        result_number = float("".join([str(s) for s in couple_number]))
        return result_number

    def calculate(self, name1: str, name2: str, hape1: str, hape2: str):
        couple = self.couple_calculate(name1, name2)
        handphone = handphone_calculate(hape1, hape2)
        final = (100 - (couple * handphone) ** .5)
        return str(final) + "%"


if __name__ == "__main__":
    calculator = CoupleCalculator()
    calculator.calculate("bima", "maudy")
