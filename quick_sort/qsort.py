def qsort_rec(lst):
    match lst:
        case []: return []
        case _: return qsort_rec(list(filter(lambda x: x < lst[0], lst[1:]))) + lst[0:1] + qsort_rec(list(filter(lambda x: x >= lst[0], lst[1:])))


#def qsort_imp(lst):
