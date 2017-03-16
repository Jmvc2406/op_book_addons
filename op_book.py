# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
import logging
logging.basicConfig(level=logging.INFO)

class op_book(osv.osv):
    _inherit = "op.book"

    _columns = {
        'codigo_barras': fields.char(size=12, string='Codigo Barras', required=False),
	    'book_comments': fields.one2many('op.book.comments', 'book_id', 'Comentarios'),
	    'publicacion': fields.many2one('res.country'),
    }

op_book()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
