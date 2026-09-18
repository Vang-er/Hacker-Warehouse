const stock = document.getElementById("your")
const add = document.getElementById("add")
const dashboard = document.getElementById("dash")
const stockdiv = document.getElementById("stockdiv")
const adddiv = document.getElementById("adddiv")
const dashdiv = document.getElementById("dashdiv")
let butnum = 0;












function chosestock(){
stock.style.backgroundColor = "#78cc78"
stock.style.borderRadius = "20px"
add.style.backgroundColor = "#fff"
add.style.borderRadius = "0px"
dashboard.style.backgroundColor = "#fff"
dashboard.style.borderRadius = "0px"
stockdiv.style.display = "block"
adddiv.style.display = "none"
dashdiv.style.display = "none"
}
function choseadd(){
add.style.backgroundColor = "#78cc78"
add.style.borderRadius = "20px"
stock.style.backgroundColor = "#fff"
stock.style.borderRadius = "0px"
dashboard.style.backgroundColor = "#fff"
dashboard.style.borderRadius = "0px"
stockdiv.style.display = "none"
adddiv.style.display = "block"
dashdiv.style.display = "none"
}
function chosedash(){
dashboard.style.backgroundColor = "#78cc78"
dashboard.style.borderRadius = "20px"
add.style.backgroundColor = "#fff"
add.style.borderRadius = "0px"
stock.style.backgroundColor = "#fff"
stock.style.borderRadius = "0px"
stockdiv.style.display = "none"
adddiv.style.display = "none"
dashdiv.style.display = "block"
}