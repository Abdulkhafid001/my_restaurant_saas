var total = Number("{{order.get_cart_total|floatformat:2}}");

const checkoutForm = document.getElementById("checkoutForm");

document.addEventListener("DOMContentLoaded", (e) => {
  checkoutForm.addEventListener("submit", function (e) {
    e.preventDefault();
    getCheckoutFormData();
    
  });
});

function getCheckoutFormData() {
    console.log('getting form data...');
    
  let userData = {
    name: "",
    phoneNumber: "",
    deliveryAddress: "",
  };

  userData.name = checkoutForm.name.value;
  userData.phoneNumber = checkoutForm.phoneNumber.value;
  userData.deliveryAddress = checkoutForm.deliveryAddress.value;
  console.log(userData);
}
