latexlog2html 
=============

This is script for turning a LaTeX log file into something a little more pleasant to read. 

How it works
------------

	python latexlog2html.py --file FILE --browser BROWSER 
	
Where `FILE` is the name of the log file and and `BROWSER` is the name of the browser you want to use to display the file e.g., `google-chrome` or `firefox.`

Install
-------
Probably the simplest thing to do is just place latexlog2html.py in your `/usr/local/bin` and make it executable (`chmod + x latexlog2html`). 


Caveats & Limitations
---------------------

Right now, it uses `os.system(BROWSER + 'sample.html')` to open the HTML file. 
This is a bad idea - consider `python latexlog2html.py --file sample.log --browser sudo rm -rf /;`. 
The working assumption is that the person using this knows that they are doing and wouldn't do something so foolish. 
But I'd be more than happy to merge a pull request that did something more sensible here. 

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
