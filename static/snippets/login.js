console.log('hi Init()');
let app = new Vue({
    el: '#login',
    data: {
        username: '',
        password: '',
        login_db: 'http://127.0.0.1:1234/',
        username_db: 'http://127.0.0.1:1234/usernamedump',
        usernames: [],
    },
    methods: {
        
    },
});

function GetUsernames() {
    var response = GetJson(app.username_db).then((data) =>{
        PullUsernames(data);
    })
}

function PullUsernames(data) {
    var temp_arr = [];
    for (let index = 0; index < data.length; index++) [
        temp_arr.push()
    ]
}



function Login(event) {
    
	var response = PostJson(app.login_db+'?username='+app.username+'&password='+app.password).then((data) => {
        console.log(data);
        
	});
}

function GetJson(url) {
	return new Promise((resolve, reject) => {
	console.log('hi promise');
		$.get(url, (data) => {
		console.log('hi GET');
			resolve(data);
		}, "json");
	});
}

function PostJson(url) {
	return new Promise((resolve, reject) => {
	console.log('hi promise');
		$.post(url, (data) => {
		console.log('hi GET');
			resolve(data);
		}, "json");
	});
}