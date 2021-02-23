#<one line to give the program's name and a brief idea of what it does.>
#    Copyright (C) <2021>  Mauro Clemente <meezyclemente@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import socket


def get_open_ports(target, port_range):
   open_ports = []

   for port in range (port_range[0], port_range[1]):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(5)
      outcome = s.connect_ex((target, port))

      if  outcome == 0:
        open_ports.append(port)
      s.close()

   return (open_ports)


def main():
    target = input("Enter the target IP or URL: ")
    print("Enter a port range: ")
    port_initial = int(input("\tFrom: "))
    port_final = int(input("\tTo: "))
    port_list = [port_initial, port_final]

    print("Open Ports: ", get_open_ports(target, port_list))


main()

