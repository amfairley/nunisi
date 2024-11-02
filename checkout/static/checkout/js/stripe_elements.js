// Get stripe keys
var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1,-1);
var clientSecret = document.getElementById('id_client_secret').textContent.slice(1,-1);

// Set up stripe
var Stripe = Stripe(stripePublicKey);

// Create instances of stripe elements
var elements = Stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card');
card.mount('#card-element', {style: style});

// Handle real-time validation errors on the card element
card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        errorDiv.innerHTML = `
            <div>
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            </div>
        `;
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

// Get form element
form.addEventListener('submit', function(ev) {
    // Prevent the default form action
    ev.preventDefault();
    // Disable the card element and submit button to prevent multiple submissions
        card.update({ 'disabled': true});
        document.getElementById('checkout-form-submit-button').disabled = true;
 
    // Send card information securely to stripe
    // Call confirm payment method
    Stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    // Then execute this function on result
    }).then(function(result) {
        // If there is an error, display the error message in the card error div
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
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
});
