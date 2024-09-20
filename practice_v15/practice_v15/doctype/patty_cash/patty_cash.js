// Copyright (c) 2024, NexTash and contributors
// For license information, please see license.txt

frappe.ui.form.on("Patty Cash", {
  //jb hamamra  form 1st time setup hota ha tb setup wali command challty hain 
	refresh(frm) {
//       frappe.msgprint("this is frappe setup command")
//       if (frappe.user_roles.includes('HR')) {
//     frm.enable_save();
// } else {
//     frm.disable_save();
// }

// if (frm.is_dirty()) {
//     frappe.show_alert('Please save form before attaching a file')
// }
// frm.doc.browser_data = navigator.appVersion;
// frm.dirty();
// frm.save();

if (!frm.doc.date) {
    frm.set_intro('Please set the value of Date', 'red');
}

// Custom buttons
frm.add_custom_button('Open Reference form', () => {
    frappe.set_route('Form', frm.doc.refe, frm.doc.reference_name);
})

// Custom buttons in groups
frm.add_custom_button('Closed', () => {
    frm.doc.status = 'Closed'
}, 'Set Status');

// change type of ungrouped button
frm.change_custom_button_type('Open Reference form', null, 'primary');

// change type of a button in a group
frm.change_custom_button_type('Closed', 'Set Status', 'danger');
frm.change_custom_button_type('Open', 'Set Status', 'primary');


	},
	// onload_post_render(frm) {
  //     frappe.msgprint("this is frappe onload_post_render command")
	// },
});
