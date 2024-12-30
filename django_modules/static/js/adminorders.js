// this file contains code for the admin orders page
let orderStatusField = document.getElementById("orderStatus");
let orderDateField = document.getElementById("orderDate");

orderStatusField.addEventListener("input", (event) => {
  sendOrderDetailsToBackend();
});

orderDateField.addEventListener("input", (event) => {
  sendOrderDetailsToBackend();
});

function getCSRFToken(params) {
  var cookieValue = "";
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function getOrderDetails() {
  const orderStatus = document.getElementById("orderStatus").value;
  const orderDate = document.getElementById("orderDate").value;
  const OrderData = {
    orderStatus: orderStatus,
    orderDate: orderDate,
  };
  return OrderData;
}

let csrftoken = "PIxfGivh6dxqUvxh1aZx6rgyu2sa3kEA";

function sendOrderDetailsToBackend() {
  const url = "/naijakitchen/admin/getorder/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(getOrderDetails()),
  })
    .then((response) => response.json())
    .then((data) => {
      // this where I can use json to render orders or other I get from my backend.
      //   console.log("response from server", data);
    })
    .catch((error) => {
      console.log("Error from Order function", error);
    });
}
