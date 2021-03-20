from collections import Counter
from collections import namedtuple
from collections import deque
c=Counter("greedy")
c_one=Counter([1,2,3,4])
c_2=Counter(a=4,b=3,c=2)

point=namedtuple("point",['x','y','z'])
newp=point(1,2,3)
point_two=namedtuple("point2",'x y z')
p_two=point_two([1,2,3],1,2)


d=deque('greedy')
d.append('g')
d.reverse()
d.appendleft('gg')
print(d.count('g'))
print(d)
