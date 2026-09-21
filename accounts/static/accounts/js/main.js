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
const history = document.getElementById("history");
const historydiv = document.getElementById("histroydiv");
const historylist = document.getElementById("historylist");
const historycount = document.getElementById("historycount");
const proadd = document.getElementById("proadd");
const pardrop = document.getElementById("Parent");
const newcatform = document.getElementById("newcatform");
const productaddform = document.getElementById("newproform");
const proname = document.getElementById("proname");
const prodes = document.getElementById("prodes");
const probrand = document.getElementById("probrand");
const dropparnet = document.getElementById("dropparnet");
async function enter(event) {
  event.preventDefault();

  const name = catname.value.trim();
  const description = catdes.value.trim();
  const parent = pardrop.value;

  const data = {
    name: name,
    description: description,
    parent: parent || null,
  };

  console.log("Sending:", data);

  try {
    const response = await fetch("/api/categories/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify(data),
    });

    const result = await response.json();

    console.log("API response:", result);

    if (!response.ok) {
      console.error("API error:", result);
      alert("Failed to create category");
      return;
    }

    console.log("Category created:", result);

    // Clear form
    catname.value = "";
    catdes.value = "";
    pardrop.value = "";

    // Close form
    back();

    // Refresh category dropdown
    await loadcat();

    alert("Category created successfully!");
  } catch (error) {
    console.error("Error:", error);
    alert("Something went wrong");
  }
}
function getCookie(name) {
  let cookieValue = null;

  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");

    for (let cookie of cookies) {
      cookie = cookie.trim();

      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }

  return cookieValue;
}

function back() {
  productaddform.style.display = "none;";
  theadd.style.display = "none";
  catadd.style.display = "block";
  proadd.style.display = "block";
}
async function loadcat() {
  try {
    const response = await fetch("/api/categories/");
    if (!response.ok) {
      throw new Error("Failed");
    }
    const data = await response.json();
    pardrop.innerHTML = "";
    const defaultele = document.createElement("option");
    defaultele.value = "";
    defaultele.textContent = "------";
    pardrop.appendChild(defaultele);
    data.results.forEach((category) => {
      const option = document.createElement("option");
      option.value = category.id;
      option.textContent = category.name;
      pardrop.appendChild(option);
    });
  } catch (error) {
    console.log("an error occured", error);
  }
}
async function loadpro() {
  try {
    const response = await fetch("/api/products/");
    if (!response.ok) {
      throw new Error("Failed");
    }
    const data = await response.json();
    pardrop.innerHTML = "";
    const defaultele = document.createElement("option");
    defaultele.value = "";
    defaultele.textContent = "------";
    pardrop.appendChild(defaultele);
    data.results.forEach((category) => {
      const option = document.createElement("option");
      option.value = category.id;
      option.textContent = category.name;
      pardrop.appendChild(option);
    });
  } catch (error) {
    console.log("an error occured", error);
  }
}
document.addEventListener("DOMContentLoaded", loadcat);
function newcategory() {
  catadd.style.display = "none";
  theadd.style.display = "block";
  proadd.style.display = "none";
  loadcat();
}
function newproduct() {
  catadd.style.display = "none";
  theadd.style.display = "none";
  proadd.style.display = "none";
  productaddform.style.display = "block";
}
newcatform.addEventListener("submit", enter);
function chosestock() {
  stock.style.backgroundColor = "#78cc78";
  stock.style.borderRadius = "20px";
  add.style.backgroundColor = "#fff";
  add.style.borderRadius = "0px";
  dashboard.style.backgroundColor = "#fff";
  dashboard.style.borderRadius = "0px";
  history.style.backgroundColor = "#fff";
  history.style.borderRadius = "0px";
  stockdiv.style.display = "block";
  adddiv.style.display = "none";
  dashdiv.style.display = "none";
  historydiv.style.display = "none";
}
function choseadd() {
  add.style.backgroundColor = "#78cc78";
  add.style.borderRadius = "20px";
  stock.style.backgroundColor = "#fff";
  history.style.backgroundColor = "#fff";
  history.style.borderRadius = "0px";
  stock.style.borderRadius = "0px";
  dashboard.style.backgroundColor = "#fff";
  dashboard.style.borderRadius = "0px";
  stockdiv.style.display = "none";
  adddiv.style.display = "block";
  dashdiv.style.display = "none";
  historydiv.style.display = "none";
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
  history.style.backgroundColor = "#fff";
  history.style.borderRadius = "0px";
}

function chosehistory() {
  history.style.backgroundColor = "#79d679";
  history.style.borderRadius = "20px";
  stock.style.backgroundColor = "#fff";
  stock.style.borderRadius = "0px";
  add.style.backgroundColor = "#fff";
  add.style.borderRadius = "0px";
  dashboard.style.backgroundColor = "#fff";
  dashboard.style.borderRadius = "0px";
  stockdiv.style.display = "none";
  adddiv.style.display = "none";
  dashdiv.style.display = "none";
  historydiv.style.display = "block";
  localHistory();
}

function localHistory() {
  historylist.innerHTML = "Loading...";
  fetch("/api/stock-movements/")
    .then((response) => response.json())
    .then((data) => {
      historycount.textContent = "Count: " + data.count;
      if (data.results.length === 0) {
        historylist.innerHTML =
          "<p style='text-align:center'>Nothing has happened yet</p>";
        return;
      }
      const sorted = data.results
        .slice()
        .sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
      historylist.innerHTML = sorted.map(historyWidget).join("");
    })
    .catch(() => {
      historylist.innerHTML =
        "<p style='text-align:center'>Could not load History</p>";
    });
}

function historyWidget(movement) {
  const isIn = movement.movement_type === "IN";
  const sign = isIn ? "+" : "";
  const when = new Date(movement.created_at).toLocaleString();
  return `
    <div class="historywidget ${isIn ? "widget-in" : "widget-out"}">
      <div class="widget-type">${isIn ? "Added" : "Removed"} - ${movement.product_name}</div>
      <div class="widget-qty">${sign}${movement.quantity} units</div>
      <div class="widget-meta">balance now: ${movement.balance_after} · ${movement.reason.toLowerCase()}</div>
      <div class="widget-when">${when}</div>
    </div>`;
}
