import requests, json, sys, re, time, warnings, argparse, os, subprocess, platform

from datetime import datetime

warnings.filterwarnings("ignore")

# Code to validate all correct parameters are passed in

parser=argparse.ArgumentParser(description="Python script using Redfish API to update device firmware using DMTF standard action SimpleUpdate from a local directory")
parser.add_argument('-ip', action='store', type=str, nargs='+', help='iDRAC IP', required=True)
parser.add_argument('-u', help='iDRAC username', required=True)
parser.add_argument('-p', help='iDRAC password', required=True)
parser.add_argument('script_examples',action="store_true",help='DeviceFirmwareSimpleUpdateREDFISH.py -ip 192.168.0.120 -u root -p calvin -g y, this example will return current firmware versions for all devices supported for updates. DeviceFirmwareSimpleUpdateREDFISH.py -ip 192.168.0.120 -u root -p calvin -l C:\Python27 -f BIOS_422T0_WN64_1.4.9.EXE, this example will update BIOS firmware which BIOS DUP is located in C:\Python27 directory')
parser.add_argument('-g', help='Get current supported devices for firmware updates and their current firmware versions, pass in \"y\"', required=False)
parser.add_argument('-l', help='Pass in the local directory location of the firmware image', required=False)
parser.add_argument('-f', help='Pass in the firmware image name', required=False)
parser.add_argument('-r', help='Reboot the server to apply the update if needed. Pass in \"n\" to reboot the server now to run the update or pass in \"l\" to not reboot the server (job ID will still be in scheduled state and will execute on next manual server reboot. Note: If the update gets applied with no server reboot (Example: iDRAC, DIAGs, Driver pack), you don\'t need to pass in this argument. For more details on which devices update immediately, refer to Lifecycle Controller User Guide Update section.', required=False)


args=vars(parser.parse_args())
print(args)

idracip=args["ip"]
new_list_ips = []
new_list_ips = idracip[0].split(',')
idrac_username=args["u"]
idrac_password=args["p"]
print(new_list_ips)


# def get_FW_inventory():
#   for idrac_ip in new_list_ips:
#     print("\n- INFO, current devices detected with firmware version and updateable status -\n")
#     req = requests.get('https://%s/redfish/v1/UpdateService/FirmwareInventory/' % (idrac_ip), auth=(idrac_username, idrac_password), verify=False)
#     statusCode = req.status_code
#     installed_devices=[]
#     data = req.json()
#     for i in data['Members']:
#         for ii in i.items():
#             if "Installed" in ii[1]:
#                 installed_devices.append(ii[1])
#     for i in installed_devices:
#         req = requests.get('https://%s%s' % (idrac_ip, i), auth=(idrac_username, idrac_password), verify=False)
#         statusCode = req.status_code
#         data = req.json()
#         try:
#             updateable_status = data['Updateable']
#             version = data['Version']
#             device_name = data['Name']
#             print("Device Name: %s, Firmware Version: %s, Updatable: %s" % (device_name, version, updateable_status))
#         except:
#             print("- INFO, unable to get property info for URI: \"%s\"" % i)
#     sys.exit(1)
# if __name__ == "__main__":
#     get_FW_inventory()





