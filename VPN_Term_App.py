
import os,time

#import custom modules
import VPN  

def void_function():
    pass

menu = [
        {
            "display_name": "kill VPN",
            "action": VPN.kill_vpn
        },
        {
            "display_name": "activate VPN",
            "action": VPN.activate_vpn
        },
        {
            "display_name": "Check VPN Status",
            "action": VPN.VPN_running
        },
        {
            "display_name": "quit",
            "action": void_function
        }
    ]


def main():

    while True:
        os.system('cls' if os.name=='nt' else 'clear')

        print("VPN Term APP")
        time.sleep(0.1)
        if VPN.VPN_running():
            print("VPN is running\n")
        else:
            print("VPN is NOT running\n")

        print("choose one:")

        for index,m in enumerate(menu):
            print("\t",index, m["display_name"])
        print("\t\t","--> type QUIT to quit")
        
        user_input = input()

        try: 
            menu[int(user_input)]["action"]()

            if menu[int(user_input)]["display_name"] == "quit":
                break
        except:
            if user_input.upper() in ["QUIT","EXIT","DONE"]:
                break




if __name__ == "__main__":
    main()