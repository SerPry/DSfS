

def vector_add(v,w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v,w):
    return [v_i - w_i for v_i, w_i in zip(v,w)]


def vector_sum(vectors):
    return reduce(vector_add, vectors)

v1 = [1,2]
v2 = [2,1]
print(vector_add(v1,v2))


