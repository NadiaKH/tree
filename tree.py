def to_dict(edges):
    d = {}
    for u, v in edges:
        if u not in d:
            d[u] = []
        d[u].append(v)
        if v not in d:
            d[v] = []
        d[v].append(u)
    return d

def dfs(v, g, h, parent=None):
    if not parent:
        h[v] = 0
    else:
        h[v] = h[parent] + 1
    
    for child in g[v]:
        if child in h:
            continue
        dfs(child, g, h, v)

        
def task_4(root, edges):
    g = to_dict(edges)
    h = {}
    dfs(root, g, h)
    for k in sorted(h.keys()):
        print("{}:{}".format(k, h[k]))
    return h
