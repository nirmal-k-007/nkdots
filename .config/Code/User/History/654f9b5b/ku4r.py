import sys

import subprocess

def getvol():
    result = subprocess.run("wpctl get-volume @DEFAULT_AUDIO_SINK@",shell=True,capture_output=True,text=True)
    percent = result.stdout
    if "MUTED" in percent:
        return 0
    percent = float(percent[8:len(percent)-1])
    percent*=100
    percent = int(percent)
    return percent

if(sys.argv[1] == "bup"):
    subprocess.run("brightnessctl set 1%+",shell=True,capture_output=True,text=True)
    result = subprocess.run("brightnessctl get",shell=True,capture_output=True,text=True)
    percent = str(result.stdout).strip()
    percent = int(percent)
    percent = int((percent/400)*100)
    if(percent<50):
        cmd = "dunstify -i  /home/nk/.config/hypr/Scripts/assets/brightzero.png -r 1234 -t 2000 \'Brightness : "+str(percent)+" %\'"
    elif(percent>=50 and percent<100):
        cmd = "dunstify -i  /home/nk/.config/hypr/Scripts/assets/brightmid.png -r 1234 -t 2000 \'Brightness : "+str(percent)+" %\'"
    else:
        cmd = "dunstify -i  /home/nk/.config/hypr/Scripts/assets/brightfull.png -r 1234 -t 2000 \'Brightness : "+str(percent)+" %\'"
    subprocess.run(cmd,shell=True,capture_output=True,text=True)
    
if(sys.argv[1] == "bdw"):
    subprocess.run("brightnessctl set 1%-",shell=True,capture_output=True,text=True)
    result = subprocess.run("brightnessctl get",shell=True,capture_output=True,text=True)
    percent = str(result.stdout).strip()
    percent = int(percent)
    percent = int((percent/400)*100)
    if(percent<50):
        cmd = "dunstify -i  /home/nk/.config/hypr/Scripts/assets/brightzero.png -r 1234 -t 2000 \'Brightness : "+str(percent)+" %\'"
    elif(percent>=50 and percent<100):
        cmd = "dunstify -i  /home/nk/.config/hypr/Scripts/assets/brightmid.png -r 1234 -t 2000 \'Brightness : "+str(percent)+" %\'"
    else:
        cmd = "dunstify -i  /home/nk/.config/hypr/Scripts/assets/brightfull.png -r 1234 -t 2000 \'Brightness : "+str(percent)+" %\'"
    subprocess.run(cmd,shell=True,capture_output=True,text=True)
    
if(sys.argv[1] == "vup"):
    if(getvol()<150):
        subprocess.run("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+",shell=True,capture_output=True,text=True)
        percent = getvol()
        if(percent<=100):
            if(percent==0):
                cmd = "dunstify -i /home/nk/.config/hypr/Scripts/assets/vol1.png -r 1234 -t 2000 \'Volume : "+str(percent)+" %\'"
            subprocess.run(cmd,shell=True,capture_output=True,text=True)
        elif(percent>100 and percent<=150):
            cmd = "dunstify -i /home/nk/.config/hypr/Scripts/assets/volume.png -u critical -r 1234 -t 2000 \'Volume : "+str(percent)+" %\'"
            subprocess.run(cmd,shell=True,capture_output=True,text=True)

if(sys.argv[1] == "vdw"):
    subprocess.run("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-",shell=True,capture_output=True,text=True)
    result = subprocess.run("wpctl get-volume @DEFAULT_AUDIO_SINK@",shell=True,capture_output=True,text=True)
    percent = result.stdout
    percent = float(percent[8:len(percent)-1])
    percent*=100
    percent = int(percent)
    if(not getvol()>100):
        cmd = "dunstify -i /home/nk/.config/hypr/Scripts/assets/volume.png -r 1234 -t 2000 \'Volume : "+str(percent)+" %\'"
        subprocess.run(cmd,shell=True,capture_output=True,text=True)
    else:
        cmd = "dunstify -i /home/nk/.config/hypr/Scripts/assets/volume.png -u critical -r 1234 -t 2000 \'Volume : "+str(percent)+" %\'"
        subprocess.run(cmd,shell=True,capture_output=True,text=True)
if(sys.argv[1] == "bt"):
    result = subprocess.run("acpi -b",shell=True,capture_output=True,text=True)
    ind = (result.stdout).index("%")
    battery = ""
    for i in range(ind-3,ind+1,1):
        battery+=result.stdout[i]
    subprocess.run("dunstify -r 1234 -t 2000 \'Battery : " + battery + "\'",shell=True,capture_output=True,text=True)

if(sys.argv[1] == "rofi"):
    result = subprocess.run("echo  \"SHUT-DOWN\nSLEEP\nRESTART\nLOCK\nLOG-OUT\" | rofi -dmenu",shell=True,capture_output=True,text=True)
    print(result.stdout)
    if(result.stdout=="SHUT-DOWN\n"):
        subprocess.run("poweroff",shell=True)
    if(result.stdout=="LOCK\n"):
        subprocess.run("hyprlock",shell=True)
    if(result.stdout=="LOG-OUT\n"):
        subprocess.run("hyprctl dispatch exit",shell=True)
    if(result.stdout=="SLEEP\n"):
        subprocess.run("hyprlock",shell=True)
        subprocess.run("systemclt suspend",shell=True)
    if(result.stdout=="RESTART\n"):
        subprocess.run("reboot",shell=True)
    
