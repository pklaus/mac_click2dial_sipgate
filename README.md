# A plugin to call contacts via Sipgate directly from the Mac OS X Address Book

With this Address Book Plugin installed, you can call any contact
via Sipgate VoIP calls directly from the Address Book application.

## Installation of the pre-packaged Plugin

#### Requirements

* Mac OS X 10.6 (I use 10.6.7 and it works. Please let me know if you have trouble
  with any other release of 10.6).

#### Installation

Get **SipgateClickToDial.bundle.zip** from the [downloads section](https://github.com/pklaus/mac_click2dial_sipgate/downloads),
unpack it and move the bundle to the folder `~/Library/Address Book Plug-Ins/`.

Then create a configuration file `~/.clicktodial.conf` from the
[sample configuration file][].

#### Usage

Now you can call numbers of contacts in your OS X Mac Address Book
by clicking on the phone number and selecting **Call via Sipgate**.

## Custom Build

#### Build Requirements

* You need py2app:  
  `pip install py2app` or `easy_install py2app`

#### Build and Installation

Run

    make
    make install

which is basically

    wget https://raw.github.com/pklaus/python-sipgate-xmlrpc/v0.9.2/sipgate.py
    python2.6 setup.py py2app
    mv "dist/SipgateClickTodial.bundle" "~/Library/Address Book Plug-Ins/"

## Authors

* Marcel Lauhoff (ml →AT→ serious-net.org)  
  He first published the project on <http://irq0.org/Code> and is the original
  author. He allowed me to use the code and publish it under any license. Thx!
* Philipp Klaus (philipp.klaus →AT→ gmail.com)  
  I copied file by file from <https://gitweb.irq0.org/?p=mac_click2dial.git;a=summary>
  (The git repo https://git.irq0.org/mac_click2dial.git was unreachable).  
  Then I put it to GitHub and made it compatible with OS X Snow Leopard.

#### Bug Reports

If something went wrong with this Address Book plugin, please open an issue
on [the bug tracker][] and provide details from the log file `~/.clicktodial.log`.


[sample configuration file]: https://github.com/pklaus/mac_click2dial_sipgate/blob/master/clicktodial.conf
[the bug tracker]: https://github.com/pklaus/mac_click2dial_sipgate/issues
