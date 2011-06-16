#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
A plugin to call contacts via Sipgate directly from the Mac OS X Address Book
    website: <https://github.com/pklaus/mac_click2dial_sipgate#readme>

Authors:

* Marcel Lauhoff <ml →AT→ irq0.org>
* Philipp Klaus <philipp.klaus →AT→ gmail.com>

"""

from AddressBook import *
from AppKit import *

from ConfigParser import ConfigParser
import os.path

from sipgate import *

from datetime import datetime
LOG_FILE=os.path.expanduser('~/.clicktodial.log')

class SipgateClickToDial(NSObject):
    def actionProperty(self):
        return kABPhoneProperty

    def titleForPerson_identifier_(self, person, identifier):
        return u"Call via Sipgate"
    
    def shouldEnableActionForPerson_identifier_(self, person, identifier):
        return len(person.phone()) > 0

    def performActionForPerson_identifier_(self, person, identifier):
        log=open(LOG_FILE,'a')
        log.write(datetime.utcnow().isoformat()+'\n')
        phones = person.valueForProperty_(kABPhoneProperty)
        use_phone = phones.valueAtIndex_(phones.indexForIdentifier_(identifier))

        conf = ConfigParser()
        conf.read(os.path.expanduser('~/.clicktodial.conf'))
        log.write('Calling %s\n' % use_phone)
        s = SimpleSipgateApi(conf.get('account','user'),conf.get('account','password'))
        log.write('SimpleSipgateApi constructed.\n')
        s.call(conf.get('account','phone'), makeSipUri(use_phone))
        log.write('SimpleSipgateApi.call was called.\n')
        log.close()
