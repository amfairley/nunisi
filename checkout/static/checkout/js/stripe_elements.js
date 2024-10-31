/* Get stripe keys */
var stripe_public_key = document.getElementById('id_stripe_public_key').textContent.slice(1,-1);
var client_secret = document.getElementById('id_client_secret').textContent.slice(1,-1);

/* Set up stripe */
var Stripe = Stripe(stripe_public_key);

/* Create instances of stripe elements */
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