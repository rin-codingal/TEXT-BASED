class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num = roman_num + syb[i]
                num -= val[i]
            i += 1

        return roman_num

#create object
num1 = py_solution()
num2 = py_solution()
print(num1.int_to_Roman(12))
print(num2.int_to_Roman(35))