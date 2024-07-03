class Cat:
    def __init__(self, name):
        self._name = name
    
    property
    def name(self):
        return self._name
    

def test():
    cats = [Cat("Tom"), Cat("Lorry"), Cat("Lucky")]
    cats_names = [cat.name() for cat in cats]
    print(cats_names)

if __name__ == '__main__':
    test()
