const stock = document.getElementById("your");
const add = document.getElementById("add");
const dashboard = document.getElementById("dash");
const addStockBtn = document.getElementById("add-stock")
const historyBtn = document.getElementById("history");
const stockdiv = document.getElementById("stockdiv");
const adddiv = document.getElementById("adddiv");
const dashdiv = document.getElementById("dashdiv");
const historydiv = document.getElementById("historydiv");
const catadd = document.getElementById("catadd"); const hDiv = getHistoryDiv()
const catname = document.getElementById("catname");
const catdes = document.getElementById("catdes");
const theadd = document.getElementById("theadd");
const backbut = document.getElementById("back");
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

const newproductModal = document.getElementById("newproduct");

function getHistoryDiv() {
  let div = document.getElementById("historydiv");
  if (!div) {
    console.warn("historydiv was missing from DOM, creation fallback applied..");
  }
  return div;
}
function getStockDiv() {return document.getElementById("stockdiv"); }
function getAddDiv() {return document.getElementById("adddiv"); }
function getDashDiv() {return document.getElementById("dashdiv"); }

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
    closeSubForms();

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
  productaddform.style.display = "none";
  theadd.style.display = "none";
  catadd.style.display = "block";
  proadd.style.display = "block";
}
async function loadcat() {
  try {
    const response = await fetch("/api/categories/");

    if (!response.ok) {
      throw new Error("Failed to load categories");
    }

    const data = await response.json();

    // Category form's parent dropdown
    pardrop.innerHTML = "";

    // Product form's category dropdown
    dropparnet.innerHTML = "";

    // Default options
    const parentDefault = document.createElement("option");
    parentDefault.value = "";
    parentDefault.textContent = "------";
    pardrop.appendChild(parentDefault);

    const productDefault = document.createElement("option");
    productDefault.value = "";
    productDefault.textContent = "------";
    dropparnet.appendChild(productDefault);

    // Add categories to both dropdowns
    data.results.forEach((category) => {
      // Parent-category dropdown
      const parentOption = document.createElement("option");
      parentOption.value = category.id;
      parentOption.textContent = category.name;
      pardrop.appendChild(parentOption);

      // Product-category dropdown
      const productOption = document.createElement("option");
      productOption.value = category.id;
      productOption.textContent = category.name;
      dropparnet.appendChild(productOption);
    });
  } catch (error) {
    console.error("Error loading categories:", error);
  }
}
document.addEventListener("DOMContentLoaded", loadcat);
function newcategory() {
  catadd.style.display = "none";
  theadd.style.display = "block";
  proadd.style.display = "none";
  loadcat();
}
function openNewProductForm() {
  catadd.style.display = "none";
  theadd.style.display = "none";
  proadd.style.display = "none";
  productaddform.style.display = "block";
  loadcat();
}
newcatform.addEventListener("submit", enter);
function chosestock() {
  hideAllMainViews();
  setActiveTab(stock);
  if (stockdiv) {
    stockdiv.style.display = "block";
    loadStockData();
  }
}

function choseadd() {
  hideAllMainViews();
  setActiveTab(add);
  if (adddiv) adddiv.style.display = "block";
  if (theadd) theadd.style.display = "none";
  if (productaddform) productaddform.style.display = "none";
  if (catadd) catadd.style.display = "block";
  if (proadd) proadd.style.display = "block";
}
function chosedash() {
  hideAllMainViews();
  setActiveTab(dashboard);
  if (dashdiv) dashdiv.style.display = "block";
}

function hideAllMainViews() {
  const divs = [
    document.getElementById("stockdiv"),
    document.getElementById("adddiv"),
    document.getElementById("dashdiv"),
    document.getElementById("historydiv")
  ];
  
  divs.forEach(div => {
    if (div) div.style.display = "none";
  });
}


function resetTabStyles() {
  const tabs = [stock, add, dashboard, addStockBtn, historyBtn];
  tabs.forEach(tab =>{
    if (tab) {
      tab.style.backgroundColor="#fff";
      tab.style.borderRadius = "0px";
    }
  });
}

function setActiveTab(tabElement) {
  resetTabStyles();
  if (tabElement) {
    tabElement.style.backgroundColor = "#78cc78";
    tabElement.style.borderRadius = "20px";
  }
}

function chosehistory() {
  hideAllMainViews();
  const historyBtn = document.getElementById("history");
  if (historyBtn) setActiveTab(historyBtn);

  const hDiv = getHistoryDiv();
  if (hDiv) {
    hDiv.style.display = "block";
    localHistory();
  } else {
    alert("Error: History section could not be found on this page layout.");
  }
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
      <div class="widget-type">${isIn ? "Added" : "Removed"} — ${movement.variant_name}</div>
      <div class="widget-qty">${sign}${movement.quantity} units</div>
      <div class="widget-meta">balance now: ${movement.balance_after} · ${movement.reason.toLowerCase()}</div>
      <div class="widget-when">${when}</div>
    </div>`;
}

function choseadds() {
  hideAllMainViews();
  setActiveTab(addStockBtn);
  if (adddiv) adddiv.style.display = "block";
  openNewProductForm();
}

function x() {
  if (newproductModal) newproductModal.style.display = "none";
}

function done(event) {
  event.preventDefault();
  alert("Product modal submitted!");
  x();
}

async function loadStockData() {
  const stockContent = document.getElementById("stockcontent");
  const emptyMsg = document.getElementById("empyty");

  if (!stockContent) return;

  stockContent.innerHTML = "<p style='text-align:center;'>Loading Inventory...</p>";
  try {
    const response = await fetch("/api/categories/");
    if (!response.ok) throw new Error("Failed to fetch stock data!");
    const data = await response.json();
    const categories = data.results || data;

    if (categories.length === 0) {
      if (emptyMsg) emptyMsg.style.display = "block";
      stockContent.innerHTML = "";
      return;
    }
    if (emptyMsg) emptyMsg.style.display = "none";

    // The Stock cards here !!! <<<<<<<<<<<<<<<<----- 
  } catch (error) {
    console.error("Error loading stock:", error);
    stockContent.innerHTML = "<p style='text-align:center; color: red;'>Could not load stock inventory...</p>"
  }
}