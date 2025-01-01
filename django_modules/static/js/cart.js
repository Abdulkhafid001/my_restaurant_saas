console.log("user: ", user);

var cartUpdateBtn = document.getElementsByClassName("update-cart-page");

for (let i = 0; i < cartUpdateBtn.length; i++) {
  cartUpdateBtn[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    showCartAlertMessage(action);
    console.log(productId, action);
    if (user == "AnonymousUser") {
      console.log("authenticate to send data");
    } else {
      updateCartInBackend(productId, action);
    }
  });
}

// document.addEventListener("DOMContentLoaded", () => {
// menu search DOM
// let menuItemCard = document.getElementById("searchMenu");

menuItemCard.addEventListener("click", function (event) {
  if (event.target.closest(".update-cart")) {
    const button = event.target.closest(".update-cart");
    const productId = button.getAttribute("data-product");
    const action = button.getAttribute("data-action");

    console.log(`Product ID: ${productId}, Action: ${action}`);
    updateCartInBackend(productId, action);
  }
});
// });

function updateCartInBackend(productId, action) {
  console.log("fetch called!");

  const url = "/cart/update_cart/";

  const data = { productId: productId, action: action };

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Response from server: ", data);
      document.getElementById("cartItems").innerHTML = data.cartItems;
      document.getElementById("quantity").innerHTML = data.quantity;
      document.getElementById("total").innerHTML = data.total;
    })
    // .then(location.reload())
    .catch((error) => {
      console.error("Error", error);
    });
}

function updateCartInSession() {}

function updateCartFrontend() {}

function showCartAlertMessage(action) {
  var alertMessage = document.getElementById("show");
  alertMessage.style.display = "block";

  var join = action == "add" ? "to" : "from";
  alertMessage.innerHTML = "you " + action + " " + join + " cart";

  var closeButton = document.createElement("button");
  closeButton.innerText = "Close";
  closeButton.style.marginLeft = "10px";
  closeButton.style.padding = "5px";

  closeButton.addEventListener("click", function () {
    alertMessage.style.display = "none";
  });

  if (!document.getElementById("closeBtn")) {
    closeButton.setAttribute("id", "closeBtn");
    alertMessage.appendChild(closeButton);
  }
}

function turnOnSession() {}
