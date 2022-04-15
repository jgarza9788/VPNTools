import os
import shutil

downloads = r'C:\Users\JGarza\Downloads'
output_folder = r'D:\Scripts\findVPNServer\output' 
connection_file = ''
server_id = ''

for dirName, subdirList, fileList in os.walk(downloads):
    if (dirName == downloads):
        # print(fileList)
        for f in fileList:
            # print(os.path.join(dirName,f))
            if '.nordvpn.com.udp.ovpn' in f:
                connection_file = os.path.join(dirName,f)
                server_id = f.split('.')[0]


print(connection_file)
print(server_id)

content = ''
with open(connection_file,'r') as f:
    content = f.readlines()
for i in range(len(content)):    
    content[i] = content[i].replace('auth-user-pass\n', 'auth-user-pass login.conf\n')
with open(connection_file,'w') as f:
    f.writelines(content)

shutil.move(connection_file, output_folder)

# x = 'us' + str(server_num)
down_file0 = r'D:\Scripts\findVPNServer\templates\{0}.nordvpn.com.udp_down.bat'.format('x')
down_file1 = os.path.join(output_folder,'{0}.nordvpn.com.udp_down.bat'.format(server_id))
shutil.copy(down_file0, down_file1)

up_file0 = r'D:\Scripts\findVPNServer\templates\{0}.nordvpn.com.udp_up.bat'.format('x')
up_file1 = os.path.join(output_folder,'{0}.nordvpn.com.udp_up.bat'.format(server_id))
shutil.copy(up_file0, up_file1)

