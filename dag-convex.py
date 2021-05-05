
import re, sys
from matplotlib import pyplot as plt
import networkx as nx
"""
Start of Professor Paliath Narendran's code
"""
def hd(L):
    return L[0]

def tl(L):
    return L[1:]

def cons(x, L):
    LL = L.copy()
    LL.insert(0, x)
    return LL

def myappend(L1, L2):
    L11 = L1.copy()
    L11.extend(L2)
    return L11

def isempty(L):
    return (len(L) == 0)

def member(x, L):
    return (x in L)

def sameset(L1, L2):
    return (set(L1) == set(L2))

def listunion(L1, L2):
    L11 = L1.copy()
    L22 = L2.copy()
    S1 = set(L11)
    S2 = set(L22)
    S3 = S1.union(S2)
    return list(S3)

def listintersect(L1, L2):
    L11 = L1.copy()
    L22 = L2.copy()
    S1 = set(L11)
    S2 = set(L22)
    S3 = S1.intersection(S2)
    return list(S3)

def mapunion(f, L):
    if isempty(L):
        return []
    else:
        return listunion(f(hd(L)), mapunion(f, tl(L)))

def remove_duplicates(L):
    L11 = L.copy()
    S1 = set(L11)
    return list(S1)

def source(pair):
    return [pair[0]]

def destination(x, y):
    return [pair[1]]

def first(pair):
    return pair[0]

"""
>>> ls = list(map(first, [(1, 2), (2, 4)]))
>>> ls
[1, 2]
"""

def second(pair):
    return pair[1]

def sources(dag):
    return list(map(first, dag))

def next(dag, a):
    if isempty(dag):
        return []
    elif first(hd(dag)) == a:
        return cons(second(hd(dag)), next(tl(dag), a))
    else: return next(tl(dag), a)

def prev(dag, a):
    if isempty(dag):
        return []
    elif second(hd(dag)) == a:
        return cons(first(hd(dag)), prev(tl(dag), a))
    else: return prev(tl(dag), a)

def reachables(dag, x):
    L1 = next(dag, x)
    L2 = []
    for z in L1:
        L2 = listunion(L2, reachables(dag, z))
    return listunion(L1, L2)

"""
>>> dag1 = [(1,2), (1,3), (3,2), (4,1)]
>>> reachables(dag1, 4)
[1, 2, 3]
"""

def all_reachables_from(dag, L):
    L1 = []
    for x in L:
        L1 = listunion(L1, reachables(dag, x))
    return L1


def alien_neighbours(dag, L):
    LL = []
    for y in L:
        LL = listunion(LL, next(dag, y))
    LL2 = []
    for z in LL:
        if member(z, L):
            LL2 = LL2
        else: LL2 = listunion([z], LL2)
    return LL2

"""
>>> dag2 = [(1,2), (1,3), (1,4), (4,2), (4,5), (3,5)]
>>> alien_neighbours(dag2, [2,4])
[5]
>>> alien_neighbours(dag2, [3,4])
[2, 5]
>>>
"""


"""
End of Professor Paliath Narendran's code
"""

# checks the regex of the given list an edge
def edgeRegEx(list):
	regex = "\([a-zA-Z0-9]+,[a-zA-Z0-9]+\)"
	return(bool(re.search(regex, list)))


def listRegEx(list):
	regex = "\([a-zA-Z0-9]+,[a-zA-Z0-9]+\)"
	return(bool(re.search(regex, list)))


#gets list and edge passed through the terminal
def getArgs():
    if len(sys.argv) < 3:
        sys.stdout.write("Not enough arguments, please include list and edge\n")
        sys.exit()
    elif not listRegEx(sys.argv[1]) and not edgeRegEx(sys.argv[2]):
        sys.stdout.write("List or Edge arguments not in the correct format\n")
        sys.exit()
    else:
        return sys.argv[1], sys.argv[2]

#given a string, it will turn it into a list 
def parseList(input):
    out = []
    input.replace(" ", "")
    p = re.compile("\([a-zA-Z0-9]+,[a-zA-Z0-9]+\)") # make this so it doesnt have to be just 2 nodes!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
    p2 = re.compile("\w+")
    m = p.findall(input)
    for i in m:
        q = p2.findall(i)
        out.append((q[0], q[1]))
    return out

#given a string, it will turn it into a list of edges
def parseEdge(input):
    out = []
    input.replace(" ", "")
    p = re.compile("[a-zA-Z0-9]+")
    p2 = re.compile("\w+")
    m = p.findall(input)
    for i in m:
        q = p2.findall(i)
        out.append(q[0])
    return out

#makes the list fit in with the other argumants for the code
def makeEdges(dagList):
		DAG = [] 
		splitList = parseList(dagList)
		#print(splitList)
		for edge in splitList:
			if edge[0] == ' ': edge = edge[1:]
			if edge[len(edge)-1] == ' ': edge = edge[:len(edge)-1]
			DAG.append(edge)
			#print(edge)
		return DAG

def displayGraph(dag):
    graph = nx.DiGraph()
    graph.add_edges_from(dag)
    plt.tight_layout()
    nx.draw_networkx(graph, arrows=True,node_color="r")
    #saves the graph to the current directory
    plt.savefig("DAG.png", format="PNG")
    plt.clf()
    
def convex():
    DAG,l = getArgs()
    L = parseEdge(l)
    print("ARGS", DAG, L)
    dag = makeEdges(DAG)
    print(dag)
    displayGraph(dag)
    aliens = alien_neighbours(dag, L)
    LL = all_reachables_from(dag, aliens)
    ls = listintersect(L, LL)
    if isempty(ls):
        return True
    else:
        return False
    
def convex2(DAG, L):
    print("NOARGS", DAG, L)
    dag = makeEdges(DAG)
    aliens = alien_neighbours(dag, L)
    LL = all_reachables_from(dag, aliens)
    ls = listintersect(L, LL)
    if isempty(ls):
        return True
    else:
        return False


"""
>>> dag1 = [(1,2), (1,3), (1,4), (4,2), (4,5), (3,5)]
>>> convex(dag1, [1,5])
False
>>> convex(dag1, [2,4])
True
>>> dag2 = [(1,2), (2,3), (3,4), (2,4), (1,4)]
>>> convex(dag2, [1,3,4])
False
"""
dag1 = "[(aa,b), (aa,c), (aa,d) ,(d,b), (d,e) ,(c,e)]"
#dag1="[(1,2), (1,3), (1 ,4), (4 ,2), (4 ,5), (3 ,5)]"
print(convex2(dag1, ['aa','c','d'])) #false
#print(convex(dag1, ['b','d'])) #true
#print(makeEdges(dag1))

# add more documentation
# add users manual as part of the report
# add sample stuff
# On checking the convexity of a set of nodes in a directed graph
print(convex()) 

