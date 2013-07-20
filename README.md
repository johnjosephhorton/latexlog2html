latexlog2html 
=============

This is script for turning a LaTeX log file into a more-pleasant-to-read [HTML file](http://dl.dropboxusercontent.com/u/420874/permanent/sample.html).
It lists all the errors and warnings from the log file as ordered lists at the top of the HTML file, with internal hyperlinks to the actual in situ warnings/errors.                                   

Install
-------
    
	git clone git@github.com:johnjosephhorton/latexlog2html.git
	cd latexlog2html 
	sudo python setup.py install 

Usage
-----
To create the HTML file, simply run: 

	latexlog2html LOGFILE
	
Where `LOGFILE` is the name of the LaTeX log file. 
The HTML file will open automatically in a browser tab. 

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
