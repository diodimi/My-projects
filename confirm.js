function myFunction() {
    var name=document.getElementById("name").value;
    var tel=document.getElementById("tel").value;
    var question=document.getElementById("question").value;
    var email=document.getElementById("email").value;
    if(name!="" && question!="" && email!=""){
      window.open("part6.html");
    }


}

document.getElementById("newname").innerHTML=nn;
document.getElementById("newphone").innerHTML=tel;
document.getElementById("newquestion").innerHTML=question;
document.getElementById("newemail").innerHTML=email;
