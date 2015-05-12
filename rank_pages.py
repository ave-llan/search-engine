# returns a dictionary of page rankings
def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10 # number of levels to check

    ranks = {}
    npages = len(graph) # of pages in graph
    for page in graph:
        ranks[page] = 1.0 / npages # initialize each rank to 1/npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages # chance user randomly arrives here
            # update by summing in the inlink ranks
            for inlink in ranks:
                if page in graph[inlink]: # if this is an inlink to this page
                    # add: damper * rank[previous loop] / number of outlinks from inlink
                    newrank += d * ranks[inlink] / len(graph[inlink])
            newranks[page] = newrank
        ranks = newranks
    return ranks