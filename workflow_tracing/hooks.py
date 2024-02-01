app_name = "workflow_tracing"
app_title = "Workflow Tracing"
app_publisher = "SanU Development Team"
app_description = "A frappe web-based appplication that adds a workflow tracing features and reports"
app_email = "eng.bakraldubai@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/workflow_tracing/css/workflow_tracing.css"
# app_include_js = "/assets/workflow_tracing/js/workflow_tracing.js"

# include js, css files in header of web template
# web_include_css = "/assets/workflow_tracing/css/workflow_tracing.css"
# web_include_js = "/assets/workflow_tracing/js/workflow_tracing.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "workflow_tracing/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "workflow_tracing/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "workflow_tracing.utils.jinja_methods",
#	"filters": "workflow_tracing.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "workflow_tracing.install.before_install"
# after_install = "workflow_tracing.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "workflow_tracing.uninstall.before_uninstall"
# after_uninstall = "workflow_tracing.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "workflow_tracing.utils.before_app_install"
# after_app_install = "workflow_tracing.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "workflow_tracing.utils.before_app_uninstall"
# after_app_uninstall = "workflow_tracing.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "workflow_tracing.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"workflow_tracing.tasks.all"
#	],
#	"daily": [
#		"workflow_tracing.tasks.daily"
#	],
#	"hourly": [
#		"workflow_tracing.tasks.hourly"
#	],
#	"weekly": [
#		"workflow_tracing.tasks.weekly"
#	],
#	"monthly": [
#		"workflow_tracing.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "workflow_tracing.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "workflow_tracing.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "workflow_tracing.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["workflow_tracing.utils.before_request"]
# after_request = ["workflow_tracing.utils.after_request"]

# Job Events
# ----------
# before_job = ["workflow_tracing.utils.before_job"]
# after_job = ["workflow_tracing.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"workflow_tracing.auth.validate"
# ]
