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
        }
	});
}

function Register(event) {
	console.log('hi register');
	console.log(app.db);
	if(app.username.length < 2) { alert("Your Username must be at least 2 characters!"); }
	if(app.avatar === '') { alert('Please select your Avitar');}
	if((app.password === app.passwordcon) && app.password!= '' && app.avitar != '') {
		PostJson(app.db+'?username='+app.username +'&password=' + app.password + '&company=' +app.company).then((data) => {
			console.log("post POST");
			window.location.href="BlackJack.html";
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