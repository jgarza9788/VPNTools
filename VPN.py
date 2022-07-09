import os,sys,re,time
from datetime import datetime
import subprocess, platform
import nerdfonts as nf
from termcolor import colored
from utilities import bar as b

sids = [
    "us8479"
    ,"us8494"
    ,"us8495"
    ,"us9618"
    ,"us9612"
    ,"us8482"
    ,"us9616"
    ,"us8478"
    ,"us9619"
    ,"us8474"
]

def run_cmd(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)


def kill_program(name,verbose=False):

    text = ""
    try:
        cmd = f"taskkill /IM {name} /f"
        p = run_cmd(cmd)
        text = str(p.stdout.read())
        retcode = p.wait()
    except:
        pass

    if verbose:
        print(name)
        print(text)

    if retcode == 0:
        icon = nf.icons["mdi_checkbox_marked"]
        print(colored(f" {icon} {name} was killed",color="green"))
    else:
        icon = nf.icons["mdi_close_box"]
        print(colored(f" {icon} {name} was not killed",color="red"))


def ping_server(sid):

    server = sid + '.nordvpn.com'

    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', server), shell=True)
        output = str(output)
        # print(output)

        result = re.findall(r'Average = \d+ms', output)[0]
        # print(result)
        result = int(re.findall(r'\d+', result)[0])
        # print(result)
        return result

    except Exception as e:
        return False

def write_to_log(sid,ping):
    dt = datetime.now()
    date = dt.strftime("%m/%d/%Y")
    time = dt.strftime("%H:%M:%S.%f")[:11]
    cmd = "echo " + date +","+time+"," + sid + ".nordvpn.com.udp.ovpn," + str(ping) + ">> results.log"
    print(cmd)
    run_cmd(cmd)

def connect_to_VPN(sid):
    cmd = "\"C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe\" --connect {0}.nordvpn.com.udp.ovpn"
    cmd = cmd.format(sid)
    run_cmd(cmd)

    text = nf.icons['fa_check'] + " " + sid + ".nordvpn.com" 
    text = colored(text,color='green')
    print(text)


def activate_vpn():
    programs_to_kill = [
        "openvpn-gui.exe",
        "openvpn.exe",
        "qbittorrent.exe",
    ]

    print("\nkilling programs")
    for index,p in enumerate(programs_to_kill):
        kill_program(p)
        print(b.slant_bar((index+ 1)/len(programs_to_kill),color='red',on_color='grey'),end='\r')


    icon = colored(nf.icons['mdi_timer_sand'],color='green')
    print("\n\n" + icon + "waiting 3 seconds ")
    time.sleep(3)
    

    print("\nPinging servers:")
    sid = "us8479"
    low_ping = 1000
    for index,s in enumerate(sids):
        print(s + " -- " + b.data_bar((index+ 1)/len(sids),color='green',on_color='grey'),end='\r')
        r = ping_server(s)
        
        if r == None:
            continue
        elif r < low_ping:
            low_ping = r
            sid = s

    print("\n\nConnecting to server:")
    print(sid,low_ping)
    
    write_to_log(sid,low_ping)
    connect_to_VPN(sid)

def kill_vpn():
    programs_to_kill = [
        "openvpn-gui.exe",
        "openvpn.exe",
        "openvpnserv.exe",
        "qbittorrent.exe",
    ]

    for index,p in enumerate(programs_to_kill):
        kill_program(p)
        print(b.slant_bar((index+ 1)/len(programs_to_kill),color='red',on_color='grey'),end='\r')
    print()

    text = nf.icons['fa_check'] + " VPN is off" 
    text = colored(text,color='green')
    print(text)


def main():
    print(*sys.argv,sep='\n')

    try:
        if sys.argv[1].upper() in ["ACTIVATE","CONNECT","1"]:
            activate_vpn()
        elif sys.argv[1].upper() in ["DISCONNECT","DEACTIVATE","KILL","0"]:
            kill_vpn()
    except Exception as e:
        e = colored(nf.icons["mdi_close_box"] + str(e),color='red')
        print(e)

    input()


if __name__ == "__main__":
    # kill_program("openvpn-gui.exe")
    # kill_program("Calculator.exe")

    # print(ping_server("us8482"))

    # for i in nf.icons.keys():
    #     if "checkbox" in i :
    #         print( nf.icons[i],i)

    main()
