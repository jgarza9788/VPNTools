import os,sys,re,time
from datetime import datetime
import subprocess, platform
import nerdfonts as nf
from termcolor import colored
from utilities import bar as b

DIR = os.path.dirname(os.path.realpath(__file__))

# these are the server ids 
sids = [
    "us8479"
    ,"us8494"
    ,"us8495"
    ,"us8482"
    ,"us8478"
    ,"us9619"
    ,"us8474"
    ,"us9615"
    ,"us9618"
    ,"us9612"
    ,"us9613"
    ,"us9615"
]

vpn_programs = [
    "openvpn-gui.exe",
    "openvpn.exe",
    "qbittorrent.exe",
    ]

def run_cmd(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    # result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    # output, error = result.communicate()

    # if error == None:
    #     return output
    # else:
    #     print("error:")
    #     print(error)
    #     return None

def VPN_running():
    rc = run_cmd("tasklist")
    # print(rc.stdout.read())
    # print(rc.wait())

    rc = str(rc.stdout.read())
    
    status = False

    for p in vpn_programs:
        if p in rc:
            status = True
    
    return status


def kill_program(name,verbose=False):

    text = ""
    try:
        cmd = f"taskkill /IM {name} /f"
        p = run_cmd(cmd)
        text = str(p.stdout.read())
        status = p.wait()
    except:
        pass

    if verbose:
        print(name)
        print(text)

    if verbose:
        if status == 0:
            
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

    # cmd = "echo " + date +","+time+"," + sid + ".nordvpn.com.udp.ovpn," + str(ping) + ">> results.log"
    # print(cmd)
    # run_cmd(cmd)

    with open(os.path.join(DIR,'results.log'), 'a',encoding='UTF-8') as f:
        f.write(date + ',' + time + ',' + sid + '.nordvpn.com.udp.ovpn,' + str(ping) + '\n')
    
def connect_to_VPN(sid):
    cmd = "\"C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe\" --connect {0}.nordvpn.com.udp.ovpn"
    cmd = cmd.format(sid)
    run_cmd(cmd)

    text = nf.icons['fa_check'] + " " + sid + ".nordvpn.com" 
    text = colored(text,color='green')
    print(text)

def wait_seconds(s):
    icon = colored(nf.icons['mdi_timer_sand'],color='green')

    for i in range(s,0,-1):
        print('\r', f"{icon} {str(i)}/{str(s)} seconds          ",end='',flush=True)
        time.sleep(1)

def activate_vpn():

    if VPN_running() ==  True:
        print("\nkilling old VPN, and will rerun")
        for index,p in enumerate(vpn_programs):
            kill_program(p)
            print(b.slant_bar((index+ 1)/len(vpn_programs),color='red',on_color='grey'),end='\r')
        wait_seconds(10)

    print("\nPinging servers:")
    sid = "us8479"
    low_ping = 1000
    for index,s in enumerate(sids):
        prefix = "  " + str(index+1) + "/" + str(len(sids))
        print(b.data_bar(text=prefix,value=(index+ 1)/len(sids),color='green',on_color='grey'),end='\r')
        r = ping_server(s)
        
        if r == None or r == False:
            continue
        elif r < low_ping:
            low_ping = r
            sid = s

    print("\n\nConnecting to server:")
    print(sid,low_ping)
    
    write_to_log(sid,low_ping)
    connect_to_VPN(sid)

def kill_vpn():

    for index,p in enumerate(vpn_programs):
        kill_program(p)
        print(b.slant_bar((index+ 1)/len(vpn_programs),color='red',on_color='grey'),end='\r')
    print()

    text = nf.icons['fa_check'] + " VPN was killed" 
    text = colored(text,color='green')
    print(text)

def ping_all():

    pings = []
    for s in sids:
        r = ping_server(s)
        print(s,r)
        pings.append(r)
        # write_to_log(s,r)
    
    print()
    print('Avg ping: ', '{:.2f}'.format(sum(pings)/len(pings)))
    print('Max ping: ', max(pings))
    print('Min ping: ', min(pings))

def main():
    print(*sys.argv,sep='\n')

    try:
        if sys.argv[1].upper() in ["ACTIVATE","CONNECT","1"]:
            activate_vpn()
        elif sys.argv[1].upper() in ["DISCONNECT","DEACTIVATE","KILL","0"]:
            kill_vpn()
        elif sys.argv[1].upper() in ["PING","PING_ALL","2"]:
            ping_all()
    except Exception as e:
        e = colored(nf.icons["mdi_close_box"] + str(e),color='red')
        print(e)

    input()


if __name__ == "__main__":
    main()
#    print(VPN_running())
