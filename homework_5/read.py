class ReverseFileIterator:
    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        with open(self.file_path, 'rb') as file:
            file.seek(0, 2)
            file_size = file.tell()
            buffer = bytearray()
            position = file_size

            while position >= 0:
                file.seek(position)
                char = file.read(1)
                position -= 1

                if char == b'\n':
                    yield buffer.decode('utf-8')[::-1]
                    buffer.clear()
                else:
                    buffer.extend(char)

            if buffer:
                yield buffer.decode('utf-8')[::-1]


file_path = 'example.txt'

for line in ReverseFileIterator(file_path):
    print(line)
