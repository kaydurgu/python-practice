class FileAcceptor:
    def __init__(self, *exts) -> None:
        self.exts = exts
    
    def __call__(self, smth : str, *args, **kwds):
        return smth.endswith(self.exts)

    def __add__(self, other):
        return FileAcceptor(*self.exts, *other.exts)

filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
