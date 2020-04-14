# get the parents (like neighbors)
        # recurse on the parents to get their parents
        # go as deep as we can on each parent
        # keep track of the depth
        #   if the path we've built is longer the current longest path update the longest path
        #   if the lengths are the same return the smaller of the two ancestors
        # return the last element of the path
    

def earliest_ancestor(ancestors, starting_node):
    # check if the node we started with has no parents
    # keep track if our node has no parents
    no_parents = True
    for elem in ancestors:
        # elem is a tuple of shape (ancestor, child), so elem[1] is the child
        # if the child matches our current child, recurse on the parent, elem[0]
        if elem[1] == starting_node:
            # flag that we've found a parent
            no_parents = False
    # return -1 if our starting node is the ancient ancestor
    if no_parents:
        return -1

    deepest_depth = 0
    def earliest_ancestor_util(ancestors, starting_node, ancient_ancestor=None, depth=None):
        nonlocal deepest_depth
        if ancient_ancestor == None:
            ancient_ancestor = float("inf")
        if depth == None:
            depth = 0

        # keep track if our node has no parents
        no_parents = True
        for elem in ancestors:
            # elem is a tuple of shape (ancestor, child), so elem[1] is the child
            # if the child matches our current child, recurse on the parent: elem[0]
            if elem[1] == starting_node:
                # flag that we've found a parent
                no_parents = False
                depth += 1
                ancient_ancestor = earliest_ancestor_util(ancestors, elem[0],ancient_ancestor=ancient_ancestor, depth=depth)
                depth -= 1
            
        # once we've gotten to the end of one line, we check if we are on a longest path
        if no_parents:
            if depth > deepest_depth:
                ancient_ancestor = starting_node
                deepest_depth = depth
            elif depth >= deepest_depth:
                if starting_node < ancient_ancestor:
                    ancient_ancestor = starting_node

        return ancient_ancestor
    
    ancient_ancestor = earliest_ancestor_util(ancestors, starting_node)
    return ancient_ancestor


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
start = 3

earliest_ancestor(ancestors, start)

