def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            # value = new
            value = 'look good!'


r = repeater(42)
print(next(r))
print(next(r))
print(r.send('Hello,World!'))
print(next(r))
# print(r.send(None))
