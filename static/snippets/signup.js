let app
function Init() {
	console.log('hi Init');
	app = new Vue({
		el: '#app',
		data: {
			username: '',
			password: '',
			db: "http://127.0.0.1:5000/register",
			passwordcon:'',
			company: '',
			name: '',
			email:'',
			password_confirm: '',
			companyvalid: false,
			usernamevalid: false,
			emailvalid: false,
        }
	});
	AddListeners();
}

function AddListeners() {
	let submit_button = document.getElementById("submit")
	let company = document.getElementById("company")
	let name = document.getElementById("name")
	let email = document.getElementById("email")
	let username = document.getElementById("username")

	company.addEventListener("keyup", (event) => {
		if(company.value.length > 1){
			console.log(" ")
			console.log("length true")
			if (isValidCompany(company.value) == true) {
				console.log("true data")
				company.style.borderColor = "red"
			} else {
				console.log("false data")
				company.style.borderColor = "white"
			}
		} else {
			console.log("length false")
			company.style.borderColor = "white"
		}
	})
}

function Register(event) {
	PostJson(app.db+'?username='+app.username +'&password=' + app.password + '&company=' +app.company).then((data) => {
		
		console.log(data);
	})
}

function isValidCompany(company) {
	GetJson(app.db+'?company='+company+"&src=checkcompany").then((data) => {
		
		console.log(data+" data")
		
		if(data == true){
			return true
		}
		return false
	})
}

function PostJson(url) {
	return new Promise((resolve, reject) => {
		$.post(url, (data) => {
		console.log('hi post');
			resolve(data);
		}, "json");
	});
}

function GetJson(url) {
	return new Promise((resolve, reject) => {
		$.get(url, (data) => {
		console.log('hi get');
			resolve(data);
		}, "json");
	});
}