import uuid


class UniqueIDIterator:
    def __iter__(self):
        return self

    def __next__(self):
        return str(uuid.uuid4())


id_generator = UniqueIDIterator()

for _ in range(5):
    print(next(id_generator))
