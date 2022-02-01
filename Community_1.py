import networkx as nx
import matplotlib.pyplot as plt
# G = nx.karate_club_graph()
# print(G)
# nx.draw(G,with_labels=True)
f = open('/home/alirezakhn17/Documents/AI project/sample dataset.txt')
def initialize_graph()->list:
    ans_list = list()
    n = int(f.readline())
    for i in range(n):
        ans_list.append(i+1)
    return ans_list,n

def get_edges(n:int):
    answer_list = list()
    str_nodes = f.readline()
    while str_nodes != "":
        split_nodes = str_nodes.split(" ")
        tuple_i = (int(split_nodes[0]),int(split_nodes[1]))
        answer_list.append(tuple_i)
        str_nodes = f.readline()
    return answer_list


def edge_to_remove(graph):
  G_dict = nx.edge_betweenness_centrality(graph)
  edge = ()
  # extract the edge with highest edge betweenness centrality score
  for key, value in sorted(G_dict.items(), key=lambda item: item[1], reverse = True):
      edge = key
      break

  return edge


def girvan_newman(graph):
	# find number of connected components
	sg = nx.connected_components(graph)
	sg_count = nx.number_connected_components(graph)

	while(sg_count == 1):
		graph.remove_edge(edge_to_remove(graph)[0], edge_to_remove(graph)[1])
		sg = nx.connected_components(graph)
		sg_count = nx.number_connected_components(graph)

	return sg



# n =  int(input())
list_of_nodes,n = initialize_graph()
# print(list_of_nodes)
G = nx.Graph()
G.add_nodes_from(list_of_nodes)
edges = get_edges(n)
G.add_edges_from(edges)
c = girvan_newman(G.copy())
node_groups = []
for i in c:
  node_groups.append(list(i))
color_map = []
color_map1 =  ['blue', 'green', 'red', 'cyan', 'magneta', 'yellow', 'black', 'white']
i = 0
if len(node_groups) > len(color_map1):
    # for i in range(len(node_groups)):
      # color_map.append(color_map1[i])
    print(node_groups)
    nx.draw(G, with_labels=True)
    plt.show()
else:
    for node in G:
        for i in range(len(node_groups)):
            if node in node_groups[i] :
                color_map.append(color_map1[i])  
    nx.draw(G, with_labels=True , node_color = color_map)
    plt.show()
    # if node in node_groups[0]:
    #     color_map.append('blue')
    # else: 
    #     color_map.append('green')  
# nx.draw(G, node_color=color_map, with_labels=True)
