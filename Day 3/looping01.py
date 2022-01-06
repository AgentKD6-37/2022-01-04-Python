#!/usr/bin/env python3



def main():
    with open("dnsservers.txt", "r") as dnsfile:

        for svr in dnsfile:

            svr = svr.rstrip('\n')  # remove newline char if exists
            # would exists on all but last line
            # IF the string svr ends with 'org'
            if svr.endswith('org'):
                with open("org-domain.txt", "a") as srvfile:  # 'a' is append mode
                    srvfile.write(svr + "\n")
            # ELSE-IF the string svr ends with 'com'
            elif svr.endswith('com'):
                with open("com-domain.txt", "a") as srvfile:  # 'a' is append mode
                    srvfile.write(svr + "\n")

main()
