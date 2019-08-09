let app = new Vue ({
    el: '#app',
    data: {
        message: "hello",
        username: '',
        password: '',
        passwordrepeat: '',
        company: '',
        data_arr: [],
        company_data_url: 'http://127.0.0.1:1234/datadump'
    },    
})

function GetData() {
    GetJson(app.company_data_url).then((data) =>{
        ParseData(data);
    })
}

function ParseData (data) {
    var temp_arr = []
    for (let index = 0; index < data.length; index++) {
        var session = data[index][4]
        temp = {
            "game": data[index][1],
            "date": data[index][2],
            "session": data[index][4].toFixed(2),
            "bay_id": data[index][5],
        }
        temp_arr.push(temp);
        MakeTable(temp.bay_id, temp.game, temp.session, temp.date)
    }
    app.data_arr = temp_arr;
    console.log(app.data_arr);
}

function MakeTable(bay_id, game, session, date) {

    let table = document.getElementById("table-for-data");

    let row = table.insertRow(0);
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    let cell3 = row.insertCell(2);
    let cell4 = row.insertCell(3);
    
    cell1.innerHTML = bay_id;
    cell2.innerHTML = game;
    cell3.innerHTML = session;
    cell4.innerHTML = date;
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