function checkName(text){
    var re = /^[А-Я](?=[а-я]+)/
    return re.test(text)
}
function checkMail(text){
    var re = /^[\w-\.]+@[\w-]+\.[a-z]{2,4}$/i;
    return re.test(text)
}
function checkLogin(text){
    var re = /^[a-z]+([-_]?[a-z0-9]+){0,2}$/i;
    return re.test(text)
}
function checkPassword(text){
    var re = /(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{8,}/g;
    return re.test(text)
}
function allowREG(){
    var self = allow;
    var p = document.getElementById('Button');
    if (self.Login && self.Pass && self.Email && self.Surname && self.Name){
        p.innerHTML = '<button type="submit" class="btn" style="background-color: #580085; color: white;">Зарегестрироваться</button>'
    }
    else{
        p.innerHTML = '<button type="submit" class="btn" style="background-color: #580085; color: white;" disabled>Зарегестрироваться</button>'
    }
}
function allowLogin(cond){
    var p = document.getElementById('login_text');
    if(cond){
        p.innerHTML = '<h5 class="green-text"><i class="fas fa-check green-text" ></i>  поле заполнено верно</h5>';
        allow.Login = true;
    }
    else{
        p.innerHTML = '<h5 class="red-text"><i class="fas fa-times red-text" ></i> поле заполнено неверно</h5>';
        allow.Login = false;
    }
    allowREG();
}
function allowPassword(cond){
    var p = document.getElementById('password_text');
    if(cond){
        p.innerHTML = '<h5 class="green-text"><i class="fas fa-check green-text" ></i>  поле заполнено верно</h5>';
        allow.Pass = true;
    }
    else{
        p.innerHTML = '<h5 class="red-text"><i class="fas fa-times red-text" ></i> поле заполнено неверно</h5>';
        allow.Pass= false;
    }
    allowREG();
}
function allowName(cond){
    var p = document.getElementById('name_text');
    if(cond){
        p.innerHTML = '<h5 class="green-text"><i class="fas fa-check green-text" ></i>  поле заполнено верно</h5>';
        allow.Name = true;
    }
    else{
        p.innerHTML = '<h5 class="red-text"><i class="fas fa-times red-text" ></i> поле заполнено неверно</h5>';
        allow.Name = false;
    }
    allowREG();
}
function allowSurname(cond){
    var p = document.getElementById('surname_text');
    if(cond){
        p.innerHTML = '<h5 class="green-text"><i class="fas fa-check green-text" ></i>  поле заполнено верно</h5>';
        allow.Surname = true;
    }
    else{
        p.innerHTML = '<h5 class="red-text"><i class="fas fa-times red-text" ></i> поле заполнено неверно</h5>';
        allow.Surname = false;
    }
    allowREG();
}
function allowEmail(cond){
    var p = document.getElementById('mail_text');
    if(cond){
        p.innerHTML = '<h5 class="green-text"><i class="fas fa-check green-text" ></i>  поле заполнено верно</h5>';
        allow.Email = true;
    }
    else{
        p.innerHTML = '<h5 class="red-text"><i class="fas fa-times red-text" ></i> не соответствует формату почты</h5>';
        allow.Email = false;
    }
    allowREG();
}
allow.Login = true;
allow.Pass = true;
allow.Name = true;
allow.Surname = true;
allow.Email = true;
