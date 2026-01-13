
        function toggleWorkshopDropdown() {
            const applicationType = document.getElementById('applicationType').value;
            const workshopDropdown = document.getElementById('workshopDropdown');
            const volunteerReason = document.getElementById('volunteerReason');
            workshopDropdown.style.display = applicationType === 'workshop' ? 'block' : 'none';
            volunteerReason.style.display = applicationType === 'volunteer' ? 'block' : 'none';
        }

        function submitForm(event) {
            alert('Thank you for your registration! We will contact you shortly once your application is successful.');
            // Returning true lets the form submit as normal
            return true;
        }
