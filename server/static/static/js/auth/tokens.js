function reveal() {
	document.getElementById("staticToken").type = 'text'
	document.getElementById("staticTokenButton").onclick = function() { blurToken() }
	document.getElementById("staticTokenButton").innerHTML = "Hide"
}

function blurToken()
{
	document.getElementById("staticToken").type = 'password'
	document.getElementById("staticTokenButton").onclick = function() {reveal() }
	document.getElementById("staticTokenButton").innerHTML = "Reveal"
}
