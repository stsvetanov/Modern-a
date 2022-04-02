def range_equivalent(start, end=None, step=None):
    step = step if step is not None else 1
    value = start

    while end is not None and value < end:
        yield value
        value += step


for n in range_equivalent(2, 5):
    print(n)

gen_object = range_equivalent(1, 10)
print(gen_object)
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))

# with open('catalog_sample.csv', encoding='utf-8') as f:
#     # contents = f.read() # all content is loaded in memory
#     # print(contents)
#     print(f.__next__())
#     print(next(f))
#     for line in f:
#         print(line)
