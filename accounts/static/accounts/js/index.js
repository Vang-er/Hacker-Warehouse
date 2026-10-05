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

const loginForm = document.getElementById("loginForm");
const errorMsg = document.getElementById("error_msg");

loginForm.addEventListener("submit", async function (event) {
  event.preventDefault(); // Stop normal HTML form reload

  errorMsg.style.display = "none";

  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value;

  try {
    // Call the DRF endpoint
    const response = await fetch("/api/auth/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify({ username, password }),
    });
    const text = await response.text();
    console.log(response.status, response.headers.get("content-type"), text);
    const data = await response.json();

    if (!response.ok) {
      errorMsg.textContent = data.detail || "Login failed.";
      errorMsg.style.display = "block";
      return;
    }

    // Store JWT tokens for frontend use
    localStorage.setItem("access_token", data.access);
    localStorage.setItem("refresh_token", data.refresh);

    // Redirect to the dashboard
    window.location.href = "/dashboard/";
  } catch (error) {
    console.log(error);
    errorMsg.textContent = "Cannot connect to server.";
    errorMsg.style.display = "block";
  }
});
