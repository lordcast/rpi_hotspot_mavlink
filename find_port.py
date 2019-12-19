import os,glob, fnmatch

preferred_ports = [
    '*FTDI*',
    "*Arduino_Mega_2560*",
    "*3D*",
    "*USB_to_UART*",
    '*Ardu*',
    '*PX4*',
    '*Hex_*',
    '*Holybro_*',
    '*mRo*',
    '*FMU*']

class SerialPort(object):
    '''auto-detected serial port'''
    def __init__(self, device, description=None, hwid=None):
        self.device = device
        self.description = description
        self.hwid = hwid

    def __str__(self):
        ret = self.device
        if self.description is not None:
            ret += " : " + self.description
        if self.hwid is not None:
            ret += " : " + self.hwid
        return ret

def auto_detect_serial_win32(preferred_list=['*']):
    '''try to auto-detect serial ports on win32'''
    try:
        from serial.tools.list_ports_windows import comports
        list = sorted(comports())
    except:
        return []
    ret = []
    others = []
    for port, description, hwid in list:
        matches = False
        p = SerialPort(port, description=description, hwid=hwid)
        for preferred in preferred_list:
            if fnmatch.fnmatch(description, preferred) or fnmatch.fnmatch(hwid, preferred):
                matches = True
        if matches:
            ret.append(p)
        else:
            others.append(p)
    if len(ret) > 0:
        return ret
    # now the rest
    ret.extend(others)
    return ret



def auto_detect_serial_unix(preferred_list=['*']):
    '''try to auto-detect serial ports on unix'''
    import glob
    glist = glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*') + glob.glob('/dev/serial/by-id/*')
    ret = []
    others = []
    # try preferred ones first
    for d in glist:
        matches = False
        for preferred in preferred_list:
            if fnmatch.fnmatch(d, preferred):
                matches = True
        if matches:
            ret.append(SerialPort(d))
        else:
            others.append(SerialPort(d))
    if len(ret) > 0:
        return ret
    ret.extend(others)
    return ret

def auto_detect_serial(preferred_list=['*']):
    '''try to auto-detect serial port'''
    # see if 
    if os.name == 'nt':
        return auto_detect_serial_win32(preferred_list=preferred_list)
    return auto_detect_serial_unix(preferred_list=preferred_list)


def complete_serial_ports():
    '''return list of serial ports'''
    ports = auto_detect_serial(preferred_list=preferred_ports)
    for p in ports:
        print(p.device)		


complete_serial_ports()
