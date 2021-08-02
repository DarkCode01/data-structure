class MinHeap:
    def __init__(self):
        self.heap = []
        self.heap_size = 0

    def getParentNodeIndex(self, i: int):
        return (i - 1) // 2

    def getLeftChildNodeIndex(self, i: int):
        return 2 * i + 1

    def getRightChildNodeIndex(self, i: int):
        2 * i + 2

    def hasParent(self, i: int) -> bool:
        return self.getParentNodeIndex(i) < len(self.heap)

    def hasLeftChild(self, i: int) -> bool:
        return self.getLeftChildNodeIndex(i) < len(self.heap)

    def hasRigthChild(self, i: int) -> bool:
        return self.getRightChildNodeIndex(i) < len(self.heap)

    def getMinValue(self) -> int:
        return self.heap[0]

    def printAll(self):
        print(self.heap)

