#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Peg {
    string name;
    vector<int> disks;
    Peg(string _name, int _size) {
        name = _name;
        for (int i = _size; i >= 1; --i) disks.push_back(i);
    }
    void addRing(int ring) { disks.push_back(ring); }
    void removeRing() { disks.pop_back(); }
    void moveRing(Peg& destination) {
        int disk = disks.back();
        removeRing();
        destination.addRing(disk);
        cout << "Move " << disk << " from Peg " << name
            << " to Peg " << destination.name << "\n";
    }
};

void HanoiTowers(int height, Peg& src, Peg& dst, Peg& tmp) {

    if (height >= 1) {
        HanoiTowers(height - 1, src, tmp, dst);
        src.moveRing(dst);
        HanoiTowers(height - 1, tmp, dst, src);
    }
}

int main() {
	
	int n_disks = 5;
	vector<Peg> pegs{{"A",n_disks},{"B",0},{"C",0}};
	HanoiTowers(n_disks, pegs[0], pegs[1], pegs[2]);
}