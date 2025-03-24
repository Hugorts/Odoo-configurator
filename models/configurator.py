from odoo import models, fields, api
import os
import importlib.util
from odoo.exceptions import UserError

class Configurator(models.Model):
    _name = 'configurator.manager'
    _description = 'Configurator Manager'

    name = fields.Char(string='Script/File Name', required=True)
    file_path = fields.Char(string='File Path', required=True)
    script_type = fields.Selection([
        ('role', 'Role Script'),
        ('translation', 'Translation Script'),
        ('account', 'Account Script'),
    ], string='Script Type', required=True)

    # def run_script(self):
    #     for record in self:
    #         script_path = os.path.join(os.path.dirname(__file__), '..', 'scripts', f"{record.file_path}.py")
    #         if os.path.exists(script_path):
    #             # Импортируем и выполняем скрипт
    #             spec = importlib.util.spec_from_file_location(record.file_path, script_path)
    #             module = importlib.util.module_from_spec(spec)
    #             spec.loader.exec_module(module)
    #             module.main()  # Предполагается, что в скрипте есть функция main()
    #             return {
    #                 'type': 'ir.actions.client',
    #                 'tag': 'display_notification',
    #                 'params': {
    #                     'title': 'Success',
    #                     'message': f"Script {record.name} executed successfully!",
    #                     'sticky': False,
    #                 }
    #             }
    #         else:
    #             raise UserError(f"Script {record.file_path} not found!")