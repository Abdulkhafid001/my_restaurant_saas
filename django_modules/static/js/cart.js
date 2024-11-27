console.log("user: ", user);

var cartUpdateBtn = document.getElementsByClassName("update-cart");

for (let i = 0; i < cartUpdateBtn.length; i++) {
  cartUpdateBtn[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log(productId, action);
    if (user == "AnonymousUser") {
      console.log("authenticate to send data");
    } else {
      updateCartInBackend(productId, action);
    }
    showCartAlertMessage(action);
  });
}

function updateCartInBackend(productId, action) {
  // functionality to send data to django without reload.
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
      // Optionally update the cart UI here
    })
    // .then(location.reload())
    .catch((error) => {
      console.error("Error", error);
    });
}

function updateCartInSession(params) {}

function updateCartFrontend(params) {}

function showCartAlertMessage(action) {
  var alertMessage = document.getElementById("show");
  alertMessage.style.display = "block"; // Display the message

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
    closeButton.setAttribute("id", "closeBtn"); // Add an id to the button
    alertMessage.appendChild(closeButton);
  }
}
