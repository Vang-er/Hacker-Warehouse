let welcome_back = document.getElementById("log_in_box");
let welcome = document.getElementById("sign_up_box");
let next = document.getElementById("next");
let mail = document.getElementById("mail");
let input_mail = document.getElementById("input_mail");
let create_pass_lab = document.getElementById("create_pass_lab");
let pass1 = document.getElementById("pass1");
let submit = document.getElementById("submit");

function newuser() {
  welcome_back.style.display = "none";
  welcome.style.display = "block";
}
function thenext() {
  mail.style.display = "none";
  input_mail.style.display = "none";
  create_pass_lab.style.display = "none";
  pass1.style.display = "none";
  confirm_pass.style.display = "none";
  confirm_pass_input.style.display = "none";
  back.style.display = "block";
  next.style.display = "none";
  submit.style.display = "block";
}

function main(event) {
  event.preventDefault();

  window.location.href = "dashboard/";
}

function theback() {
  welcome_back.style.display = "block";
  welcome.style.display = "none";
}

const signupForm = document.getElementById("signupForm");

signupForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirmPassword").value;
  const passwordError = document.getElementById("passwordError");

  if (password !== confirmPassword) {
    passwordError.textContent = "Passwords do not match!";
    passwordError.style.color = "red";
    return;
  }

  passwordError.textContent = "Passwords match!";
  passwordError.style.color = "green";

  event.preventDefault();

  window.location.href = "Dashboard/";
});
