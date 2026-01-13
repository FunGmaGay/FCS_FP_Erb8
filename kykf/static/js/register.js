// This script handles the custom checkbox functionality
        function showThankYouModal(event) {
            event.preventDefault(); // Prevent form submission
            $('#thankYouModal').modal('show'); // Show the modal
            return false; // Prevent default form submission
        }
