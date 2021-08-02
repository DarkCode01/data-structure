class Graph():
    """
    space of complexity if adjacency matrix
    O(n^2)
    """
    def __init__(self, matrixSize):
        self.matrix = []
        for i in range(matrixSize):
            self.matrix.append([0 for i in range(matrixSize)])
        self.matrixSize = matrixSize

    def addEdge(self, node1, node2):
        self.matrix[node1][node2] = 1
        self.matrix[node2][node1] = 1

    def deeleteEdge(self, node1, node2):
        if self.matrix[node1][node2]:
            self.matrix[node1][node2] = 0
            self.matrix[node2][node1] = 0


