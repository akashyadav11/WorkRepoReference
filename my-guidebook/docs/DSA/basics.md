# Recursion 
--** A process that call itself 
helper recursionmethod helps in interation like array or list . it has outer and inner part for example 
function collectOddValues(arr){
    
    let result = [];

    function helper(helperInput){
        if(helperInput.length === 0) {
            return;
        }
        
        if(helperInput[0] % 2 !== 0){
            result.push(helperInput[0])
        }
        
        helper(helperInput.slice(1))
    }
    
    helper(arr)

    return result;
}

collectOddValues([1,2,3,4,5,6,7,8,9])


# Search
Linear Search : loops through array and compare the data one by one 
Binary Search : works on sorted array  

# sorting 
there is built in javascript sorting https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort

Bubble sort : A soritng where largest value bubble on top via swapping
Selection sort : pick smallest first 
Insertion sort : Builds ups sort by gradully creating a larger part always sorted .Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. 
Merge sort : 
Quick sort : 
Radix sort : Radix Sort is a linear sorting algorithm that sorts elements by processing them digit by digit. It is an efficient sorting algorithm for integers or strings with fixed-size keys
Singly Linked list: 


Stacks:used as invocation function , undo redo ,routing or history 


tree : when to user bfs or dfs 
heaps:type of tree :Maxheap,Minheap 
binary heap are used for priority queue as well

Priority queue 

hash table to store key value pair and it is not sorted, they are fast 

Graph 