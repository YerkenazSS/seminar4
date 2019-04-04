class MaxHeap:
	# Create a max-heap with maximum capacity of maxSize.
def __init__( self, maxSize ):
	self._elements = Array( maxSize )
	self._count = 0

		# Return the number of items in the heap.
def __len__( self ):
	return self._count

		# Return the maximum capacity of the heap.
def capacity( self ):
	return len( self._elements )


def simpleHeapSort( theSeq ):
		# Create an array-based max-heap.
	n = len(theSeq)
	heap = MaxHeap( n )
		# Build a max-heap from the list of values.
	for item in theSeq :
	    heap.add( item )
		# Extract each value from the heap and store them back into the list.
	for i in range( n, 0, -1 ) :
	    theSeq[i] = heap.extract()
