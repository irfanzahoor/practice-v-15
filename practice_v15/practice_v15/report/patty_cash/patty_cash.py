import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"fieldname": "transaction_id", "label": "Transaction ID", "fieldtype": "Data"},
        {"fieldname": "amount", "label": "Amount", "fieldtype": "Currency"},
        {"fieldname": "category", "label": "Category", "fieldtype": "Data"},
        {"fieldname": "payee", "label": "Payee", "fieldtype": "Data"},
        {"fieldname": "received_by", "label": "Received By", "fieldtype": "Data"},
        {"fieldname": "approved_by", "label": "Approved By", "fieldtype": "Data"},
        {"fieldname": "balance", "label": "Balance", "fieldtype": "Currency"},
        {"fieldname": "transaction_type", "label": "Transaction Type", "fieldtype": "Data"},
        {"fieldname": "currency", "label": "Currency", "fieldtype": "Link", "options": "Currency"},
        {"fieldname": "date", "label": "Date", "fieldtype": "Date"}
    ]

def get_data(filters):
    conditions = build_conditions(filters)
    data = frappe.get_all(
        "Patty Cash",
        filters=conditions,
        fields=[
            "name as transaction_id", "amount", "category", "payee", "received_by",
            "approved_by", "balance", "transaction_type", "currency", "date"
        ]
    )

    total_balance, total_amount = calculate_totals(data)

    if data:
        data.append({
            "transaction_id": "Total",
            "amount": total_amount,
            "category": "",
            "payee": "",
            "received_by": "",
            "approved_by": "",
            "balance": total_balance,
            "transaction_type": "Exceeds Balance" if total_amount > total_balance else "",
            "currency": "",
            "date": ""
        })

    return data

def build_conditions(filters):
    conditions = []
    if filters.get("transaction_id"):
        conditions.append(["name", "=", filters["transaction_id"]])
    if filters.get("start_date"):
        conditions.append(["date", ">=", filters["start_date"]])
    if filters.get("end_date"):
        conditions.append(["date", "<=", filters["end_date"]])
    return conditions

def calculate_totals(data):
    total_balance = total_amount = 0
    for item in data:
        total_balance += safe_float(item.get('balance'))
        total_amount += safe_float(item.get('amount'))
    return total_balance, total_amount

def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0

import logging

def get_data(filters):
    conditions = build_conditions(filters)
    data = frappe.get_all(
        "Patty Cash",
        filters=conditions,
        fields=[
            "name as transaction_id", "amount", "category", "payee", "received_by",
            "approved_by", "balance", "transaction_type", "currency", "date"
        ]
    )

    total_balance, total_amount = calculate_totals(data)

    logging.debug(f"Data fetched: {data}")

    if data:
        data.append({
            "transaction_id": "Total",
            "amount": total_amount,
            "category": "",
            "payee": "",
            "received_by": "",
            "approved_by": "",
            "balance": total_balance,
            "transaction_type": "Exceeds Balance" if total_amount > total_balance else "",
            "currency": "",
            "date": ""
        })

    return data
