from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list);
        self.dfs=""
        self.found=False
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFS(self,root,search,visited):
        visited.add(root)
        self.dfs=self.dfs+root+""
        if(root==search):
            self.found=True
            return
        for neighbour in self.graph[root]:
            if neighbour not in visited:
                self.DFS(neighbour,search,visited)
    def Dfs(self,root,search):
        visited=set();
        self.DFS(root,search,visited)
g=Graph()
n=int(input("enter no.of nodes\n"))
root=input("enter root node\n")
search=input("enter goal node\n")
print("enter vertices of tree\n")
for i in range(n-1):
    s=input()
    x=s.split(",")
    g.addEdge(x[0],x[1])
g.Dfs(root,search)
if(g.found):
    print("following is the depth-first search\n")
    print(g.dfs)
else:
    print("given search element is not found in tree\n")