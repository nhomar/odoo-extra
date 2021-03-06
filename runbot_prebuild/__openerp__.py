#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2014 Vauxoo - http://www.vauxoo.com/
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#
#    Coded by: Vauxoo Consultores (info@vauxoo.com)
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
{
    'name': 'Runbot Pre Build',
    'category': 'Website',
    'summary': 'Runbot',
    'version': '1.1',
    'description': "Runbot with posibility to make pre-build",
    'author': 'Vauxoo',
    'depends': ['runbot', 'runbot_language', 'runbot_pylint'],
    'data': [
        'security/runbot_team_security.xml',
        'security/ir.model.access.csv',
        'wizard/wizard_kill_builds.xml',
        'runbot_prebuild_view.xml',
    ],
    'installable': True,
}
