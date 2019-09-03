var app;
function Init() {
	console.log('hi Init()');
	app = new Vue({
		el: '#app',
		data: {
			username: '',
			password: '',
			db: 'http://127.0.0.1:1234/register',
			passwordcon:'',
			company: '',
			name: '',
			email:'',
			password_confirm: '',
        }
	});
	AddListeners();
}

function AddListeners() {
	document.getElementById("name").addEventListener("input", (event) => {
		CheckName(app.name)
	})
	document.getElementById("email").addEventListener("input", (event) => {
		CheckName(app.email)
	})
	document.getElementById("company").addEventListener("input", (event) => {
		CheckName(app.company)
	})
	document.getElementById("username").addEventListener("input", (event) =>{ 
		CheckName(app.username)
	})
}

function CheckName (name) {
	PostJson(app.db+'?name='+name+'&src='+'checkname').then((data) => {
		console.log(data);
		return true
	})
}
function Register(event) {
	console.log('hi register');
	console.log(app.db);
	if(app.username.length < 2) { alert("Your Username must be at least 2 characters!"); }
	if((app.password === app.passwordcon) && app.password!= '') {
		PostJson(app.db+'?username='+app.username +'&password=' + app.password + '&company=' +app.company).then((data) => {
			console.log(data);
		})
	} else { alert("Your password didn't match!"); }
}

function PostJson(url) {
	return new Promise((resolve, reject) => {
	console.log('hi promise and url: ' + url);
		$.post(url, (data) => {
		console.log('hi post');
			resolve(data);
		}, "json");
	});
}