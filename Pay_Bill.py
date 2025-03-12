# import random
#
# friends = ["Faisal", "Ajit", "Naveed", "Avinash", "Sunil", "Vinod"]
#
# # 1: Option
# # who_will_pay = random.randint(0 , 5)
#
# input("Please press enter to know who will pay the bill...")
# #
# # if who_will_pay == 0:
# #     print(friends[0])
# # elif who_will_pay == 1:
# #     print(friends[1])
# # elif who_will_pay == 2:
# #     print(friends[2])
# # elif who_will_pay == 3:
# #     print(friends[3])
# # elif who_will_pay == 4:
# #     print(friends[4])
# # elif who_will_pay == 5:
# #     print(friends[5])
#
# # 2: Option
#
# random_index = random.randint(0, 5)
# print(friends[random_index])
#
# # 3: Option
# # print(random.choice(friends))


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

print(dirty_dozen[0])

print(dirty_dozen[1])

print(dirty_dozen[1][2])

print(dirty_dozen[1][3])
