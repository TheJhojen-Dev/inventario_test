# -*- coding: utf-8 -*-
{
    "name": "Inventario Test",
    "version": "18.0.1.0.0",
    "summary": "Simulación de inventario para ferretería con Spreadsheet Dashboard",
    "category": "Inventory",
    "author": "Tecnosoft",
    "website": "https://tecnosoft.dev",
    "license": "LGPL-3",
    "depends": [
        "base",
        "spreadsheet_dashboard",
        "daily_tax",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/data.xml",
        "views/views.xml",
        "views/report_ferreteria_template.xml",
    ],
    "application": True,
}
