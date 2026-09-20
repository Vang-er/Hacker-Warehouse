const stock = document.getElementById("your");
const add = document.getElementById("add");
const dashboard = document.getElementById("dash");
const stockdiv = document.getElementById("stockdiv");
const adddiv = document.getElementById("adddiv");
const dashdiv = document.getElementById("dashdiv");
const catadd = document.getElementById("catadd");
const catname = document.getElementById("catname");
const catdes = document.getElementById("catdes");
const theadd = document.getElementById("theadd");
const backbut = document.getElementById("back");
const submit = document.getElementById("submit");
const history = document.getElementById("history");
const historydiv = document.getElementById("histroydiv");
const historylist = document.getElementById("historylist")
const historycount = document.getElementById("historycount");

let parentcatname = [];
let parentnum = 0;
let parentcatdes = [];
let parentdesnum = 0;
let isthereproduct = false;

function enter(event) {
  event.preventDefault();
  parentcatname[parentnum] = catname.value;
  parentcatdes[parentdesnum] = catdes.value;

  back();
  isthereproduct = true;
  stockdiv.innerHTML = `
    <div class="boxes" id="box1">
    <p class="catigoryname">${parentcatname[parentnum]}</p>
    <div class="prodectbuttonsdiv" id="prodectbuttons">
    <button class="prodectbuttons" id="addprodect">Add prodect</button>
    <button class="prodectbuttons" id="delprodect">Remove prodect</button>
</div>
</div>
    `;
  catname.value = "";
  catdes.value = "";
  parentnum++;
  parentdesnum++;
}

function back() {
  theadd.style.display = "none";
  catadd.style.display = "block";
}

function newcategory() {
  catadd.style.display = "none";
  theadd.style.display = "block";
}

function chosestock() {
  stock.style.backgroundColor = "#78cc78";
  stock.style.borderRadius = "20px";
  add.style.backgroundColor = "#fff";
  add.style.borderRadius = "0px";
  dashboard.style.backgroundColor = "#fff";
  dashboard.style.borderRadius = "0px";
  history.style.backgroundColor = "#fff";
  history.style.borderRadius= "0px";
  stockdiv.style.display = "block";
  adddiv.style.display = "none";
  dashdiv.style.display = "none";
  historydiv.style.display = "none";
}
function choseadd() {
  add.style.backgroundColor = "#78cc78";
  add.style.borderRadius = "20px";
  stock.style.backgroundColor = "#fff";
  stock.style.borderRadius = "0px";
  dashboard.style.backgroundColor = "#fff";
  dashboard.style.borderRadius = "0px";
  stockdiv.style.display = "none";
  adddiv.style.display = "block";
  dashdiv.style.display = "none";
}
function chosedash() {
  dashboard.style.backgroundColor = "#78cc78";
  dashboard.style.borderRadius = "20px";
  add.style.backgroundColor = "#fff";
  add.style.borderRadius = "0px";
  stock.style.backgroundColor = "#fff";
  stock.style.borderRadius = "0px";
  stockdiv.style.display = "none";
  adddiv.style.display = "none";
  dashdiv.style.display = "block";
}

function chosehistory() {
  history.style.backgroundColor = "#79d679";
  history.style.borderRadius = "20px";
  stock.style.backgroundColor= "#fff";
  stock.style.borderRadius = "0px";
  add.style.backgroundColor = "#fff";
  add.style.borderRadius = "0px";
  dashboard.style.backgroundColor= "#fff";
  dashboard.style.borderRadius = "0px";
  stockdiv.style.display= "none";
  adddiv.style.display= "none";
  dashdiv.style.display= "none";
  historydiv.style.display= "block";
  localHistory();
}

function localHistory() {
  historylist.innerHTML = "Loading...";
  fetch("/api/stock-movements/")
    .then((response) => response.json())
    .then((data) => {
      historycount.textContent = "Count: " + data.count;
      if (data.results.length === 0) {
        historylist.innerHTML = "<p style='text-align:center'>Nothing has happened yet</p>";
        return;
      }
      historylist.innerHTML = data.results.map(historyWidget).join("");
    })
    .catch(() => {
      historylist.innerHTML = "<p style='text-align:center'>Could not load History</p>";
    });
}

function historyWidget(movement) {
  const isIn = movement.movement_type === "IN";
  const sign = isIn ? "+" : "";
  const when = new Date(movement.created_at).toLocaleString();
  return `
    <div class="historywidget ${isIn ? "widget-in" : "widget-out"}">
      <div class="widget-type">${isIn ? "Added" : "Removed"}</div>
      <div class="widget-qty">${sign}${movement.quantity} units</div>
      <div class="widget-meta">now ${movement.balance_after} on hand · ${movement.reason.toLowerCase()}</div>
      <div class="widget-when">${when}</div>
    </div>`; 
}