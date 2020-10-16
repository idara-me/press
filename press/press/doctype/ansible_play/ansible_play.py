# -*- coding: utf-8 -*-
# Copyright (c) 2020, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from frappe.model.document import Document


class AnsiblePlay(Document):
	def on_trash(self):
		frappe.db.delete("Ansible Task", {"play": self.name})
