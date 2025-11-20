/**
 * Gets the number of adults, children, and infants and calculates
 * total guests, displaying it on the screen.
 * Works for both the navigation bar search form and index page form
 */
function updateGuestCount() {
    // Get values from the form in real time (0 if no value) for both forms
    const adultsTopNav = parseInt(
        document.querySelector("#top-nav #id_desktop-adults").value
    ) || 0;
    const adultsIndexBookingForm = parseInt(
        document.querySelector("#index-booking-form #id_mobile-adults")?.value
    ) || 0;
    const childrenTopNav = parseInt(
        document.querySelector("#top-nav #id_desktop-children").value) || 0;
    const childrenIndexBookingForm = parseInt(
        document.querySelector("#index-booking-form #id_mobile-children")?.value
    ) || 0;
    const infantsTopNav = parseInt(
        document.querySelector("#top-nav #id_desktop-infants").value
    ) || 0;
    const infantsIndexBookingForm = parseInt(
        document.querySelector("#index-booking-form #id_mobile-infants")?.value
    ) || 0;
    // Update total guests for both forms
    const totalGuestsTop = (
        adultsTopNav +
        childrenTopNav +
        infantsTopNav
    );
    const totalGuestsIndex = (
        adultsIndexBookingForm +
        childrenIndexBookingForm +
        infantsIndexBookingForm
    );
    const totalGuestsTopNav = document.querySelector(
        "#top-nav #desktop-total-guests"
    );
    if (totalGuestsTopNav) {
        totalGuestsTopNav.innerText = `${totalGuestsTop}`;
    }
    const totalGuestsIndexForm = document.querySelector(
        "#index-booking-form #mobile-total-guests"
    );
    if (totalGuestsIndexForm) {
        totalGuestsIndexForm.innerText = `${totalGuestsIndex}`;
    }
}

/**
 * Allows the user to open the calendar widgets by clicking anywhere
 * inside the check in/out date input areas.
 */
document.addEventListener("DOMContentLoaded", function () {
    // Get the checkin/out inputs for both forms
    const checkInInputTop = document.querySelector(
        "#top-nav #id_desktop-check_in_date"
    );
    const checkOutInputTop = document.querySelector(
        "#top-nav #id_desktop-check_out_date"
    );
    const checkInInputIndex = document.querySelector(
        "#index-booking-form #id_mobile-check_in_date"
    ) || null;
    const checkOutInputIndex = document.querySelector(
        "#index-booking-form #id_mobile-check_out_date"
    ) || null;
    // Add event listener to navbar check in date
    checkInInputTop.addEventListener("click", function () {
        this.showPicker();
    });
    // Add event listener to navbar check out date
    checkOutInputTop.addEventListener("click", function () {
        this.showPicker();
    });
    // Add event listener to homepage check in date
    if (checkInInputIndex) {
        checkInInputIndex.addEventListener("click", function () {
            this.showPicker();
        });
    }
    // Add event listener to homepage check out date
    if (checkOutInputIndex) {
        checkOutInputIndex.addEventListener("click", function () {
            this.showPicker();
        });
    }
});