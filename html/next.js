function myfunc() {

    var fname, lname, add, city, st, zip, scb, hq, phno, email, gen, user, pass;


    fname = document.getElementById("fname").value;
    lname = document.getElementById("lname").value;
    add = document.getElementById("add").value;
    city = document.getElementById("city").value;
    st = document.getElementById("state").value;
    zip = document.getElementById("zip").value;
    scb = document.getElementById("scb").value;
    hq = document.getElementById("hq").value;
    phno =  document.getElementById("phno").value;
    email = document.getElementById("email").value;
    user = document.getElementById("user").value;
    pass = document.getElementById("ps").value;
    gen = document.querySelector('input[name="rdb"]:checked').value;




    var j = {
        "fname": fname,
        "lname": lname,
        "address": add,
        "city": city,
        "state": st,
        "zip1": zip,
        "board": scb,
        "qualified": hq,
        "mobileno": phno,
        "email": email,
        "username": user,
        "password": pass,
        "gender": gen

    };


    var s = JSON.stringify(j);


    request(s);


}

function request(a) {

    var xmlhttp = new XMLHttpRequest();
    var data;


    xmlhttp.onreadystatechange = function () {

        document.write(" ");


        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            data = JSON.parse(xmlhttp.response);

            if (data.status1 == "ok")
            {
                alert('RECORD INSERTED');
                window.location.href = "/home/harsh/Desktop/html/login.html";
            } 
            
            
            else if (data.pass == "wrong") 
            {
                alert("User already exists!!                                                                  Please scroll down and find the Login button.                   But password is wrong.");
                window.location.href = "/home/harsh/Desktop/html/login.html";
            } 
            
            
            else if (data[0].link__fname) 
            {
                alert("User already exists!!                                                                  Please scroll down and find the Login button.");
                window.location.href = "/home/harsh/Desktop/html/login.html";
            }

        }

    }

    
    xmlhttp.open("POST", "http://127.0.0.1:8000/test/data/", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send(a);


}