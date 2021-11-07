import random
l=''
g=''
class Words:
    cw=['apple','mango','orange','plums','guava']
    m=random.choice(cw)
    count=5
    

class Guess(Words):
    def guesschar(self):
        global l
        global g
        
        while self.count>0:
            f=0
            
            for i in Words.m:
                if i in l:
                    
                    print(i)
                                        
                else:
                    
                    print('_')
                    f=f+1 
                                      
            if f==0:
                print('You win, the correct word is: ',Words.m)
                break
                
            g=input('Enter the character: ')
            l+=g
            if g not in Words.m:
                self.count=self.count-1
                print('You have entered the wrong letter. you have',self.count,'wrong attempt chances left')


    

            if self.count==0:
                print('You have run out of chances, GAME OVER')

        

c=Guess()
c.guesschar()
