
import collections
import networkx as nx
import matplotlib.pyplot as plt
import random
from operator import itemgetter
                #The Scafida Algorithm
"""
            Inputs
    n_t_0 — number of servers
    p_t_0 — number of servers’ port
    n_t_1,...,n_t_k — number of t_i type routers
    a_t_i — number of t_i type routes already allocated
    d_v— degree of the node v∈V
    m — number of links a newly added node has
"""
n_t_0 = 2
p_t_0 = 100
n_t = [ 15,30 , 53, 2]
p_t =[4, 8, 16, 32]
m=3
k=3

# initialize an empty graph
G = nx.Graph()
# add initial nodes
G.add_nodes_from([i for i in range(m)])
# initialize a_t_i
a_t = [0 for i in range(k+1)]

R = [] #used for preferential attachments
R = R + list(G.nodes())
G.add_edges_from([(m,i) for i in list(G.nodes())])
R = R + [m for i in range(m)] # update the list index
b= m + 1 # index of next node
# print(R , G.nodes(), G.edges()) #checkpoint

# total number of nodes to add
total=0
for i in n_t:
    total= total + i

while(b < total):
    G.add_node(b)
    T = [] # to store the selected target nodes
    while(len(T) < m):
        val= True
        while(val):
            v_t = random.choice(R)
            if v_t not in T:
                val = False
        d_v_t = G.degree(v_t)
        if d_v_t not in p_t:
            T = T + [v_t]
            G.add_edge(b,v_t)
        else:
            i=p_t.index(d_v_t)
            nasw = 0
            ntsw = 0
            for j in range(k+1):
                if p_t[j] > p_t[i]:
                    nasw += a_t[j]
                    ntsw += n_t[j]
            if nasw < ntsw:
                a_t[i] = a_t[i] - 1
                a_t[i+1] = a_t[i+1] + 1
                T = T + [v_t]
                G.add_edge(b,v_t)
            else:
                R.remove(v_t)
    R = R + T
    for i in range(m):
        R = R + [b]
    b = b + 1



nx.draw(G, node_size= 10)
plt.show()

                #END#


            #print average_shortest_path_length
print(nx.average_shortest_path_length(G, weight="none"))


                    # find node with largest degree
'''
node_and_degree = G.degree()
(largest_hub, degree) = sorted(node_and_degree, key=itemgetter(1))[-1]
# Create ego graph of main hub
hub_ego = nx.ego_graph(G, largest_hub)
# Draw graph
pos = nx.spring_layout(hub_ego)
nx.draw(hub_ego, pos, node_color='b', node_size=50, with_labels=False)
# Draw ego as large and red
nx.draw_networkx_nodes(hub_ego, pos, nodelist=[largest_hub], node_size=300, node_color='r')
plt.show()
'''


                            #degree distribution
'''
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# print "Degree sequence", degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color='b')

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)

# draw graph in inset
plt.axes([0.4, 0.4, 0.5, 0.5])
Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
pos = nx.spring_layout(G)
plt.axis('off')
nx.draw_networkx_nodes(G, pos, node_size=20)
nx.draw_networkx_edges(G, pos, alpha=0.4)

plt.show()
'''
