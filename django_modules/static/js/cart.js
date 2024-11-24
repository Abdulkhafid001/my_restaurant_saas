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
  });
}

function updateCartInBackend(productId, action) {
  // functionality to send data to django without reload.
  const url = "/update_cart/";

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
    .catch((error) => {
      console.error("Error", error);
    });
}

function updateCartInSession(params) {}
