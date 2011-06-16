# Developer Notes

This file contains some information for those who want to
work on this project: Hints, how to debug the app and where
to find further information.

### The important files of this project

* **plugin.py**
  The Address Book plugin.
* **sipgate.py**
  The file to communicate with the Sipgate API.
* Less important files:
  * **clicktodial.conf**  
    Example configuration file
  * **setup.py**  
    Configures this project to be built to a .bundle using py2app on Mac
  * **Makefile**  
    Makes it easy to create the app and install it for the current user.

### Debugging

If you want to debug the application, you may write to the log
file `~/.clicktodial.log` and have a look at the messages of the
OS X application Console. It holds tracebacks of exceptions.

### Inspiration

* A resource for python code in case of troubles can be
  <http://www.ibp.de/~lars/addressbook/>.

