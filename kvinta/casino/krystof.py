import random as rnd
bank = (100)
bet = 0
coin = (1, 2)
while True:
      print('you have', bank, '$')
      print('press 1 to play coin throw, or 2 to play russian roulette')
      a = int(input())
      if a == 1:
           opponent_throw = rnd.choice(coin)
           print('how much do you want to bet? ')
           bet = int(input())
           while bet > bank:
               print('you only have $', bank)
               print('how much do you want to bet? ')
               bet = int(input())
           while bet < 5:
               print('the minimal bet is $5')
               print('how much do you want to bet?')
           bank = bank - bet
           print('if you bet on tails, press 1, if you bet on heads, press 2')
           b = int(input())
           if opponent_throw == b:
                print('you have won', bet*2,'$')
                bank =+ bet*2
           else:
                print('you lost', bet,'$')
      elif a == 2:
            gun = (1, 1, 1, 1, 1, 2)
            while True:
                 print('press 1 to shoot, press 2 to quit')
                 c = int(input())
                 if c == 1:
                      shot = rnd.choice(gun)
                      if shot == 2:
                           print('you died')
                           break
                      else:
                           print('you survived!')
                 elif c == 2:
                      break
                      
                 
            

