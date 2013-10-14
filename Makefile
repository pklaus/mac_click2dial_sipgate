# Tag for the version of https://github.com/pklaus/python-sipgate-xmlrpc
SIPGATE_LIB_VERSION_TAG = v0.9.2


all: dist/SipgateClickTodial.bundle

dist/SipgateClickTodial.bundle: sipgate.py
	python2.6 setup.py py2app

sipgate.py:
	@-rm sipgate.py
	curl -O https://raw.github.com/pklaus/python-sipgate-xmlrpc/$(SIPGATE_LIB_VERSION_TAG)/sipgate.py

install: dist/SipgateClickTodial.bundle
	@-rm -rf ~/Library/Address\ Book\ Plug-Ins/SipgateClickTodial.bundle
	@mv dist/SipgateClickTodial.bundle ~/Library/Address\ Book\ Plug-Ins/
	@echo 'Moved "dist/SipgateClickTodial.bundle" to "~/Library/Address Book Plug-Ins/".'
	@echo "Please copy the sample configuration file to ~/.clicktodial.conf and adjust to your settings."

# clean the directory from unneeded files
.PHONY : clean
clean :
	@-rm -rf *~ sipgate.py build dist *.pyc
