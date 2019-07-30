function rec()
{
    var user,fname;
    user = document.getElementById("username").value;
    fname = document.getElementById("fname").value;

    var j = {
        "username": user,
        "fname": fname

    };

    var s = JSON.stringify(j);

    request(s);



    
}

function request(a)
{
    var xmlhttp = new XMLHttpRequest();
    
    xmlhttp.open("PUT", "http://127.0.0.1:8000/test/data/", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send(a);

}