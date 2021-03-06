#!/usr/bin/env python
#
# Copyright (C) 2014 Narf Industries <info@narfindustries.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

# debug for machine.py
# DEBUG = True
DEBUG = False

CONFIG = {
	'DEFAULT_DEBUG_LEVEL': 	0,

	'RT_NONE': 0,
	'RT_SELF': 1,
	'RT_MOTHER': 2,
	'RT_FATHER': 4,
	'RT_ADOPTING_PARENT': 8,
	'RT_ADOPTED_CHILD': 16,
	'RT_BIO_CHILD': 32,
	'RT_PARTNER': 64,
	'RT_FORMER': 128,

	'RELATED': 	   0x10000001,
	'NOT_RELATED': 0x14000041,
}

ERRORS = {

}