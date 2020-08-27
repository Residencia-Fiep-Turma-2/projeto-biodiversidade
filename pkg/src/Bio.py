class Bio:
    sep = ";"

    def __init__(self, path):
        self.path = path
        self.data = self.open_()

    def open_(self):
        f = open(self.path, "r")
        data = f.readlines()
        f.close()

        for i in range(len(data)):
            data[i] = data[i].replace("\n", "").split(";")

        return data
