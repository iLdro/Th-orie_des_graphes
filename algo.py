def has_cycle(graphe):
    visited = set()
    path = set()
    for node in graphe:
        a = set()
        b = set()
        visited.add(node.name)
        path.add(node.name)
        for parent in node.dependencies:
            print("yes")
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
                b = True
        else:
            b = False
    return b


def check_arc_value(graphe):
    """Valeurs identiques pour tous les arcs incidents vers l’extérieur à un sommet"""


def check_arc_entry(graphe):
    """Arcs incidents vers l’extérieur au point d’entrée ont une valeur nulle"""
    for node in graphe:
        if node.name == '0':
            for parent in node.dependencies:
                if parent.duration != 0:
                    return False
    return True


def check_negative_arc(graphe):
    """Arcs avec une valeur négative"""
    for node in graphe:
        for _ in node.dependencies:
            if node.duration < 0:
                return False
    return True


def calendar(graphe):
    """Algrithme de calcul du calendrier"""
    for node in graphe:
        for parent in node.dependencies:
            if parent.name == '0':
                node.duration = node.duration
            else:
                node.duration = max(node.duration, parent.duration + node.duration)
    return graphe