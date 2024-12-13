// Get stripe keys
var stripePublicKey = document
    .getElementById("id_stripe_public_key")
    .textContent.slice(1,-1);
var clientSecret = document
    .getElementById("id_client_secret")
    .textContent.slice(1,-1);

// Set up stripe
var Stripe = new Stripe(stripePublicKey);

// Set the form to a variable
var form = document.getElementById("payment-form");

// Set up an opacity variable
var opacity = 0;

// Define a save info variables
var saveInfo = false;
var csrfToken;
var postData;


// Create instances of stripe elements
var elements = Stripe.elements();
// Create a stripe card element
var card = elements.create("card");
// Add this element to our card-element div
card.mount("#card-element");

// Handle real-time validation errors on the card element
card.addEventListener("change", function(event) {
    // Set my error div to a variable using id
    var errorDiv = document.getElementById("card-errors");
    // If there is an error
    if (event.error) {
        // Set the internal html to:
        errorDiv.innerHTML = `
            <div>
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            </div>
        `;
    // Otherwise make the error div empty
    } else {
        errorDiv.textContent = "";
    }
});

// Handle form submit
// Add an event listener for when the form is submitted
form.addEventListener("submit", function(ev) {
    // Define the payment form and loading overlay
    var paymentForm = document.getElementById("payment-form");
    var loadingOverlay = document.
    getElementById("loading-overlay");
    // Define the info from the cache checkout data view
    var room_id;
    var room;
    var total_days;
    var check_in_date;
    var check_out_date;
    var adults;
    var children;
    var infants;
    var total_cost;
    var url;
    // Prevent the default form action
    ev.preventDefault();
    // Disable the card element and submit button
    // to prevent multiple submissions
    card.update({ "disabled": true});
    document.getElementById("checkout-form-submit-button").disabled = true;
    document.getElementById("payment-form");
    // Fade out the payment form
    if (paymentForm.style.display === "none" ||
        paymentForm.style.display === "") {
        paymentForm.style.display = "block";
        paymentForm.style.opacity = 0;
        opacity = 0;
        const fadeIn = setInterval(function () {
            opacity += 0.1;
            paymentForm.style.opacity = opacity;
            if (opacity >= 1) {
                clearInterval(fadeIn);
            }
        }, 10);
    } else {
        opacity = 1;
        const fadeOut = setInterval(function () {
            opacity -= 0.1;
            paymentForm.style.opacity = opacity;
            if (opacity <= 0) {
                paymentForm.style.display = "none";
                clearInterval(fadeOut);
            }
        }, 10);
    }
    // Fade out loading overlay
    if (loadingOverlay.style.display === "none" ||
        loadingOverlay.style.display === "") {
        loadingOverlay.style.display = "block";
        loadingOverlay.style.opacity = 0;
        opacity = 0;
        const fadeInOverlay = setInterval(function () {
            opacity += 0.1;
            paymentForm.style.opacity = opacity;
            if (opacity >= 1) {
                clearInterval(fadeInOverlay);
            }
        }, 10);
    } else {
        opacity = 1;
        const fadeOutOverlay = setInterval(function () {
            opacity -= 0.1;
            paymentForm.style.opacity = opacity;
            if (opacity <= 0) {
                paymentForm.style.display = "none";
                clearInterval(fadeOutOverlay);
            }
        }, 10);
    }

    // Getting form post information for the cache_checkout_data view
    saveInfo = Boolean(document.getElementById("id-save-info").checked);
    room_id = document.querySelector("input[name='room_id']").value;
    room = document.querySelector("input[name='room']").value;
    total_days = document.querySelector("input[name='total_days']").value;
    check_in_date = document.querySelector("input[name='check_in_date']").value;
    check_out_date = document.querySelector(
        "input[name='check_out_date']"
    ).value;
    adults = document.querySelector("input[name='adults']").value;
    children = document.querySelector("input[name='children']").value;
    infants = document.querySelector("input[name='infants']").value;
    total_cost = document.querySelector("input[name='total_cost']").value;
    csrfToken = document
        .querySelector("input[name='csrfmiddlewaretoken']")
        .value;
    postData = {
        "client_secret": clientSecret,
        "csrfmiddlewaretoken": csrfToken,
        "save_info": saveInfo,
        "room_id": room_id,
        "room": room,
        "total_days": total_days,
        "check_in_date": check_in_date,
        "check_out_date": check_out_date,
        "adults": adults,
        "children": children,
        "infants": infants,
        "total_cost": total_cost
    };
    url = "/checkout/cache_checkout_data/";

    $.post(url, postData).done(function() {
        // Send card information securely to stripe
        // Call confirm payment method
        // Set some values in the payment intent object
        // See full object here:
        // https://docs.stripe.com/api/payment_intents/object
        Stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    // .trim() used to remove whitespace
                    name: form.full_name.value.trim(),
                    phone: form.phone_number.value.trim(),
                    email: form.email.value.trim(),
                    address: {
                        line1: form.street_address1.value.trim(),
                        line2: form.street_address2.value.trim(),
                        city: form.town_or_city.value.trim(),
                        country: form.country.value.trim(),
                        state: form.county.value.trim()
                    }
                }
            },
            // In case customes have different billing and shipping addresses
            shipping: {
                name: form.full_name.value.trim(),
                phone: form.phone_number.value.trim(),
                address: {
                    line1: form.street_address1.value.trim(),
                    line2: form.street_address2.value.trim(),
                    city: form.town_or_city.value.trim(),
                    country: form.country.value.trim(),
                    postal_code: form.postcode.value.trim(),
                    state: form.county.value.trim()
                }
            }
        // Then execute this function on result
        }).then(function(result) {
            var errorDiv;
            var html;
            // If there is an error display the error message
            // in the card error div
            if (result.error) {
                // Get the error div, define the inner html and apply it
                errorDiv = document.getElementById("card-errors");
                html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                // Fade out the payment form
                paymentForm = document.getElementById("payment-form");
                if (paymentForm.style.display === "none" ||
                    paymentForm.style.display === "") {
                    paymentForm.style.display = "block";
                    paymentForm.style.opacity = 0;
                    opacity = 0;
                    const fadeInPayment = setInterval(function () {
                        opacity += 0.1;
                        paymentForm.style.opacity = opacity;
                        if (opacity >= 1) {
                            clearInterval(fadeInPayment);
                        }
                    }, 10);
                } else {
                    opacity = 1;
                    const fadeOutPayment = setInterval(function () {
                        opacity -= 0.1;
                        paymentForm.style.opacity = opacity;
                        if (opacity <= 0) {
                            paymentForm.style.display = "none";
                            clearInterval(fadeOutPayment);
                        }
                    }, 10);
                }
                // Fade out loading overlay
                loadingOverlay = document.getElementById("loading-overlay");
                if (loadingOverlay.style.display === "none" ||
                    loadingOverlay.style.display === "") {
                    loadingOverlay.style.display = "block";
                    loadingOverlay.style.opacity = 0;
                    opacity = 0;
                    const fadeInLoading = setInterval(function () {
                        opacity += 0.1;
                        paymentForm.style.opacity = opacity;
                        if (opacity >= 1) {
                            clearInterval(fadeInLoading);
                        }
                    }, 10);
                } else {
                    opacity = 1;
                    const fadeOutLoading = setInterval(function () {
                        opacity -= 0.1;
                        paymentForm.style.opacity = opacity;
                        if (opacity <= 0) {
                            paymentForm.style.display = "none";
                            clearInterval(fadeOutLoading);
                        }
                    }, 10);
                }

                // If there is an error enable card and submit button to fix it
                card.update({ "disabled": false});
                $("#submit-button").attr("disabled", false);
            } else {
                // If payment intent is succsessful, submit the form
                if (result.paymentIntent.status === "succeeded") {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        // Reload the page, the error will be in django messages
        location.reload();
    });
});