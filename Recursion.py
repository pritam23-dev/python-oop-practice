# যখন একটি function নিজেই নিজেকে call করে, তখন তাঁকে Recursion বলে
# When a function calls itself, it is called recursion.

def countdown(n):
    if n == 0:     # base case
       print("start")
       return
    print(n)
    countdown(n - 1)     # recursive case

countdown(3)


def loop_porikha():
    # এখানে ১ থেকে ৫ পর্যন্ত লুপ চালানোর জন্য range(1, 6) ব্যবহার করা হয়েছে
    for sonkha in range(1, 6):
        print(f"লুপ এখন এই সংখ্যাটি দেখছে: {sonkha}")

        # একটি শর্ত বা ইফ (if) বসালাম
        if sonkha == 3:
            return "আমি ৩ পেয়ে গেছি, তাই খেলা শেষ!"

        print("লুপের ভেতরের বাকি কাজ...")


# ফাংশনটি কল করে রেজাল্টটি ভ্যারিয়েবলে রাখা হলো
rezult = loop_porikha()

print("-" * 40)  # জাস্ট একটা বর্ডার দেওয়ার জন্য
print(f"ফাংশন থেকে যা ফেরত আসলো: {rezult}")


def bonus_hishab(salary):
    if salary < 20000:
        return 5000

    return 2000
    print("আপনার বোনাস হিসাব করা হয়েছে!")


amar_bonus = bonus_hishab(15000)
print(amar_bonus)


for i in range(3, 0, -1):
    print(i)
print("বুম!")


def countdown(n):
    # ১. এখানে 'if' হলো আমাদের থামার উপায় (Base Case)
    if n == 0:
        return print("বুম!")

    print(n)

    # ২. এখানে ফাংশনটি নিজেকে আবার ডাকছে (Recursion)
    return countdown(n - 1)


countdown(3)




