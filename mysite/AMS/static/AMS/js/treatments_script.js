document.addEventListener('DOMContentLoaded', async function () {
    try {
        // Fetch patient data
        const patientResponse = await fetch('http://localhost:3000/patients/1');
        if (!patientResponse.ok) {
            throw new Error('Network response was not ok: ' + patientResponse.statusText);
        }
        const patient = await patientResponse.json();

        // Update profile image dynamically
        const profileImg = document.getElementById('profile-img');
        if (profileImg) {
            profileImg.src = 'images/' + (patient.profileImage || 'default-profile-img.jpg'); // Set default image if profileImage is not available
            profileImg.alt = patient.firstName + ' ' + patient.lastName; // Set alt text based on patient's name
        } else {
            console.error('Profile image element not found.');
        }

        // Fetch previous treatments data
        const treatmentsResponse = await fetch('http://localhost:3000/prev_treatments');
        if (!treatmentsResponse.ok) {
            throw new Error('Network response was not ok: ' + treatmentsResponse.statusText);
        }
        const treatments = await treatmentsResponse.json();

        // Display treatments in a table
        const tbody = document.getElementById('treatment-table-body');
        treatments.forEach(treatment => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${treatment.date}</td>
                <td>${treatment.treatment}</td>
                <td>${treatment.doctor}</td>
                <td>${treatment.notes}</td>
            `;
            tbody.appendChild(row);
        });

    } catch (error) {
        console.error('Error fetching data:', error);
    }
});
