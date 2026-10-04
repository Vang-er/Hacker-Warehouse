addvariants.addEventListener("click", () => {
  catpresser = false;
  stockpressed = false;
  varpressed = true;
  propressed = false;
  addvariants.style.backgroundColor = "#4B5563";
  addstock.style.backgroundColor = "#6B7280";
  addcat.style.backgroundColor = "#6B7280";
  addpro.style.backgroundColor = "#6B7280";
  cat.style.display = "none";
  stock.style.display = "none";
  productform.style.display = "none";
  variantform.style.display = "flex";
});
addpro.addEventListener("click", () => {
  stockpressed = false;
  catpresser = false;
  varpressed = false;
  propressed = true;
  addpro.style.backgroundColor = "#4B5563";
  addcat.style.backgroundColor = "#6B7280";
  addstock.style.backgroundColor = "#6B7280";
  addvariants.style.backgroundColor = "#6B7280";
  cat.style.display = "none";
  stock.style.display = "none";
  productform.style.display = "flex";
  variantform.style.display = "none";
});
addcat.addEventListener("click", () => {
  catpresser = true;
  stockpressed = false;
  varpressed = false;
  propressed = false;
  addcat.style.backgroundColor = "#4B5563";
  addstock.style.backgroundColor = "#6B7280";
  addpro.style.backgroundColor = "#6B7280";
  addvariants.style.backgroundColor = "#6B7280";
  cat.style.display = "flex";
  stock.style.display = "none";
  productform.style.display = "none";
  variantform.style.display = "none";
});
addstock.addEventListener("click", () => {
  stockpressed = true;
  catpresser = false;
  varpressed = false;
  propressed = false;
  addstock.style.backgroundColor = "#4B5563";
  addcat.style.backgroundColor = "#6B7280";
  addpro.style.backgroundColor = "#6B7280";
  addvariants.style.backgroundColor = "#6B7280";
  cat.style.display = "none";
  stock.style.display = "flex";
  productform.style.display = "none";
  variantform.style.display = "none";
});
addcat.style.backgroundColor = "#4B5563";
addstock.style.backgroundColor = "#6B7280";
addstock.addEventListener("click", () => {
  stockpressed = true;
  catpresser = false;
  addstock.style.backgroundColor = "#4B5563";
  addcat.style.backgroundColor = "#6B7280";
});
window.addEventListener("resize", checkSearch);
addcat.addEventListener("click", () => {
  catpresser = true;
  stockpressed = false;

  addcat.style.backgroundColor = "#4B5563";
  addstock.style.backgroundColor = "#6B7280";
});

addstock.addEventListener("click", () => {
  stockpressed = true;
  catpresser = false;

  addstock.style.backgroundColor = "#4B5563";
  addcat.style.backgroundColor = "#6B7280";
});
cat.addEventListener("submit", async (event) => {
  event.preventDefault();
  const name = document.getElementById("catname").value;
  const description = document.getElementById("catdes").value;
  const parent = document.getElementById("catslect").value;
  const response = await fetch("/api/categories/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      name: name,
      description: description,
      parent: parent === "" ? null : Number(parent),
    }),
  });
  const data = await response.json();
  if (response.ok) {
    window.alert(`added category ${name}`);
  } else {
    window.alert("an error occured");
  }
  document.getElementById("catname").value = "";
  document.getElementById("catdes").value = "";
  window.location.reload();
});
pro.addEventListener("submit", async (event) => {
  event.preventDefault();
  const name = document.getElementById("proname").value;
  const description = document.getElementById("prodes").value;
  const brand = document.getElementById("probrand").value;
  const cat = document.getElementById("proslect").value;
  const response = await fetch("/api/products/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      name: name,
      description: description,
      category: cat,
      brand: brand,
      is_active: true,
    }),
  });
  const data = await response.json();



  if (response.ok) {
    showdivsucks()
  } else {
    showdivdecli()
  }



  document.getElementById("proname").value = "";
  document.getElementById("prodes").value = "";
  document.getElementById("probrand").value = "";
  window.location.reload();
 });
// variantform.addEventListener("submit", async (event) => {
//     event.preventDefault();
//     const name = document.getElementById("varname").value;
//     const product = document.getElementById("varslect").value;
//     const price = document.getElementById("varprice").value;
//     const cost = document.getElementById("varcost").value;
//     const response = await fetch("/api/")
// })
