import os

import shellinford


class MultiStorage:
    def __init__(self, path: str):
        self.path = path
        self.ext = "fm"
        self.db = dict()
        self.init()

    def init(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        names = [
            pathname
            for pathname in os.listdir(f"{self.path}")
            if pathname.endswith(f".{self.ext}")
        ]
        for name in names:
            self.db[name] = \
                shellinford.FMIndex(use_wavelet_tree=True, filename=f"{self.path}/{name}")

    def search(self, query='я шагаю по москве'):
        prompt = str(query).split(" ")
        for fm in self.db:
            for doc in self.db[fm].search(prompt):
                print('doc_id:', doc.doc_id)
                print('count:', doc.count)
                # print('text:', doc.text)
            break
        return 0
