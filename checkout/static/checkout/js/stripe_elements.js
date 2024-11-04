// Get stripe keys
var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1,-1);
var clientSecret = document.getElementById('id_client_secret').textContent.slice(1,-1);

// Set up stripe
var Stripe = Stripe(stripePublicKey);

// Create instances of stripe elements
var elements = Stripe.elements();
// Create a stripe card element
var card = elements.create('card');
// Add this element to our card-element div
card.mount('#card-element');

// Handle real-time validation errors on the card element
card.addEventListener('change', function(event) {
    // Set my error div to a variable using id
    var errorDiv = document.getElementById('card-errors');
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
        errorDiv.textContent = '';
    }
});

// Handle form submit
// Set the form to a variable
var form = document.getElementById('payment-form');

// Add an event listener for when the form is submitted
form.addEventListener('submit', function(ev) {
    // Prevent the default form action
    ev.preventDefault();
    // Disable the card element and submit button to prevent multiple submissions
    card.update({ 'disabled': true});
    document.getElementById('checkout-form-submit-button').disabled = true;
    document.getElementById('payment-form')
    // Fade out the payment form
    const paymentForm = document.getElementById('payment-form');
    if (paymentForm.style.display === 'none' || paymentForm.style.display === '') {
        paymentForm.style.display = 'block';
        paymentForm.style.opacity = 0;
        let opacity = 0;
        const fadeIn = setInterval(() => {
            opacity += 0.1;
            paymentForm.style.opacity = opacity;
            if (opacity >= 1) {
                clearInterval(fadeIn);
            }
        }, 10);
    } else {
        let opacity = 1;
        const fadeOut = setInterval(() => {
            opacity -= 0.1;
            paymentForm.style.opacity = opacity;
            if (opacity <= 0) {
                paymentForm.style.display = 'none';
                clearInterval(fadeOut);
            }
        }, 10);
    }
    // Fade out loading overlay
    const loadingOverlay = document.getElementById('loading-overlay');
    if (loadingOverlay.style.display === 'none' || loadingOverlay.style.display === '') {
        loadingOverlay.style.display = 'block';
        loadingOverlay.style.opacity = 0;
        let opacity = 0;
        const fadeIn = setInterval(() => {
            opacity += 0.1;
            loadingOverlay.style.opacity = opacity;
            if (opacity >= 1) {
                clearInterval(fadeIn);
            }
        }, 10);
    } else {
        let opacity = 1;
        const fadeOut = setInterval(() => {
            opacity -= 0.1;
            loadingOverlay.style.opacity = opacity;
            if (opacity <= 0) {
                loadingOverlay.style.display = 'none';
                clearInterval(fadeOut);
            }
        }, 10);
    }
    
    // To save information or not
    var saveInfo = Boolean(document.getElementById('id-save-info').checked);
    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    }
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        // Send card information securely to stripe
        // Call confirm payment method
        // Set some values in the payment intent object
        // See full object here: https://docs.stripe.com/api/payment_intents/object
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
            },
        // Then execute this function on result
        }).then(function(result) {
            // If there is an error, display the error message in the card error div
            if (result.error) {
                // Get the error div, define the inner html and apply it
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                // Fade out the payment form
                const paymentForm = document.getElementById('payment-form');
                if (paymentForm.style.display === 'none' || paymentForm.style.display === '') {
                    paymentForm.style.display = 'block';
                    paymentForm.style.opacity = 0;
                    let opacity = 0;
                    const fadeIn = setInterval(() => {
                        opacity += 0.1;
                        paymentForm.style.opacity = opacity;
                        if (opacity >= 1) {
                            clearInterval(fadeIn);
                        }
                    }, 10);
                } else {
                    let opacity = 1;
                    const fadeOut = setInterval(() => {
                        opacity -= 0.1;
                        paymentForm.style.opacity = opacity;
                        if (opacity <= 0) {
                            paymentForm.style.display = 'none';
                            clearInterval(fadeOut);
                        }
                    }, 10);
                }
                // Fade out loading overlay
                const loadingOverlay = document.getElementById('loading-overlay');
                if (loadingOverlay.style.display === 'none' || loadingOverlay.style.display === '') {
                    loadingOverlay.style.display = 'block';
                    loadingOverlay.style.opacity = 0;
                    let opacity = 0;
                    const fadeIn = setInterval(() => {
                        opacity += 0.1;
                        loadingOverlay.style.opacity = opacity;
                        if (opacity >= 1) {
                            clearInterval(fadeIn);
                        }
                    }, 10);
                } else {
                    let opacity = 1;
                    const fadeOut = setInterval(() => {
                        opacity -= 0.1;
                        loadingOverlay.style.opacity = opacity;
                        if (opacity <= 0) {
                            loadingOverlay.style.display = 'none';
                            clearInterval(fadeOut);
                        }
                    }, 10);
                }
            
                // If there is an error enable card and submit button to fix it
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                // If payment intent is succsessful, submit the form
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        // Reload the page, the error will be in django messages
        location.reload()
    });
});
