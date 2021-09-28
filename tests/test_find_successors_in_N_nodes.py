
import commons
from libraries import chord
import os
current_nodes = None
def run():
    global current_nodes
    if not current_nodes: return
    print("finded",current_nodes[0].find_successor(current_nodes[1].uid))
    commons.stoplocalnodes(current_nodes)
    current_nodes = None
def init(nodes_number):
    global current_nodes
    print('Building',nodes_number,'nodes:')
    nodes = commons.createlocalnodes(2,setfingers=os.environ.get("SET_FINGERS",False), stabilizer=os.environ.get("SET_STABILIZER",False))
    nodes[1].join(chord.NodeInterface(nodes[0].asdict()))
    for _ in range(nodes_number-2):
        nodes.append((commons.createlocalnodes(1,setpredecessor=True,setfingers=True, stabilizer=True)[0]))
        nodes[-1].join(chord.NodeInterface(nodes[0].asdict()))
    current_nodes = nodes

if __name__ == '__main__':
    import timeit
    init(int(os.environ.get("NODES_SIZE",5)))
    print(timeit.timeit("run()", setup="from __main__ import run"))
    """import numpy as np
    from tqdm import tqdm
    node_tests_size = [5]#,10,15,50,100]
    general_results = [[node_tests_size]]
    node_tests_size_lenght = len(node_tests_size)
    for i in range(10):
        general_results.append([0 for _ in range(node_tests_size_lenght)])
        
    for i,node_size in enumerate(node_tests_size):
        init(node_size)
        for j in tqdm(range(1)):
            general_results[j+1][i]=timeit.timeit("run()", setup="from __main__ import run")
    
    a = np.array(general_results)
    np.savetxt('result.csv', a, delimiter=',')"""
    #print(timeit.timeit("test()", setup="from __main__ import test"))
    #print(timeit.timeit("test()", setup="from __main__ import test"))
    #print(timeit.timeit("test()", setup="from __main__ import test"))
    #print(timeit.timeit("test()", setup="from __main__ import test"))

    # For Python>=3.5 one can also write:
    #print(timeit.timeit("test()", globals=locals()))