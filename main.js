const stock = document.getElementById("your")
const add = document.getElementById("add")
const dashboard = document.getElementById("dash")
const stockdiv = document.getElementById("stockdiv")
const adddiv = document.getElementById("adddiv")
const dashdiv = document.getElementById("dashdiv")
const catadd = document.getElementById("catadd")
const catname = document.getElementById("catname")
const catdes = document.getElementById("catdes")
const theadd = document.getElementById("theadd")
const backbut = document.getElementById("back")
const submit = document.getElementById("submit")
const newproduct = document.getElementById("newproduct")
const inputproname = document.getElementById("inputproname")



let parentcatname = []
let parentnum = 0;
let parentcatdes = []
let parentdesnum = 0;
let isthereproduct = false;
let productlist = []
let saveprolist = 0


function done(){
productlist[saveprolist] = inputproname.value 
}
function x(){
    newproduct.style.display = "none"
}
function addpro(){
    newproduct.style.display = "flex"
}
function enter(event){
    event.preventDefault();
    parentcatname[parentnum] = catname.value
    parentcatdes[parentdesnum] = catdes.value
    
    
    back()
    isthereproduct = true
    stockdiv.innerHTML = `
    <div class="boxes" id="box1">
    <p class="catigoryname">${parentcatname[parentnum]}</p>
    <div class="prodectbuttonsdiv" id="prodectbuttons">
    <button class="prodectbuttons" id="addprodect">Add prodect</button>
    <button class="prodectbuttons" id="delprodect">Remove prodect</button>
</div>
</div>
    `
    catname.value = ""
    catdes.value = ""
    parentnum ++
    parentdesnum ++
}

function back(){
    theadd.style.display = "none"
    catadd.style.display = "block"
}

function newcategory(){
    catadd.style.display = "none"
    theadd.style.display = "block"
}

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