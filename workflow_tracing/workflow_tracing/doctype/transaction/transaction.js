// Copyright (c) 2024, SanU Development Team and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Transaction", {
// 	refresh(frm) {

// 	},
// });

// restrect choosing of Incoming and Outgoing check box
frappe.ui.form.on('Transaction', {
    // refresh: function(frm) {
    //     frm.toggle_reqd('incoming', !frm.doc.outgoing);
    // },
    // outgoing: function(frm) {
    //     frm.doc.incoming = !frm.doc.outgoing;
    //     frm.refresh_field('incoming');
    // },
    // incoming: function(frm) {
    //     frm.doc.outgoing = !frm.doc.incoming;
    //     frm.refresh_field('outgoing');
    // }

    outgoing: function(frm) {
        if(frm.doc.outgoing){
            frm.doc.incoming = false;
        }
        frm.refresh_field('incoming');
    },
    incoming: function(frm) {
        if(frm.doc.incoming){
            frm.doc.outgoing = false;
        }
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

///////////////////

// hide (From Department) and (To Department) until select (Incoming) or (Outgoing)

frappe.ui.form.on('Transaction', {
    incoming: function(frm) {
        toggleDepartmentFieldsVisibility(frm);
    },
    outgoing: function(frm) {
        toggleDepartmentFieldsVisibility(frm);
    },
    refresh: function(frm) {
        toggleDepartmentFieldsVisibility(frm);
    }
});

function toggleDepartmentFieldsVisibility(frm) {
    // Get references to the fields
    var fromDeptField = frm.fields_dict.from_department;
    var toDeptField = frm.fields_dict.to_department;

    // Check if either checkbox is checked
    var incomingChecked = frm.doc.incoming;
    var outgoingChecked = frm.doc.outgoing;

    // Set field visibility based on checkbox state
    fromDeptField.df.hidden = !(incomingChecked || outgoingChecked);
    toDeptField.df.hidden = !(incomingChecked || outgoingChecked);

    // Refresh the form to apply the visibility changes
    frm.refresh_field('from_department');
    frm.refresh_field('to_department');
}

  //////////////////
  
  
//   frappe.ui.form.on('Transaction', {
//     party: function(frm) {
//         if (frm.doc.party === 'Internal') {
//             frappe.call({
//                 method: 'frappe.client.get_list',
//                 args: {
//                     doctype: 'Department',
//                     // filters: { /* Add any filters if needed */ },
//                     fields: ['department_name'],
//                     // parent: 'Setup'
//                 },
//                 callback: function(response) {
//                     console.log(response.message.map(d => d.name))
//                     // if (response.message && Array.isArray(response.message)) {

//                     //     frm.set_df_property('from_department', 'options', response.message.map(d => d.name));
//                     // }
//                 }
//             });
//         } else if (frm.doc.party === 'External') {
//             // Add logic for the 'External' case if needed
//         }
//     }
// });


// frappe.ui.form.on('Transaction', {
//     party: function(frm) {
//         if (frm.doc.party === 'Internal') {

//         } else if (frm.doc.party === 'External') {
        
//         }
//     }
// });
