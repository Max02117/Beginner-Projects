stipend = float(input("Стипендия (руб.): "))
base_expenses = float(input("Расходы (руб.): "))

total_deficit = 0.0
current_expenses = base_expenses

for _ in range(10):
    monthly_deficit = current_expenses - stipend
    total_deficit += monthly_deficit
    current_expenses *= 1.03

print(f"Необходимая сумма: {total_deficit:.2f} руб.")