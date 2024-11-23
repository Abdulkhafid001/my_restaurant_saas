
function getCartData() {
  var cartUpdateBtn = document.getElementsByClassName("update-cart");
  for (let i = 0; i < cartUpdateBtn[i].length; i++) {
    cartUpdateBtn[i].addEventListener("click", function () {
      var productId = this.dataset.product;
      var action = this.dataset.action;
      console.log(
        "productId: ",
        productId,
        " action: ",
        action,
        "should be added to cart."
      );
    });
  }
}

getCartData();
