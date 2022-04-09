Graph = {
"A":["B","C"],
"B":["A","E"],
"C":["D","A"],
"D":["C","F"],
"E":["B"],
"F":["D"]
}

Discovered = []
Queue = []

def bfs_search(Graph,Discovered,Element,ToFind,path):
     Queue.append(Element)
     Discovered.append(Element)
     path=path+Element+"--->"     
     while Queue:
         p = Queue.pop(0)
         print(p)
         if p==ToFind:
             return path
         for adj in Graph[p]:
            if adj not in Discovered:
              path=path+adj+"--->"
              Discovered.append(adj)
              Queue.append(adj)
            




path=""
bfs_search(Graph,Discovered,"A","D",path)     
print(path)
