def insert_into_heap(heap, x):
    heap.append(x)
    i=len(heap)-1
    while i>0:
        parent=(i-1)//2
        if heap[i]>heap[parent]:
            heap[i],heap[parent]=heap[parent],heap[i]
            i=parent
        else:
            break
    return heap
