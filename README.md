latexlog2html 
=============

This is script for turning a LaTeX log file into a more-pleasant-to-read [HTML file](http://dl.dropboxusercontent.com/u/420874/permanent/sample.html).
It lists all the errors and warnings from the log file as ordered lists at the top of the HTML file, with internal hyperlinks to the actual in situ warnings/errors.                                   

How it works
------------
To create this HTML file, simply run: 

	python latexlog2html.py LOGFILE
	
Where `LOGFILE` is the name of the LaTeX log file. 

Install
-------
Probably the simplest thing to do is just place latexlog2html.py in your `/usr/local/bin` and make it executable (`chmod + x latexlog2html`). 

License 
-------

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
