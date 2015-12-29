# Offline Documentation Manager

Downloads online documentation from websites you specify and stores it for local
use on your computer.

### Setup

After downloading the script, create a file called docs.conf. This will contain
the websites you want to download. The file should contain a short name and
the root URL of the website you want to download. both the URL and name should
not contain any spaces. The format looks like this:

    name URL
    another URL

Example that downloads the python2 and python3 docs:

    python2 https://docs.python.org/2/
    python3 https://docs.python.org/3/

Then run:

    offline-docs-manager.py getnew

A file called index.html is created in the current dirrector. You should open
this in your browser. It is a list of links to all the documentation you
downloaded. You might want to bookmark it.

### License
    Copyright 2015 Nathanael Merrill

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
