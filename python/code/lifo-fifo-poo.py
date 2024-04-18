class Pile :
    def __init__(self):
        self._data = list()
        
    def empiler(self, n) :
        return self._data.append(n)

    
    def depiler(self) :
        return self._data.pop(-1)

    
    def est_vide(self) :
        if len(self._data) == 0 :
            return True
        else : 
            return False 
        
    def sommet(self):
        if len(self._data) == 0 :
            return None
        else : 
            return self._data[-1]
            
pile = Pile()
assert pile.est_vide() is True
pile.empiler(1)
assert pile.est_vide() is False
assert pile.sommet() == 1


pile.empiler(2)
assert pile.est_vide() is False
assert pile.sommet() == 2
assert pile.est_vide() is False


pile.empiler(3)
assert pile.sommet() == 3
assert pile.depiler() == 3


while not pile.est_vide():
    pile.depiler()


assert pile.est_vide() is True
assert pile.sommet() is None

from collections import *
class File :
    
    
    def __init__(self) :
        self._data = deque()
        
        
    def et_vide(self) :
        if len(self._data) == 0 :
            return True 
        else :
            return False 
        
        
    def enfiler(self, n) :
        return self._data.append(n)
    
    
    def defiler(self):
        return self._data.popleft()
        
    
    def tete(self):
        if self.et_vide() == True :
            return None
        else :
            return self._data[0]
    
    

file = File()
assert file.et_vide() is True
file.enfiler(1)

assert file.et_vide() is False
assert file.tete() == 1


file.enfiler(2)

assert file.et_vide() is False
assert file.tete() == 1
assert file.et_vide() is False

file.enfiler(3)
assert file.tete() == 1
assert file.et_vide() is False


assert file.defiler() == 1
assert file.defiler() == 2
assert file.defiler() == 3


assert file.et_vide() is True
assert file.tete() is None    
