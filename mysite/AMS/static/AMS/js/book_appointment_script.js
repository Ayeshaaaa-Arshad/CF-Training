document.addEventListener('DOMContentLoaded', async function () {
    try {
        // Fetch top doctor details
        const response = await fetch('http://localhost:3000/doctors');
        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.statusText);
        }
        const doctors = await response.json();
        const topDoctor = doctors[0];

        // Update doctor info section dynamically
        const doctorInfo = document.getElementById('doctor-info');
        doctorInfo.innerHTML = `
            <img class="doctor-img" src="${topDoctor.image}" alt="Doctor Picture">
            <h2>${topDoctor.name}</h2>
            <p>${topDoctor.designation}</p>
            <h3>Price: $${topDoctor.price}</h3>
            <label for="appointment-date">Select Appointment Date:</label>
            <input type="date" id="appointment-date" name="appointment-date">
            <button id="book-appointment-btn" class="btn" onclick="booked()">Book Appointment</button>
        `;

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

    } catch (error) {
        console.error('Error fetching data:', error);
    }
});

function booked() {
    const popup = document.getElementById('popup');
    popup.classList.add('show');
    const btn = document.getElementById('book-appointment-btn');
    btn.innerText = 'Already Booked';
    btn.disabled = true;
}

function closePopup() {
    const popup = document.getElementById('popup');
    popup.classList.remove('show');
}
