document.addEventListener("DOMContentLoaded", function() {
    fetch('http://localhost:3000/patients')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            if (data.length > 0) {
                const patient = data[0]; 

                // Pre-fill form with patient data
                document.getElementById('idNumber').value = patient.idNumber;
                document.getElementById('firstName').value = patient.firstName;
                document.getElementById('lastName').value = patient.lastName;
                document.getElementById('phone').value = patient.phone;
                if (patient.gender === 'female') {
                    document.querySelector('input[name="gender"][value="female"]').checked = true;
                } else if (patient.gender === 'male') {
                    document.querySelector('input[name="gender"][value="male"]').checked = true;
                }

                // Handle form submission to update patient data
                const editForm = document.querySelector('form');
                editForm.addEventListener('submit', function(event) {
                    event.preventDefault();

                    const formData = new FormData(editForm);
                    const updatedPatient = {
                        id: patient.id, 
                        idNumber: formData.get('idNumber'),
                        firstName: formData.get('firstName'),
                        lastName: formData.get('lastName'),
                        phone: formData.get('phone'),
                        gender: formData.get('gender'),
                    };

                    // Check if a profile image was selected
                    const profileImageFile = formData.get('profileImage');
                    if (profileImageFile && profileImageFile.name) {
                        // If a new profile image is selected, include it in the request
                        updatedPatient.profileImage = profileImageFile.name; // Or handle as needed
                    } else {
                        // Use the existing profile image if no new image is selected
                        updatedPatient.profileImage = patient.profileImage;
                    }

                    // Call function to update patient data
                    updatePatientData(updatedPatient);
                });

                // Function to update patient data via PUT request
                function updatePatientData(patientData) {
                    fetch(`http://localhost:3000/patients/${patientData.id}`, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(patientData),
                    })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok: ' + response.statusText);
                        }
                        return response.json();
                    })
                    .then(data => {
                        console.log('Patient data updated:', data);
                        showNotification('Patient data updated successfully!');
                    })
                    .catch(error => {
                        console.error('Error updating patient data:', error);
                        showNotification('Failed to update patient data. Please try again.');
                    });
                }

            } else {
                console.error('No patient data found.');
            }
        })
        .catch(error => {
            console.error('Error fetching patient data:', error);
        });

    // Function to show notification popup
    function showNotification(message, duration = 3000) {
        const notificationPopup = document.getElementById('notification-popup');
        if (!notificationPopup) {
            console.error('Notification popup element not found.');
            return;
        }
        
        const notificationMessage = notificationPopup.querySelector('#notification-message');
        if (!notificationMessage) {
            console.error('Notification message element not found within the popup.');
            return;
        }

        notificationMessage.textContent = message;
        notificationPopup.style.display = 'block';

        setTimeout(() => {
            notificationPopup.style.display = 'none';
        }, duration);
    }
});
