

# returns a list of nbuckets
def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table

# returns hash for this string
def hash_string(keyword, buckets):
    h = 0
    for c in keyword:
        h = (h + ord(c)) % buckets
    return h

# given a hashtable, returns bucket where keyword would be located
def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]

# returns value associated with given key if key is present, else returns None
def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable, key)
    for item in bucket:
        if item[0] == key:
            return item[1]
    return None

# adds value to hashtable
def hashtable_add(htable,key,value):
    hashtable_get_bucket(htable,key).append([key,value])

# if key is not present, adds it to table. Else, updates keys value to new value.
def hashtable_update(htable,key,value):
    if not hashtable_lookup(htable, key) == None:
        bucket = hashtable_get_bucket(htable, key)
        for entry in bucket:
            if entry[0] == key:
                entry[1] = value
                break
    else:
        hashtable_add(htable, key, value)
    return htable