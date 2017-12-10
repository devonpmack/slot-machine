purple = 0
emerald = 1
banana = 2
cherry = 3
apple = 4
r = 96

p1 = banana;
p2 = purple;
p3 = emerald;

//1
n = p1-global.pos1;
if (n <= 0) {
    n += 5;
}
Slot1.dist = r*n;
cop1.dist = r*n;
global.pos1 = p1;

//2
n = p2-global.pos2;
if (n <= 0) {
    n += 5;
}
Slot2.dist = r*n;
cop2.dist = r*n;
global.pos2 = p2;

//3
n = p3-global.pos3;
if (n <= 0) {
    n += 5;
}
Slot3.dist = r*n;
cop3.dist = r*n;
global.pos3 = p3;

trace(Slot1.dist,Slot2.dist,Slot3.dist);
