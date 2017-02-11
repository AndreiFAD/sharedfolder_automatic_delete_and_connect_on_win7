#!/usr/bin/python
# -*- coding: cp1250  -*-
__author__ = 'Fekete András Demeter'

import subprocess,time,os,requests

def connected_to_internet(url='https://host.intra/', timeout=10):
    # check internet or intranet connection
    try:
        _ = requests.get(url, timeout=timeout, verify=True)
        return True
    except requests.ConnectionError:
        return False


def delete_shared_folder_connection(Drive_letter):
    try:
        # delete shared folders, what now use on pc:
        for adat in Drive_letter:
            if len(adat) == 1:
                subprocess.Popen(r'net use ' + adat + ': /del', shell=False, stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE)
                time.sleep(1)
    except:
        time.sleep(1)

def connect_shared_foder(Drive_letter, Shared_drive_path):

    f = 0
    while f < len(Drive_letter):
        # connect shared folders on pc:
        if os.path.isdir(Drive_letter[f] + ":\\") == False:
            print('net use ' + Drive_letter[f] + ': ' + Shared_drive_path[f])
            subprocess.Popen(r'net use ' + Drive_letter[f] + ': ' + Shared_drive_path[f], shell=False,
                             stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        f += 1
        time.sleep(1)

if __name__ == "__main__":

    Drive_letter=['X','Y']
    Shared_drive_path=['\\\\host\\sharefolderpath\\', '\\\\host\\sharefolderpath2\\']

    check=connected_to_internet()

    if check==True:

        try:

            delete_shared_folder_connection(Drive_letter)

            time.sleep(2)

            connect_shared_foder(Drive_letter, Shared_drive_path)

        except Exception as e:
                    print(e)
                    time.sleep(5)

        print("I'm ready to work")
        time.sleep(60)

    else:
        print("You havn't internet or intranet connetion, pls check it!")
        time.sleep(60)
