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
