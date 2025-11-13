print("Example")

task = input("What is the task needing to be done?")

importance = input("How important is this task? On a scale of 1-5?")

deadline = int(input("How many hours do you have to do this?"))

print("\n--- TIME MANAGEMENT ADVICE ---")

importance_level = int(importance)

if importance_level == 1:
    print("This task is low priority. Do it only if you have spare time.")

if importance_level == 2:
    print("Not very urgent. Plan it after your main tasks.")

if importance_level == 3:
    print("Moderately important. Try to schedule it soon.")

if importance_level == 4:
    print("Important task. You should work on it today.")

if importance_level == 5:
    print("Very important! Make this your top priority.")

if deadline < 2:
    print("You have very little time—start immediately!")

if deadline == 2:
    print("Two hours left. Focus and avoid distractions.")

if deadline > 2:
    print("You have some time. Break the task into smaller steps.")

print("\nGood luck managing your task!")























