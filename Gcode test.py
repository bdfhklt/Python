import math

gcode = ""
center = 150

def sin(a): return round(math.sin(math.radians(a)), 3)
def cos(a): return round(math.cos(math.radians(a)), 3)

# 360도 테스트
def speedTestXY360(speedMin, speedMax, step):
    gcode = ""
    for s in range(speedMin, speedMax, step):
        gcode += "M117 speed {}\n".format(s)
        gcode += "G4 S1\n"
        m = 0
        if s < 120:
            m = s
        else:
            m = 120
        for d in range(36):
            gcode += "G0 F{} X{} Y{}\n".format(s * 600, round(center + (cos(d * 5) * m), 3), round(center + (sin(d * 5) * m), 3))
            gcode += "G0 F{} X{} Y{}\n".format(s * 600, round(center - (cos(d * 5) * m), 3), round(center - (sin(d * 5) * m), 3))
        gcode += "G0 F3000 X{0} Y{0}\n".format(center)
        gcode += "G4 P200\n"
    gcode += "M117 end\n"
    return gcode

# X, Y 개별 테스트
def speedTestXY(xy, speedMin, speedMax, step):
    gcode = ""
    gcode += "G4 S1\n"
    for speed in range(speedMin, speedMax, step):
        gcode += "M117 speed {}: {}\n".format(xy, speed)
        distance = 0
        if speed < 120:
            distance = speed
        else:
            distance = 120
        gcode += "G0 F12000 {}{}\n".format(xy, center - distance)
        gcode += "G4 P100\n"
        gcode += "G0 F{} {}{}\n".format(speed * 60, xy, center + distance)
        gcode += "G0 F{} {}{}\n".format(speed * 60, xy, center - distance)
        gcode += "G4 P100\n"
    gcode += "G0 F12000 {}{}\n".format(xy, center)
    gcode += "M117 end\n"
    return gcode

# M204: 가속도, M205: X저크 Y저크
gcode += "M204 S800\nM205 X8 Y8\nG0 F6000 X{0} Y{0} Z1\n".format(center)
speedMin = 20
speedMax = 100 + 1
step     = 5
# gcode += speedTestXY360(speedMin, speedMax, step)
gcode += speedTestXY("X", speedMin, speedMax, step)
gcode += speedTestXY("Y", speedMin, speedMax, step)

with open('./Gcode_test.gcode', 'w') as f:
    f.write(gcode)
