"""
Script for building ClickToDial plugin
"""
from distutils.core import setup
import py2app

infoPlist = dict(
    CFBundleName='SipgateClickToDial',
    CFBundleGetInfoString='Sipget Click2Dial function for Address Book',
    CFBundleVersion='0.9',
    CFBundleShortVersionString = '0.9',
    NSPrincipalClass='SipgateClickToDial',
)

setup(
    name='SipgateClickToDial',
    plugin=['plugin.py'],
    data_files=['sipgate.py'],
    options=dict(py2app=dict(
        extension=".bundle",
        plist=infoPlist,
    )),
)
