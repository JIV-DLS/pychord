
import commons
from libraries import chord
nodes = commons.createlocalnodes(2,setfingers=True, stabilizer=True)
nodes[1].join(chord.NodeInterface(nodes[0].asdict()))
nodes.append((commons.createlocalnodes(1,setfingers=True, stabilizer=True)[0]))
nodes[2].join(chord.NodeInterface(nodes[0].asdict()))
print(*nodes,sep='\n')
commons.stoplocalnodes(nodes)
