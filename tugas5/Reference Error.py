import gc as g
import weakref as wk
class check_Object(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print ('Delete it %s') % self
obj_check = check_Object('object')
abc = wk.proxy(obj_check)
print('Before deleting =', abc.name)
obj_check  = None
print('After deleting = ', abc.name)