"""
Simple graph implementation
"""
class Queue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return (len(self.queue))


class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return (len(self.stack))


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")

# SOLUTION ---------------------------------------------------
    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Queue
        q.enqueue(starting_vertex_id)
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first node from the queue
            v = q.dequeue()
            # If that node has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

# SOLUTION ---------------------------------------------------
    def dft(self, starting_vertex_id):
        # Create an empty queue
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Queue
        s.push(starting_vertex_id)
        # While the queue is not empty
        while s.size() > 0:
            # Dequeue the first node from the queue
            v = s.pop()
            # If that node has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the queue
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
    
    def dft_r(self, starting_vertex_id, path = []):
        path.append(starting_vertex_id)

        for neighbor in self.vertices[starting_vertex_id]:
            if neighbor not in path:
                path = self.dft_r(neighbor, path)
        
        return path

# SOLUTION --------------------------------------------------- 
    def dft_r_brady(self, starting_vertex_id, visited=None):
        if visited == None:
            visited = set()
        # Mark the starting node as visted
        print(starting_vertex_id)
        visited.add(starting_vertex_id)
        print(f'visited: {visited}') 
        # Then call dft_r() on each unvisited neighbor
        for neighbor in self.vertices[starting_vertex_id]:
            if neighbor not in visited:
                self.dft_r_brady(neighbor, visited)

    def bfs(self, start, destination):
         # Create an empty queue
        q = Queue()
        # Create an empty set of visited vertices
        visited = []
        # Put the starting vertex in our Queue
        q.enqueue(start)
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first node from the queue
            v = q.dequeue()
            # If that node has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.append(v)
                if v == destination:
                    return visited
                # Then, put all of it's children into the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
        return f'No path to: {destination}'

# SOLUTION ---------------------------------------------------
    def bfs_brady(self, starting_vertex_id, target_id):
        # Create an empty queue
        q = Queue()
        # Create an empty set of visited vertices
        visited = set()
        # Put the path of the starting vertex in our Queue
        q.enqueue([starting_vertex_id])
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first path from the queue
            path = q.dequeue()
            # Get the current node from the last element in the path
            v = path[-1]
            # If that node has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Check if it's our taget
                if v == target_id:
                    return path
                # Then, put paths all of it's children into the queue
                for neighbor in self.vertices[v]:
                    # Copy the path into a new instance
                    new_path = list(path)
                    # Append the neighbor to the end of the path
                    new_path.append(neighbor)
                    # Enqueue
                    q.enqueue(new_path)


    def dfs(self, start, destination):
         # Create an empty queue
        s = Stack()
        # Create an empty set of visited vertices
        visited = []
        # Put the starting vertex in our Queue
        s.push(start)
        # While the queue is not empty
        while s.size() > 0:
            # Dequeue the first node from the queue
            v = s.pop()
            # If that node has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.append(v)
                if v == destination:
                    return visited
                # Then, put all of it's children into the queue
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
        return f'No path to: {destination}'

# SOLUTION ---------------------------------------------------
    def dfs_brady(self, starting_vertex_id, target_id):
        # Create an empty stack
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()
        # Put the path of the starting vertex in our Queue
        s.push([starting_vertex_id])
        # While the queue is not empty
        while s.size() > 0:
            # Dequeue the first path from the queue
            path = s.pop()
            # Get the current node from the last element in the path
            v = path[-1]
            # If that node has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Check if it's our taget
                if v == target_id:
                    return path
                # Then, put paths all of it's children into the queue
                for neighbor in self.vertices[v]:
                    # Copy the path into a new instance
                    new_path = list(path)
                    # Append the neighbor to the end of the path
                    new_path.append(neighbor)
                    # Enqueue
                    s.push(new_path)   
