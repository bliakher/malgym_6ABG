
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

# girl naming part ----------------------------------------------

def name_girl():
  import random as rnd

  girl_names = ["Marie", "Jana", "Eva", "Hana", "Sofie", "Ema", "Julie", "Anna", "Tereza"]
 
  name = rnd.choice(girl_names)
  print('Name:', name)
  while input('Is this name good (y/n) ').lower() != 'y':
    name = rnd.choice(girl_names)
    print('Name:', name)
  
# menu part --------------------------------------------------------

def gender_choosing():
  child_gender = input("Choose your prefered gender (male/female): ")

  if child_gender == "male":
    name_boy()
  elif child_gender == "female":
    name_girl()
  print(f"You have chosen to name a {child_gender}")



