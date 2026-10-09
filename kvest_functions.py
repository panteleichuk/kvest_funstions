from random import randint
from time import sleep

# ==================== БАЗОВІ ФУНКЦІЇ ====================

def draw_line(emoji, n):
    print(emoji * n)

def random_number(start, end, emoji):
    n = randint(start, end)
    print(emoji * n)
    return n

def type_text(txt):
    for letter in txt:
        print(letter, end="")
        sleep(0.03)
    print()

def question(text, a, b, c, correct):
    print(text)
    print("1.", a)
    print("2.", b)
    print("3.", c)
    answer = int(input("Введи номер правильної відповіді: "))
    return answer == correct

def yes_no(qw):
    ans = input(qw + " (так/ні): ").strip().lower()
    return ans == "так"

def character_say(emoji, name, txt):
    print("💠" * 15)
    print(emoji, name, ":")
    print(f"«{txt}»")
    print("💠" * 15)

def action(icon, text):
    print(icon, text)
    print("🎲 Перевіряємо результат...")
    sleep(1)
    result = randint(1, 2)
    if result == 1:
        print("✨ Супер! У тебе вийшло!")
        return True
    else:
        print("😅 Не вийшло! Спробуй ще!")
        return False

def question2(q, right_answer):
    a = input(q)
    while a != right_answer:
        print("Не вірно!")
        a = input(q)
    print("Вірно!")

def cube():
    n = randint(1, 6)
    print("🔒 На дверях кубик долі. Вгадай число від 1 до 6, щоб відкрити замок!")
    ans = int(input("Твоє число: "))
    while ans != n:
        print("😔 Не вгадав, спробуй ще!")
        ans = int(input("Твоє число: "))
    print("🔓 Клац! Замок відкрито!")
def guess_number():
    n = randint(1,100)
    print("Комп'ютер загадує число від 1 до 100.")
    print("Ви відгадуєте його.")
    count = 1
    ans = int(input())
    while ans != n:
        if ans > n:
            print("Ваше число більше!")
        else:
            print("Ваше число менше!")
        ans = int(input())
        count += 1
        
    print(f"Тив вгадав за {count} спроб!")
def rock_scissors_paper():
    print("Гра Камінь, ножиці, папір!")
    bot = randint(1,3)
    pl = int(input("Твій хід: 1 - камінь, 2 - ножиці, 3 - папір? "))
    bot_score = 0
    pl_score = 0
    while pl_score != 5 or bot_score != 5:
        if bot == 1 and pl==2:
            print("Комп'ютер  обрав камінь - ти програв!")
            bot_score+=1
        elif bot == 2 and pl ==3:
             print("Комп'ютер  обрав ножиці - ти програв!")
             bot_score+=1
        elif bot ==3 and pl == 1:
             print("Комп'ютер  обрав папір - ти програв!")
             bot_score+=1
        elif bot == pl:
            print("Комп'ютер теж це обрав - Нічия!")
        else:
             print("Ти виграв!")
             pl_score+=1
        print(f"Поточний рахунок: ти - {pl_score}, комп'ютер -  {bot_score}")
        pl = int(input("Твій хід: 1 - камінь, 2 - ножиці, 3 - папір? "))
    if pl_score > bot_score:
        print(f"Вітаю! Ти виграв з рахунокм {pl_score}:{bot_score}!")
    else:
        print(f"Нажаль :( Ти програв з рахунокм {pl_score}:{bot_score}!")
        
def random_cube():
    n = randint(1,6)
    print("Вгадай число, що випало (від 1 до 6)")
    ans = int(input("Ваша відповідь:"))
    while ans != n:
        print("Не вгадали, спробуйте ще!")
        ans = int(input("Ваша відповідь:"))
    print("Вітаємо! Гру пройдено!")
