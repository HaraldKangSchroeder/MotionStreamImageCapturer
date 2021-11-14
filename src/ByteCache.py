class ByteCache:

    def __init__(self):
        self.bytes = [b'-', b'-']

    def update(self, byte):
        self.bytes.append(byte)
        self.bytes.pop(0)

    def get_bytes(self):
        return self.bytes
