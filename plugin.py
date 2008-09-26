#! /usr/bin/evn python
# -*- coding: utf-8 -*-

"""
Apple Address Book Plugin for sipgate click to dial function

author: Marcel Lauhoff <ml@irq0.org>

"""

from AddressBook import *
from AppKit import *

from ConfigParser import ConfigParser
import os.path

from sipgate import *

class SipgateClickToDial(NSObject):
    def actionProperty(self):
        return kABPhoneProperty

    def titleForPerson_identifier_(self, person, identifier):
        return u"Dial (Sipgate Click2Dial)"
    
    def shouldEnableActionForPerson_identifier_(self, person, identifier):
        return len(person.phone()) > 0

    def performActionForPerson_identifier_(self, person, identifier):
        phones = person.valueForProperty_(kABPhoneProperty)
        use_phone = phones.valueForIdentifier_(identifier)

        conf = ConfigParser()
        conf.read(os.path.expanduser('~/.clicktodial.conf'))

        s = SimpleSipgateApi(conf.get('account','user'),
                             conf.get('account','password'))
        s.call(conf.get('account','phone'), makeSipUri(use_phone)) 
