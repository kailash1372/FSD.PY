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

def bfs_search(Graph,Discovered,Element):
     Queue.append(Element)
     Discovered.append(Element)
     
     while Queue:
         p = Queue.pop(0)
         print(p)
         for adj in Graph[p]:
            if adj not in Discovered:
              Discovered.append(adj)
              Queue.append(adj)
            





bfs_search(Graph,Discovered,"A")     
