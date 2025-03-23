print("ברוך הבא למחשבון ה-BMI!")

weight = float(input("הכנס את המשקל שלך בקילוגרמים: "))
height = float(input("הכנס את הגובה שלך במטרים: "))

bmi = weight / (height ** 2)

print(f"ה-BMI שלך הוא: {bmi:.2f}")

if bmi < 18.5:
    print("אתה בתת-משקל.")
elif bmi < 25:
    print("המשקל שלך תקין.")
elif bmi < 30:
    print("יש לך עודף משקל.")
else:
    print("אתה במצב של השמנה.")
