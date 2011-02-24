import os
from minitage.core.common import which
def h(options,buildout):
    make = "gmake"
    try:
        make = which("gmake")
    except:
        make = "make"
    os.environ['MAKE'] = make

# vim:set ts=4 sts=4 et  :
