function Init() {
    console.log("Hi Init")
    let app = new Vue ({
        el: '#app',
        data: {
            username: '',
            password: '',
            login_url: "http://127.0.0.1:5000/login?"
        },    
    })
}

function Login (){
    PostJson(app.login_url+"username="+app.username+"&password="+app.password).then((data) => {
        console.log(data)
    });
}

function GetJson (url) {
    return new Promise((resolve, reject) => {
        $.get(url, (data) => {
            resolve(data);
        }, "json");
    });
}

function PostJson (url) {
    return new Promise((resolve, reject) => {
        $.post(url, (data) => {
            resolve(data);
        }, "json");
    });
}