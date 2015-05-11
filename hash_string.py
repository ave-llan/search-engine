# given a hashtable, returns bucket where keyword would be located
def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]

# returns hash for this string
def hash_string(keyword, buckets):
    h = 0
    for c in keyword:
        h = (h + ord(c)) % buckets
    return h

# returns a list of nbuckets
def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table