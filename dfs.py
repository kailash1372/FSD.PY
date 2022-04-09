Graph = {
"A":["B","C"],
"B":["A","E"],
"C":["D","A"],
"D":["C","F"],
"E":["B"],
"F":["D"]
}

Discovered = []

def dfs_search(Graph,Discovered,Element):
     if Element not in Discovered:
       Discovered.append(Element)
       print(Element)
     for adj in Graph[Element]:
        if adj not in Discovered:
           dfs_search(Graph,Discovered,adj)
            





dfs_search(Graph,Discovered,"A")     
