# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2014, 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Bundles for Jasmine test runner."""

from __future__ import unicode_literals

from invenio.base.bundles import invenio as _i, jquery as _j
from invenio.ext.assets import Bundle, RequireJSFilter

jasmine_js = Bundle(
    # es5-shim is needed by PhantomJS
    # 'vendors/es5-shim/es5-shim.js',
    # 'vendors/es5-shim/es5-sham.js',
    "js/jasmine/init.js",
    output="jasmine.js",
    weight=50,
    filters=RequireJSFilter(exclude=[_j, _i]),
    bower={
        "jasmine": ">=2",
        "jasmine-jquery": ">=2",
        "jasmine-flight": ">=3",
        "jasmine-ajax": ">=2",
    }
)

jasmine_styles = Bundle(
    'vendors/jasmine/lib/jasmine-core/jasmine.css',
    weight=-1,
    output='jasmine.css'
)
