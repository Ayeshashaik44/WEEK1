graph={}
n=int(input("enter the no.of nodes: "))
for i in range(n):
    ver=input("enter the vertice:")
    neigh=input("enter the neighboring nodes:").split()
    graph[ver]=neigh
startnode=input("enter the startnode :")
print(graph[startnode])

