import json
import time

done = False

with open('Birthdays.json', "r+") as f:
    data = json.load(f)

    print("Welcome to the Birthday game ! We have the birthdays to: \n")
    time.sleep(1)

    for birthday in data:
        print(birthday['name'])
    time.sleep(1)

    while done == False:
        ask = input("\n Would you like to add or lookup a birthday? ")
        time.sleep(1)
        if ask == "lookup":
            choice = input("\n Who's birthday do you want to look up? ")

            for birthday in data:
                if choice == birthday['name']:
                    time.sleep(1)
                    print(
                        f"\n The birthday of {choice} is: {birthday['birthday']}")
                    askagain = input(
                        "\n Are you done? ")
                    if askagain == 'yes':
                        done = True

        if ask == "add":
            name = input("\n What is their name? ")
            birthday = input(f"\n What is {name}'s birthday? ")

            obj = {
                "name": name,
                "birthday": birthday
            }

            data.append(obj)

            f.seek(0)
            f.truncate()
            f.write(json.dumps(data))
            f.close()
            askagain = input(
                "\n Are you done? ")

            if askagain == 'yes':
                done = True
