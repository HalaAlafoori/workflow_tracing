# Copyright (c) 2024, SanU Development Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Transaction(Document):
    def before_save(self):
		# self.fields.get("from_department").hidden = 0
        if self.outgoing:
            department = frappe.get_doc("Department", "Accounts")
            if department:
                self.from_department = department.name		


# class Transaction(Document):
#     def before_save(self):
#         if self.outgoing:
#             department = frappe.get_doc("Department", "Accounts")
#             if department:
#                 self.from_department = department.name

#         # self.get("from_department").hidden = 0