app_name = "testapp"
app_title = "Test App"
app_publisher = "Web Notes"
app_description = "Test App"
app_icon = "icon-book"
app_color = "#FFBBFF"
app_email = "pdvyas@gmail.com"
app_url = "https://frappe.io"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/testapp/css/testapp.css"
# app_include_js = "/assets/testapp/js/testapp.js"

# include js, css files in header of web template
# web_include_css = "/assets/testapp/css/testapp.css"
# web_include_js = "/assets/testapp/js/testapp.js"

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

# Installation
# ------------

# before_install = "testapp.install.before_install"
# after_install = "testapp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "testapp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"testapp.tasks.all"
# 	],
# 	"daily": [
# 		"testapp.tasks.daily"
# 	],
# 	"hourly": [
# 		"testapp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"testapp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"testapp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "testapp.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.core.doctype.event.event.get_events": "testapp.event.get_events"
# }

