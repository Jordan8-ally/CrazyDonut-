import numpy as np
import math
import time

theta_spacing = 0.07
phi_spacing = 0.02
R1 = 1
R2 = 2
K2 = 5
screen_width = 50
screen_height = 30
K1 = screen_width*K2*3/(8*(R1+R2))

A = 0.0
B = 0.0
cosA = 0.0
cosB = 0.0
sinA = 0.0
sinB = 0.0
def render_frame(A, B):
    cosA = math.cos(A)
    cosB = math.cos(B)
    sinA = math.sin(A)
    sinB = math.sin(B)
    
    output = [[' ' for _ in range(screen_width)] for _ in range(screen_height)]
    zbuffer = [[0.0 for _ in range(screen_width)] for _ in range(screen_height)]

    for theta in np.arange(0, 2*np.pi, theta_spacing):
        costheta = math.cos(theta)
        sintheta = math.sin(theta)
    
        for phi in np.arange(0, 2*np.pi, phi_spacing):
            cosphi = math.cos(phi)
            sinphi = math.sin(phi)

            circlex = R2+R1*costheta
            circley = R1*sintheta

            x = circlex*(cosB*cosphi + sinA*sinB*sinphi) - circley*cosA*sinB
            y = circlex*(sinB*cosphi - sinA*cosB*sinphi) + circley*cosA*cosB
            z = K2 + circlex*cosA*sinphi + circley*sinA
            ooz = 1/z
            xp = int(screen_height/2 + K1*ooz*x)
            yp = int(screen_height/2 - K1*ooz*y)
    
            if(0<=xp<screen_width and 0<=yp<screen_height):
                L = cosphi*costheta*sinB - cosA*costheta*sinphi - sinA*sintheta + cosB*(cosA*sintheta - sinA*costheta*sinphi)
                if(L>0):
                    if(ooz>zbuffer[yp][xp]):
                        zbuffer[yp][xp] = ooz
                        luminance_index = int(L*8)
                        output[yp][xp] = ".,-~:;=!*#$@"[luminance_index]
           
    frame = "\n".join([" ".join(row) for row in output])
    return frame

with open("spinningDonut.txt", "w") as f:
    for i in range(1000):
        frame = render_frame(A, B)
        f.write(frame)
        f.write("\n" + "-"*screen_width + "\n")
        A += 0.04
        B += 0.02
        time.sleep(0.03)
    

