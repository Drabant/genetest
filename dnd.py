import object

class Character(object.Human):
    a_str = None
    a_str_super = None
    a_dex = None
    a_con = None
    a_int = None
    a_wis = None
    a_cha = None

    def __init__(self, **kwargs):
        super(Character, self).__init__(**kwargs)
        self.__calcabilities()

    def getgene(self, pair, offset, length):
        pair = self.genes[pair]
        if pair[0] > pair[1]:
            active = 0
        else:
            active = 1
        return (pair[active] >> offset) & ~(~0 << length)

    def __calcabilities(self):
        self.a_str = sum([self.getgene(i, 0, 16) % 6 + 1 for i in range(0,3)])
        if self.a_str == 18:
            self.a_str_super = sum([self.getgene(i, 16, 16) for i in range(0,3)]) % 100 + 1
        self.a_dex = sum([self.getgene(i, 0, 16) % 6 + 1 for i in range(3,6)])
        self.a_con = sum([self.getgene(i, 0, 16) % 6 + 1 for i in range(6,9)])
        self.a_int = sum([self.getgene(i, 0, 16) % 6 + 1 for i in range(9,12)])
        self.a_wis = sum([self.getgene(i, 0, 16) % 6 + 1 for i in range(12,15)])
        self.a_cha = sum([self.getgene(i, 0, 16) % 6 + 1 for i in range(15,18)])

    def printsheet(self):
        if self.a_str_super is not None:
            print("Str:", str(self.a_str) + '/' + str(self.a_str_super))
        else:
            print("Str:", self.a_str)
        print("Dex:", self.a_dex)
        print("Con:", self.a_con)
        print("Int:", self.a_int)
        print("Wis:", self.a_wis)
        print("Cha:", self.a_cha)
