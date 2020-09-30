import psutil

class GetSys:
    def GetCpu(self):
        usage = str(psutil.cpu_percent(interval=1))+"%"
        return usage
    
    def GetBattery(self):
        battery = psutil.sensors_battery().percent
        check_plugged = " Plugged in" if(psutil.sensors_battery().power_plugged) else " Not Plugged in"
        return "Your battery is at " + str(battery)+"%"+" and "+ "it is currently" + check_plugged