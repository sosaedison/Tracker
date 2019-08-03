var app;
function Init() {
    console.log('hi Init()');
    app = new Vue({
        el: '#login',
        data: {
            username: '',
            password: '',
            db: 'http://127.0.0.1:1234/login',
        methods: {
            
        },
    }
        
    });
}



function Login(event) {
    
	var response = GetJson(app.db+'?username='+app.username+'&password='+app.password).then((data) => {
        console.log(data);
        data.forEach(element => {
            console.log(element)
        });
	});
    console.log("response")
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