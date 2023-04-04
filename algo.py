def detect_cycle(graph):
    nodes = list(graph.graph)
    while nodes:
        # Trouver les points d'entrée (pas de dépendances)
        entry_nodes = [node for node in nodes if not any(node in task.dependencies for task in nodes)]

        # S'il n'y a pas de points d'entrée, il y a un cycle
        if not entry_nodes:
            return True

        # Supprimer les points d'entrée de la liste des nœuds
        for entry_node in entry_nodes:
            nodes.remove(entry_node)

            # Supprimer les liens vers les points d'entrée supprimés
            for node in nodes:
                if entry_node in node.dependencies:
                    node.dependencies.remove(entry_node)

    return False

