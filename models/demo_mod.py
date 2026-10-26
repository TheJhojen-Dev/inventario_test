# -*- coding: utf-8 -*-
from odoo import models, fields, api


class FerreteriaCategoria(models.Model):
    _name = "ferreteria.categoria"
    _description = "Categoría de Ferretería"
    _order = "name"

    name = fields.Char(string="Categoría", required=True)
    description = fields.Text(string="Descripción")
    producto_ids = fields.One2many(
        "ferreteria.producto", "categoria_id", string="Productos"
    )


class FerreteriaProducto(models.Model):
    _name = "ferreteria.producto"
    _description = "Producto de Ferretería"
    _order = "name"

    codigo = fields.Char(string="Código / SKU", required=True, copy=False)
    name = fields.Char(string="Descripción / Nombre", required=True)
    categoria_id = fields.Many2one(
        "ferreteria.categoria", string="Categoría", required=True
    )
    unidad_medida = fields.Selection(
        [
            ("unidad", "Unidad"),
            ("metro", "Metro"),
            ("kg", "Kilogramo"),
            ("litro", "Litro"),
            ("caja", "Caja / Paquete"),
        ],
        string="Unidad de Medida",
        default="unidad",
        required=True,
    )
    ubicacion = fields.Char(
        string="Ubicación / Pasillo / Estante",
        help="Ejemplo: Pasillo 3, Estante B-2",
    )
    stock_actual = fields.Float(string="Stock Actual", default=0.0)
    stock_minimo = fields.Float(string="Stock Mínimo", default=5.0)
    precio_costo = fields.Float(string="Costo Unitario ($)", default=0.0)
    precio_venta = fields.Float(string="Precio Venta ($)", default=0.0)
    estado = fields.Selection(
        [
            ("disponible", "En Stock"),
            ("bajo_stock", "Stock Bajo"),
            ("agotado", "Agotado"),
        ],
        string="Estado",
        compute="_compute_estado",
        store=True,
    )
    active = fields.Boolean(string="Activo", default=True)

    @api.depends("stock_actual", "stock_minimo")
    def _compute_estado(self):
        for rec in self:
            if rec.stock_actual <= 0:
                rec.estado = "agotado"
            elif rec.stock_actual <= rec.stock_minimo:
                rec.estado = "bajo_stock"
            else:
                rec.estado = "disponible"

