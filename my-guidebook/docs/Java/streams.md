Pipeline from which our collection passes through and performs various operations and used for bulk processing.
## 
three steps are involved : 1 .Create Stream ,2.intermidate operation and 3.terminal operation (collect,reduce,count etcs) 
and close the stream.  for example long output=Salarylist.stream().filter((Integer sal)->sal>3000).count();
#### Ways to create stream
From collection
From Arrays
From static method like stream.of();
using stream builder like Stream.builder().build
from stream iterate like stream.iterate(seed:,limit)

### Intermediate operations:
1 Map  
2 FlatMap  
3 distinct  
4 sorted
5 peek : help you to see the intermiadate result of the stream which is getting processed
6 limit 
7 skip
8 maptoInt
9 maptoLong
10 maptoDouble

### Terminal operations
for Each 
toArray
reduce
collect 
min
max
count
anymatch
allmatch
noneMatch
findFirst
findany

