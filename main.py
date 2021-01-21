
#hello just redacted

def iterator(seq):
  for i in seq:
    yield i
    yield -i
n=0
for i in iterator(range(10)):
    n+=1
print(n)
    

        
    