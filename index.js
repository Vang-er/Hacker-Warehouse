let welcome_back = document.getElementById("log_in_box");
let welcome = document.getElementById("sign_up_box")
let next = document.getElementById("next")
let mail = document.getElementById("mail")
let input_mail = document.getElementById("input_mail")
let create_pass_lab = document.getElementById("create_pass_lab")
let pass1 = document.getElementById("pass1")
let confirm_pass = document.getElementById("confirm_pass")
let confirm_pass_input = document.getElementById("confirm_pass_input")


function newuser(){
   welcome_back.style.display = "none"
   welcome.style.display = "block"
}
function thenext(){
   mail.style.display = "none"
   input_mail.style.display = "none"
   create_pass_lab.style.display = "none"
   pass1.style.display = "none"
   confirm_pass.style.display = "none"
   confirm_pass_input.style.display = "none"
}