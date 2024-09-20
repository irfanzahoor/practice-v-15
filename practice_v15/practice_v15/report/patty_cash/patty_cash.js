frappe.query_reports["Patty Cash"] = {
	"filters": [
		{
			fieldname: "transaction_id",
			label: __("Transaction ID"),
			fieldtype: "Link",
			options: "Patty Cash"
		},
		{
			fieldname: "from_date",
			label: __("From Date"),
			fieldtype: "Date",
			default: frappe.datetime.month_start()
		},
		{
			fieldname: "to_date",
			label: __("To Date"),
			fieldtype: "Date",
			default: frappe.datetime.month_end()
		}
	]
};
