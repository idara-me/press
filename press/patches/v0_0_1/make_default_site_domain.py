# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe


def execute():
	frappe.reload_doc("press", "doctype", "site")
	for site in frappe.db.get_all(
		"Site", {"status": ("!=", "Archived")}, pluck="name"
	):
		frappe.get_doc("Site", site)._create_default_site_domain()
