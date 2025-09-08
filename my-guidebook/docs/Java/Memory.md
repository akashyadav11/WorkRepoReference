types of Memory:
    1.Stack:  
    Stores temporary variables and separate memory block for methods
    Stores primitive data types 
    stores reference of heap objects 
    each thread has its own stack memory 
    variables within a scope is only visible and as soon any variables goes out of scope it gets deleted from the stack(LIFO order)
    new() -creates memory in heap and refernce in stack(there are 3 type of reference(Strong,weak and soft))
    String is stored in string pool inside heap
    garbage collector is used to delete unreferenced object from the heap
    Strong Reference: Person p=new Person(); 
    WeaK Reference : if gc runs it will be freed 
    Soft reference : do it when if urgent need of memory is required 
    2.heap Memory :
    

