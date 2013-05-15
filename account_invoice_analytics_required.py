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

from osv import fields, osv

def _get_property_value(obj, cr, uid, context={}):
    property_obj = obj.pool.get('ir.property')
    prop_ids = property_obj.search(cr, uid, [('name', '=', 'analytics_distribution_default')],context=context)
    if len(prop_ids)>0:
        return property_obj.read(cr,uid,prop_ids[0],['value_integer'],context=context)['value_integer']
    return False

class account_invoice_line(osv.osv):
    _name = "account.invoice.line"
    _inherit="account.invoice.line"

    _columns = {
        'analytics_id': fields.many2one('account.analytic.plan.instance', 'Analytic Distribution', required=True),
    }

    _defaults = {
        'analytics_id': lambda obj, cr, uid, context: _get_property_value(obj,cr,uid,context)
    }

account_invoice_line()

class sale_order_line(osv.osv):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    def _prepare_order_line_invoice_line(self, cr, uid, line, account_id=False, context={}):
        vals = super(sale_order_line,self)._prepare_order_line_invoice_line(cr,uid,line,account_id,context=context)
        if 'analytics_id' not in vals:
            vals['analytics_id'] = _get_property_value(self, cr, uid, context)
        return vals

sale_order_line()
