print("LA8")

class book:
    def __init__(self, title,author):
        self.title = title
        self.author = author
        
x = book("the adventure of john pol", "pol")
y = book("daniel","pol")
print(f"{x.title}, {x.author}")
del x.author
print(f"{y.title}, {y.author}")
