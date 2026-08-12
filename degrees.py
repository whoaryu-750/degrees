def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no path exists, returns None.
    """

    if source == target:
        return []

    start = Node(source, None, None)
    frontier = QueueFrontier()
    frontier.add(start)

    explored = set()

    while not frontier.empty():
        node = frontier.remove()
        explored.add(node.state)

        for movie_id, person_id in neighbors_for_person(node.state):
            if person_id in explored:
                continue

            child = Node(person_id, node, movie_id)

            if person_id == target:
                path = []

                while child.parent is not None:
                    path.append((child.action, child.state))
                    child = child.parent

                path.reverse()
                return path

            frontier.add(child)

    return None
