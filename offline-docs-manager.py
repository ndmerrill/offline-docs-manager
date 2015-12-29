#!/bin/python
#
# Copyright 2015 Nathanael Merrill
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import sys
import os.path
import subprocess as sp
from urllib import parse

def get_sites ():
    if not os.path.isfile('docs.conf'):
        print("No docs.conf present")
        print("Run '" + sys.argv[0], "help' for help")
        sys.exit()
    f = open('docs.conf', 'r')
    sites = {}
    for row in f:
        if row.strip() == "":
            continue
        rowa = row.strip().split(" ")
        if len(rowa) != 2:
            print("docs.conf is incorrectly formatted")
            print("Run '" + sys.argv[0], "help' for help")
            sys.exit()
        sites[rowa[0]] = rowa[1]
    f.close()
    return sites

if len(sys.argv) < 2:
    print("Please enter a subcommand")
    print("Run", sys.argv[0], "help' for help")
    sys.exit()

subcommand = sys.argv[1]

if subcommand == "help":
    print("USAGE:")
    print("   ", sys.argv[0], "subcommand")
    print("")
    print("Subcommands:")
    print("    help - print this help")
    print("    update - update all websites in docs.conf")
    print("    getnew - download new websites in docs.conf")
    print("")
    print("docs.conf:")
    print("    This is where all the websites you want to download should be")
    print("    stored. It is a plain text file, in this format:")
    print("        [your name for docs] [website]")
    print("        [annother doc name] [website]")

elif subcommand == "update":
    sites = get_sites()

    links = {}
    for site in sites.items():
        out = sp.run(["wget",
            "--recursive",
            "--page-requisites",
            "--html-extension",
            "--convert-links",
            "--no-parent", site[1]])
        if out.returncode != 0:
            print("Failed to download URLs in docs.conf")
            print("Error Code:", out.returncode)
            sys.exit()
        urlparsed = parse.urlparse(site[1])
        links[site[0]] = "./" + urlparsed.netloc + urlparsed.path + "index.html"

    f = open('index.html', 'w')
    for link in links.items():
        f.write('<a href="' + link[1] + '">' + link[0] + '</a>')
    f.close()

elif subcommand == "getnew":
    sites = get_sites()

    links = {}
    for site in sites.items():
        urlparsed = parse.urlparse(site[1])
        if urlparsed.path.endswith("index.html"):
            st = ""
        else:
            st = "index.html"
        links[site[0]] = "./" + urlparsed.netloc + urlparsed.path + st
        if os.path.exists(urlparsed.netloc):
            continue
        out = sp.run(["wget",
            "--recursive",
            "--page-requisites",
            "--html-extension",
            "--convert-links",
            "--no-parent", site[1]])
        if out.returncode != 0 and out.returncode != 8:
            print("Failed to download URLs in docs.conf")
            print("Error Code:", out.returncode)
            sys.exit()

    f = open('index.html', 'w')
    for link in links.items():
        f.write('<a href="' + link[1] + '">' + link[0] + '</a><br />\n')
    f.close()

