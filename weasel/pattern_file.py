class PatternFile(object):
    def __init__(self, filename):
        self.closed = True
        self.filepointer = open(filename, 'r')
        self.closed = False

    def __del__(self):
        self.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def read(self):
        patterns = []
        for line in self.filepointer:
            pattern = line.rstrip()
            if len(pattern) == 0 or (len(pattern) > 0 and pattern[0] == '#'):
                continue
            patterns.append(pattern)

        return patterns

    def close(self):
        if not self.closed:
            self.filepointer.close()
        self.closed = True
