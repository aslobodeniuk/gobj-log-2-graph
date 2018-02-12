# usage :
# $ cat file.log | python gobj-log-2-graph.py > mygraph.dot
# $ dot -Tsvg mygraph.dot mygraph.svg
#
# if something:
# dot is in graphviz package
# apt install graphviz

import re
import fileinput

# 'obj' : 'parent'
di = {}

print 'digraph {'

for line in fileinput.input():
    mobj = re.match(r".*<(.*)> child '(.*)'.*", line)
    if mobj:
        di[mobj.group(2)] = mobj.group(1)

for ke in di:
    print '"',di[ke],'"' , '->', '"',ke,'";'

print '}'
