def cached_execution(cache, proc, proc_input):
    if not proc_input in cache:
        cache[proc_input] = proc(proc_input)
    return cache[proc_input]

def cached_fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return (cached_execution(cache, cached_fibo, n - 1 )
               + cached_execution(cache,  cached_fibo, n - 2 ))

cache = {}
print cached_execution(cache, cached_fibo,100)