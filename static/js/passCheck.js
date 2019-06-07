function checkL(text){
    var listL = ["_","-",".","@","0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
    var res = true;
    for (var i = 0; i < text.length; i++){
        if (!~listL.indexOf(text[i])){
            res = false;
            break;
        }
    }
    return res;
}
function checkP(text){
    var listP = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
    var res = true;
    for (var i = 0; i < text.length; i++){
        if (!~listP.indexOf(text[i])){
            res = false;
            break;
        }
    }
    return res;
}
function allow(){
    var self = allow;
    var p = document.getElementById('But');
    if (self.Login && self.Pass){
        p.innerHTML = '<button type="submit" id="Butt" class="btn" style="background-color: #580085; color: white;">Войти</button>'
    }
    else{
        p.innerHTML = '<button type="submit" id="Butt" class="btn" style="background-color: #580085; color: white;" disabled>Войти</button>'
    }
}
function allowL(cond){
    if(cond){
        TextL.setAttribute("style", "Opacity: 0; position: absolute");
        allow.Login = true;
    }
    else{
        TextL.setAttribute("style", "Opacity: 1; position: static");
        allow.Login = false;
    }
    allow();
}
function allowP(cond){
    if(cond){
        TextP.setAttribute("style", "Opacity: 0; position: absolute");
        allow.Pass = true;
    }
    else{
        TextP.setAttribute("style", "Opacity: 1; position: static");
        allow.Pass= false;
    }
    allow();
}
allow.Login = true;
allow.Pass = true;
