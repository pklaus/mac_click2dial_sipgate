"""
Script for building ClickToDial plugin

Usage:
    python setup.py py2app

To use this copy dist/ClickToDial.plugin to the plugin directory:
   $ mv dist/ClickToDial.plugin \
           ~/Library/Address\ Book\ Plug-Ins/ClickToDial.plugin
"""
from distutils.core import setup
import py2app

infoPlist = dict(
    CFBundleName='ClickToDial',
    CFBundleGetInfoString='Sipget Click2Dial function for Address Book',
    CFBundleVersion='0.1',
    CFBundleShortVersionString = '0.1',
    NSPrincipalClass='SipgateClickToDial',
)

setup(
    name='ClickToDial',
    plugin=['plugin.py'],
    data_files=['sipgate.py'],
    options=dict(py2app=dict(
        extension=".bundle",
        plist=infoPlist,
    )),
)
