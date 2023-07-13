
function validateform(){  
    var firstName=document.newUserFrom.firstname.value;   
    var lastName=document.newUserFrom.lastname.value; 
    
    var email=document.newUserFrom.email.value;
    var atposition=email.indexOf("@");  
    var dotposition=email.lastIndexOf(".");  

    var password=document.newUserFrom.userpassword.value;
    var repassword=document.newUserFrom.userrepassword.value;

    if (firstName==null || firstName==""){  
      alert("First Name must is Required !!");  
      return false;  
    }else if(firstName.length < 4){  
        alert("First Name must be at least 4 characters long or more !!");  
        return false;  
    }else if(lastName==null || lastName==""){
        alert("Last Name must is Required !!");  
        return false;
    }else if(lastName.length < 4){
        alert("Last Name must be at least 4 characters long or more !!");  
        return false;
    }else if (atposition<1 || dotposition<atposition+2 || dotposition+2>=x.length){  
        alert("Please enter a valid e-mail address !!\n"+email);  
        return false;  
    }else if (password==null || password==""){  
        alert("Password must is Required !!");  
        return false;  
      }else if(password.length < 6){  
          alert("Password must be at least 6 characters and number long or more !!");  
          return false;  
      }else if(repassword==null || repassword==""){
        alert("Repassword must is Required !!");
        return false;
      }else if(repassword.length < 6){
        alert("Repassword must be at least 6 characters and number long or more !!"); ;  
        return false;
      }


}

console.log("Authenticate")

function passToggle() {
    var pass = document.getElementById("exampleInputPassoword");
    var repass = document.getElementById("exampleInputConfirm");
    if (pass.type === "password") {
        pass.type = "text";
    }else{
        pass.type = "password";
    }
    if (repass.type === "password") {
        repass.type = "text";
    }else{
        repass.type = "password";
    }
}








