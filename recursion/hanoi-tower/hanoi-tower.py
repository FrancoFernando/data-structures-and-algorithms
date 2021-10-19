class Peg:
    name = ""
    disks = []
    def __init__(self, _name, _size):
        self.name = _name
        self.disks = [i for i in range(_size, 0, -1)]

    def addRing(self, ring):
        self.disks.append(ring)
        
    def removeRing(self):
        self.disks.pop()
        
    def moveRing(self, destination):
        disk = self.disks[-1]
        self.removeRing()
        destination.addRing(disk)
        print("Move " + str(disk) + " from Peg " + self.name
            + " to Peg " + destination.name)
            
def HanoiTowers(height, src, dst, tmp):
    if height >= 1:
        HanoiTowers(height-1, src, tmp, dst)
        src.moveRing(dst)
        HanoiTowers(height-1, tmp, dst, src)

def main():
	n_disks = 5
    pegs = [Peg("A",n_disks),Peg("B",0),Peg("C",0)]
    HanoiTowers(n_disks, pegs[0], pegs[1], pegs[2])
