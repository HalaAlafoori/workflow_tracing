// Copyright (c) 2024, SanU Development Team and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Transaction", {
// 	refresh(frm) {

// 	},
// });

// restrect choosing of Incoming and Outgoing check box
frappe.ui.form.on('Transaction', {
    refresh: function(frm) {
        frm.toggle_reqd('incoming', !frm.doc.outgoing);
    },
    outgoing: function(frm) {
        frm.doc.incoming = !frm.doc.outgoing;
        frm.refresh_field('incoming');
    },
    incoming: function(frm) {
        frm.doc.outgoing = !frm.doc.incoming;
        frm.refresh_field('outgoing');
    }
});

// set the "Start Date" field to the current date by default 
frappe.ui.form.on('Transaction', {
    onload: function(frm) {
        if (!frm.doc.start_date) {
            frm.set_value('start_date', frappe.datetime.get_today());
        }
    }
});
