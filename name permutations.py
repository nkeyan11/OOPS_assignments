import itertools
class Names:
    

    def perm(self):
        name=input('Enter the name: ')
        print(list(itertools.permutations(name)))
        
c=Names()
c.perm()

        
