document.addEventListener('DOMContentLoaded', function() {
    // Get the date input field and time select element
    const dateInput = document.querySelector('input[name="date"]');
    const timeSelect = document.querySelector('select[name="time"]');

    // Function to disable unavailable time slots
    function disableUnavailableTimeSlots() {
        const selectedDate = dateInput.value;
        
        // If no date is selected, do nothing
        if (!selectedDate) return;

        // AJAX request to check booked time slots for the selected date
        fetch(`/check-booked-times/?date=${selectedDate}`)
            .then(response => response.json())
            .then(data => {
                // Enable all time slots first
                Array.from(timeSelect.options).forEach(option => {
                    option.disabled = false;
                    option.style.color = '';
                });

                // Disable booked time slots
                data.booked_times.forEach(time => {
                    Array.from(timeSelect.options).forEach(option => {
                        if (option.value === time) {
                            option.disabled = true;
                            option.style.color = 'gray'; // Gray out the option
                        }
                    });
                });
            })
            .catch(error => {
                console.error('Error fetching booked times:', error);
            });
    }

    // Add event listener to date input
    dateInput.addEventListener('change', disableUnavailableTimeSlots);

    // Check availability on page load if date is already selected
    if (dateInput.value) {
        disableUnavailableTimeSlots();
    }
});