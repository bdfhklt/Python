import math

gcode = ""
center = 150

def sin(a): return round(math.sin(math.radians(a)), 3)
def cos(a): return round(math.cos(math.radians(a)), 3)

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

def speedTestXY(xy, speedMin, speedMax, step):
    gcode = ""
    gcode += "G4 S1\n"
    for s in range(speedMin, speedMax, step):
        gcode += "M117 speed {}: {}\n".format(xy, s)
        m = 0
        if s < 120:
            m = s
        else:
            m = 120
        gcode += "G0 F{} {}{}\n".format(s * 60, xy, center + m)
        gcode += "G0 F{} {}{}\n".format(s * 60, xy, center - m)
        gcode += "G0 F3000 {}{}\n".format(xy, center)
        gcode += "G4 P200\n"
    gcode += "M117 end\n"
    return gcode

gcode += "M204 S1000\nM205 X10 Y10\nG0 F4200 X{0} Y{0} Z1\n".format(center)
speedMin = 50
speedMax = 105
step     = 5
# gcode += speedTestXY360(speedMin, speedMax, step)
gcode += speedTestXY("X", speedMin, speedMax, step)
gcode += speedTestXY("Y", speedMin, speedMax, step)

with open('./Gcode_test.gcode', 'w') as f:
    f.write(gcode)
