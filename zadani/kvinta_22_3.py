
# enter the application
# menu: choose the sex of the baby
# sex -> name_boy(), name_girl()


# name_boy() -> name (string)

# boys - name suggestions
# suggest a name
# ask if want another name

# name_girl() -> name (string)

# girls - name suggestions
# suggest a name
# ask if want another name

# choose name -> return  to menu
# name other child

# boy naming part -----------------------------------------------------

def get_boy_name():
    boy_names = ["Maxík", "Kopáč", "Maxmilián', 'Klement", "Maxim"]
    return rnd.choice(boy_names)


def name_boy():
    while True:
        boy_name = get_boy_name()

        print(f"Is {boy_name} ok?")
        print("\t[A]:  Yes")
        print("\t[B]:  No")
        print("\t[ANY] Exit")
        input_key = input()

        if input_key == "a" or input_key == "A":
            print("bááájo")
            chosen_name = "Your name: " + boy_name
            return chosen_name
            break
        elif input_key == "b" or input_key == "B":
            continue
        else:
            break
            return False


result = name_boy()
print(result)
