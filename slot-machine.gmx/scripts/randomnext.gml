purple = 0
emerald = 1
banana = 2
cherry = 3
apple = 4
r = 96

a = random(100);

probp = 0.01;
probg = 4.49;
probf = 7.5;
//Purple
if (a <= probp) {
    global.win=true;
    trace("$,-50,3 Purple gems");
    p1 = purple;
    p2 = purple;
    p3 = purple;
} else if (a <= probg+probp) {
    global.win=true;
    trace("$,-5,3 Green gems");
    p1 = emerald;
    p2 = emerald;
    p3 = emerald;
} else if (a <= probf+probg+probp) {
    global.win=true;
    b = choose(1,2,3);
    if (b == 1) {
        trace("$,-2,3 Bananas");
        p1 = banana;
        p2 = banana;
        p3 = banana;
    }
    if (b == 2) {
        trace("$,-2,3 Cherries");
        p1 = cherry;
        p2 = cherry;
        p3 = cherry;
    }
    if (b == 3) {
        trace("$,-2,3 Apples");
        p1 = apple;
        p2 = apple;
        p3 = apple;
    }
} else {
    trace("$,0,User won nothing -1 tries");
    ex = irandom(4);
    ey = irandom(4);
    ez = irandom(4);
    while (eq(ex,ey,ez)) {
        ex = irandom(4);
        ey = irandom(4);
        ez = irandom(4);
    }
    p1 = ex;
    p2 = ey;
    p3 = ez;
}
ma = 5;
mi = 1;

spins = (irandom(ma) + mi)*5;
//1
n = p1-global.pos1 + spins;
Slot1.dist = r*n;
cop1.dist = r*n;
global.pos1 = p1;

//2
spins = (irandom(ma) + mi)*5;
n = p2-global.pos2 + spins;
Slot2.dist = r*n;
cop2.dist = r*n;
global.pos2 = p2;

//3
spins = (irandom(ma) + mi)*5;
n = p3-global.pos3 + spins;
Slot3.dist = r*n;
cop3.dist = r*n;
global.pos3 = p3;
