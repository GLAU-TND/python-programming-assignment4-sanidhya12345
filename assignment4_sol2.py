def sdict(p, str=''):
    if type(p) is dict:
        if type(p) is dict:
            str = str + "." if str else str
            for k in p:
                yield from sdict(p[k], str + k)

        elif (type(p) is list):
            for i in p:
                yield from sdict(i, str)
    else:
        yield str, p

ini_dict = {
 "key": 3,
 "foo": {
 "a": 5,
 "bar": {
 "baz": 8
 }
 }
}
res = {k: v for k, v in sdict(ini_dict)}
print(str(res))
