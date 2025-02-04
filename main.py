from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.Parent = list(range(1, n + 1))
        self.Parent.insert(0, None)
        self.Size = [1] * n
        self.Size.insert(0, None)

    # Function to find the representative (or the root
    # node) for the set that includes i
    def find(self, i):
        if self.Parent[i] != i:
          
            # Path compression: Make the parent of i the
            # root of the set
            self.Parent[i] = self.find(self.Parent[i])
        return self.Parent[i]

    # Unites the set that includes i and the set that
    # includes j by size
    def unionBySize(self, i, j):
      
        # Find the representatives (or the root nodes) for
        # the set that includes i
        irep = self.find(i)

        # And do the same for the set that includes j
        jrep = self.find(j)

        # Elements are in the same set, no need to unite
        # anything.
        if irep == jrep:
            return

        # Get the size of i’s tree
        isize = self.Size[irep]

        # Get the size of j’s tree
        jsize = self.Size[jrep]

        # If i’s size is less than j’s size
        if isize < jsize:
          
            # Then move i under j
            self.Parent[irep] = jrep

            # Increment j's size by i's size
            self.Size[jrep] += self.Size[irep]
            
        # Else if j’s size is less than i’s size
        else:
          
            # Then move j under i
            self.Parent[jrep] = irep

            # Increment i's size by j's size
            self.Size[irep] += self.Size[jrep]
    
    def display_parents(self):
        for idx, parent in enumerate(self.Parent):
            if idx != 0:
                print(f"[{parent}]<-{idx}")
        print("=============================")
    
    def display_sizes(self):
        for idx, size in enumerate(self.Size):
            if idx != 0:
                print(f"Tamanho de {idx} é {size}")
        print("=============================")

number_of_nodes = 7
unionFind = UnionFind(number_of_nodes)

# Criando primeiro Set
unionFind.unionBySize(1, 3)
unionFind.display_parents()

# Criando sub-árvore da esquerda (2 e 4)
unionFind.unionBySize(2, 4)
unionFind.unionBySize(1, 2)
unionFind.display_parents()

# Criando sub-árvore verde
unionFind.unionBySize(5, 6)
unionFind.unionBySize(5, 7)
unionFind.display_parents()

# Unindo as sub-ávores verde e roxa
unionFind.unionBySize(1, 5)
unionFind.display_parents()

unionFind.display_sizes()

print(unionFind.find(5))
