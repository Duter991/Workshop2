$("#form").submit(function(e) {
    e.preventDefault();
});

function signup() {
	name = document.getElementById("username").value;
	email = document.getElementById("email").value;
	pwd = document.getElementById("password").value;
	confpwd = document.getElementById("confirm_password").value;
	firstName = document.getElementById("firstName").value;
	lastName = document.getElementById("lastName").value;

	if (pwd != confpwd) {
		Swal.fire({
			type: 'error',
			text: "Passwords does not match.",
		})
		return
	}

	form = new FormData()
	form.append("username", name)
	form.append("password", pwd)
	form.append("email", email)
	form.append("firstName", firstName)
	form.append("lastName", lastName)

	$.ajax({
		url: document.location.href,
		type: "POST",
		data: form,
		headers: {"X-CSRFToken": token},
		processData: false,
		contentType: false,
		success: function (data) {
			if (data == "ok")
				window.location.href = "/auth/account"
			else
				Swal.fire({
					type: 'error',
					text: data,
				})
		}
	})
	return false;
}
