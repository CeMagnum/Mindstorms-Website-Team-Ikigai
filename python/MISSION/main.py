#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import SoundFile
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

LM = Motor(Port.D)
RM = Motor(Port.A)
BONK = Motor(Port.C)
LS = ColorSensor(Port.S3)
USS = UltrasonicSensor(Port.S4)

R = 3
W = 62
TH = (R + W) / 2
DS = 50    
PG = 5.2
IG = 0.008
DG = 0.001
I = 0
D = 0
LE =0

ev3 = EV3Brick()
ev3.speaker.beep()
ev3.speaker.set_volume(200)

while True:
    E=LS.reflection()-TH
    I=I+E
    D=E-LE
    TR=PG*E+IG*I+DG*D
    LM.run(DS+TR)
    RM.run(DS-TR)
    LE=E
    while USS.distance() <= 100:
        BONK.run(-1000)
        ev3.speaker.say("mooda")
    while USS.distance() >= 100:
        BONK.run(0)
        break
    wait(10)
