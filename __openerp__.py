# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Mariano Ruiz (Enterprise Objects Consulting)
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
##############################################################################

{
    "name" : "Make account invoice analytics distribution account required in sale invoice line",
    "version" : "1.0",
    "depends" : ["account", "base", "account_analytic_plans"],
    "author" : "Enterprise Objects Consulting",
    "description":
"""
Module to make analytics distribution account field required in sale invoice line.
Also you can set a default value for the field.
""",
    "website" : "http://www.eoconsulting.com.ar",
    "category" : "Generic Modules/Accounting",
    "active": False,
    "installable": True,

}
