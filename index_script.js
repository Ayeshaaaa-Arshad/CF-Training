let slideIndex = 0;
showSlides();

function showSlides() {
    let slides = document.getElementsByClassName("slides")[0];
    let dots = document.getElementsByClassName("dot");
    slides.style.transform = `translateX(-${slideIndex * 100}%)`;
    for (let i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    dots[slideIndex].className += " active";
}

function changeSlide(n) {
    let slides = document.getElementsByClassName("slides")[0].children.length;
    slideIndex = (slideIndex + n + slides) % slides;
    showSlides();
}

function currentSlide(n) {
    slideIndex = n - 1;
    showSlides();
}

function redirectToBooking() {
    window.location.href = "book_appointment.html";
}

function confirmCancel() {
    var modal = document.getElementById("myModal");
    modal.style.display = "block";
}

function closeModal() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
}

function cancelAppointment() {
    closeModal();
    alert("Appointment canceled successfully.");
}

//fetching data
fetch('http://localhost:3000/doctors')
.then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
})
.then(data => {
    const container = document.getElementById('doctor-info-container');

    if (!data || !Array.isArray(data)) {
        throw new Error('Invalid data format received');
    }

    data.forEach(doctor => {
        const card = document.createElement('div');
        card.classList.add('doctor-card');

        card.innerHTML = `
            <div>
                <img class="doctor-img" src="${doctor.image}" alt="Doctor Picture">
            </div>
            <div class="doctor-info">
                <table class="info-table">
                    <tr>
                        <td>Name:</td>
                        <td>${doctor.name}</td>
                    </tr>
                    <tr>
                        <td>Email:</td>
                        <td>${doctor.email}</td>
                    </tr>
                    <tr>
                        <td>Designation:</td>
                        <td>${doctor.designation}</td>
                    </tr>
                </table>
                <div class="buttons">
                    <button class="btn-2" onclick="confirmCancel()">Cancel Appointment</button>
                    <button class="btn" onclick="redirectToBooking()">Book Appointment</button>
                </div>
            </div>
        `;

        container.appendChild(card);
    });
})
.catch(error => {
    console.error('Error fetching doctors:', error);
});
