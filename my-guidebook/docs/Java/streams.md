Pipeline from which our collection passes through and performs various operations and used for bulk processing.
## 
three steps are involved : 1 .Create Stream ,2.intermidate operation and 3.terminal operation (collect,reduce,count etcs) 
and close the stream.  for example long output=Salarylist.stream().filter((Integer sal)->sal>3000).count();
#### Ways to create stream