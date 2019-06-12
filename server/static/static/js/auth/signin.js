$("#form").submit(function(e) {
    e.preventDefault();
});

function signin() {
	name = document.getElementById("username").value;
	pwd = document.getElementById("password").value;

	form = new FormData()
	form.append("username", name)
	form.append("password", pwd)

	$.ajax({
		url: document.location.href,
		type: "POST",
		data: form,
		headers: {"X-CSRFToken": token},
		processData: false,
		contentType: false,
		success: function (data) {
			if (data == "ok")
				window.location.href = "/auth/account/"
			else
				Swal.fire({
					type: 'error',
					text: data,
				})
		}
	})
	return false;
}
