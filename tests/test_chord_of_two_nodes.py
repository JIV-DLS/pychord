
import commons
from libraries import chord
nodes = commons.createlocalnodes(2, stabilizer=False)
nodes[1].join(chord.NodeInterface(nodes[0].asdict()))
print(*nodes,sep='\n')
commons.stoplocalnodes(nodes)