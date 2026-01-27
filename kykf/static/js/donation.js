function showThankYouModal(event) {
    if (document.getElementById('contribute_fund').value != '') {
        $('#thankYouModal').modal('show');

        if (document.getElementById('receipt').value == 'Y') {
            event.preventDefault();
            let form = $("#donation_form");
            var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();

            $.ajax({
                type: "POST",
                url: $('#hiddenFormAction').val(),
                data: {csrfmiddlewaretoken: $('#csrfmiddlewaretoken').val(), 
                       last_name: $('#last_name').val(), 
                       first_name: $('#first_name').val(), 
                       email: $('#email').val(), 
                       contribute_fund: $('#contribute_fund').val()},
                headers: {
                    'X-CSRFToken': csrf_token // Include CSRF token in headers
                },
                xhrFields: {
                    responseType: 'blob' // Important: set the response type to blob
                },
                success: function(response, status, xhr) {

                },
                error: function (data) {

                }
            });

            document.getElementById("first_name").value = "";
            document.getElementById("last_name").value = "";
            document.getElementById("email").value = "";
            document.getElementById("contribute_fund").value = "";
        }
        else {
            document.getElementById("first_name").value = "";
            document.getElementById("last_name").value = "";
            document.getElementById("email").value = "";
            document.getElementById("contribute_fund").value = "";        
        }
    }
}

