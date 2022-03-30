from numpy import Inf


''' Breath First Search
    Dijkstra's Algorithm
'''

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

djGraph = {}
djGraph['you'] = [['alice'], ['bob'], ['claire']]
djGraph['bob'] = [['anuj'], ['peggy']]
djGraph['alice'] = [['peggy']]
djGraph['claire'] = [['thom'], ['jonny']]
djGraph['anuj'] = []
djGraph['peggy'] = []
djGraph['thom'] = []
djGraph['jonny'] = []


START = 'you'
END = 'jonny'

def BreathFirstSearch(graph):

    searchQueue = [[START]]
    searched = []

    while searchQueue:
        path = searchQueue.pop(0)
        cur = path[-1]
        if cur not in searched:
            if cur == END:
                print('Found')
                print(path)
                return path
            else:
                for i in graph[cur]:
                    newPath = path[:]
                    newPath.append(i)
                    searchQueue.append(newPath)
            searched.append(cur)

    if not searchQueue:
        print('Not Found')


def Dijkstras(graph):
    parents = {}
    costs = {}
    for i in graph.keys():
        parents[i] = []
        costs[i] = []

    


BreathFirstSearch(graph)
Dijkstras()