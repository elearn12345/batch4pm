class a:
    def m(self):
        print('class-1')

class b:
    def m(self):
        print('class-2')

class c:
    def m(self):
        print('class-3')

class d:
    def n(self):
        print('class-4')

l=[a(),b(),c(),d()]
for i in l:
    if hasattr(i,'m'):
        i.m()
    elif hasattr(i,'n'):
        i.n()
        
    





