print("===== GENERAL KNOWLEDGE QUIZ =====") 
score = 0
# Question 1
print("\n1. Who is the national poet of Pakistan?")
print("a) Allama Iqbal")
print("b) Faiz Ahmed Faiz")
print("c) Mirza Ghalib")
ans = input("Enter answer: ")
if ans.lower() == "a":
    score += 1
# Question 2
print("\n2. Imran Khan served as the Prime Minister of Pakistan from:")
print("a) 2013 to 2017")
print("b) 2018 to 2022")
print("c) 2020 to 2024")
ans = input("Enter answer: ")
if ans.lower() == "b":
    score += 1
# Question 3
print("\n3. Which is the largest continent in the world?")
print("a) Africa")
print("b) Europe")
print("c) Asia")
ans = input("Enter answer: ")
if ans.lower() == "c":
    score += 1
# Question 4
print("\n4. Imran Khan is famous for winning the Cricket World Cup in which year?")
print("a) 1987")
print("b) 1992")
print("c) 1996")
ans = input("Enter answer: ")
if ans.lower() == "b":
    score += 1
# Question 5
print("\n5. Which is the fastest land animal?")
print("a) Lion")
print("b) Horse")
print("c) Cheetah")
ans = input("Enter answer: ")
if ans.lower() == "c":
    score += 1
print("\n===== RESULT =====")
print("Your Score:", score, "/ 5")
if score == 5:
    print("Excellent!")
elif score >= 3:
    print("Good Job!")
else:
    print("Keep Practicing!")
