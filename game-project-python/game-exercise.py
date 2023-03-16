

















class Game:

    def __init__(self):
        while True:
            print('''welcome
             1: Names Count
             2: Divided By
             3: Sentence No Duplicate
             4: to exit''')

            user_choice= int(input('Enter Game Number : '))
            if user_choice ==4:
                print('goodbye')
                break
            elif user_choice == 1:
                self.names_count
                
            elif user_choice == 2:
                self.divided_by()
                

            elif user_choice == 3:
                self.Sentence_no_duplicate()

            else :
                print(f'no game with this number : {user_choice}')

            play_again = input('Press any key to play againg , n to exit : ')
            if play_again =='n':
                print('goodbye')
                break

    def names_count(self):
        names= (input('Enter Names comma seperated : ')).split(',')
        names_count = [len(x) for x in names]
        print(names_count)
        

    def divided_by(self):
        x= int(input('Enter First Number : '))
        y= int(input('Enter Second Number : '))
        result=[]
        for n in range(1,101):
            if n%x == 0 and n%y==0:
                result.append(n)
        print(result)
            

    def Sentence_no_duplicate(self):
        sentence = input('Enter Sentence : ')
        words = sentence.split(' ')
        words_no_duplicate = []
        for w in words:
            if w not in words_no_duplicate:
                words_no_duplicate.append(w)
        print(words_no_duplicate)
        print(' '.join(words_no_duplicate))
        print('-'.join(words_no_duplicate))
        print('/'.join(words_no_duplicate))
        
        




g1 = Game()
