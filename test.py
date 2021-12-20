import numpy as np
from queue import Queue
np.random.seed(42)

def gen_test():
    g = {}    
    n = np.random.randint(10, 20)
    vert = np.arange(1, n + 1)
    parent = np.arange(0, n + 1)
    h = np.zeros_like(parent, dtype='int')
    
    np.random.shuffle(vert)
    
    for i, v in enumerate(vert):
        free_vs = vert[i + 1:]
        if len(free_vs) > 0: 
            parent[v] = np.random.choice(free_vs)    
        
    q = Queue(1000)
    q.put(vert[-1])
    #for i, p in enumerate(parent):
     #   print(i, p)
     
    
    while not q.empty():
        w = q.get()
        #print("g", w)
        for i in range(1, n + 1):
            if parent[i] == w and i != parent[i]:
                h[i] = h[w] + 1
                q.put(i)
                #print("p", i)
    
    
    
    return parent, h
        
        

                
    
    
parent, h = gen_test()

edges = []
root = None
ans = {}
for ch, p in enumerate(parent):
    if ch == p:
        root = p
    else:
        edges.append([p, ch])


for v, height in enumerate(h):
    if v == 0:
        continue
    ans[v] = height

task_4(root, edges) == ans 
