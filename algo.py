def has_cycle(graphe):
    visited = set()
    path = set()
    for node in graphe:
        a = set()
        visited.add(node.name)
        path.add(node.name)
        for parent in node.dependencies:
            if parent not in visited:
                if a:
                    a = True
            elif parent in path:
                a = True
            else:
                a = False
        path.remove(node.name)
        if node.name not in visited:
            if a:
                return True
        else:
            return False
