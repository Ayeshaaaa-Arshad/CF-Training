let slideIndex = 0;

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


setInterval(() => {
    changeSlide(1);
}, 4000);

//....................


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
let currentPage = 1; 
const cardsPerPage = 2; // Number of cards per page

// Function to display doctors based on current page
function displayDoctors(page) {
    const container = document.getElementById('doctor-info-container');
    container.innerHTML = ''; // Clear existing content

    // Calculate start and end indices based on current page
    const startIndex = (page - 1) * cardsPerPage;
    const endIndex = startIndex + cardsPerPage;

    fetch('http://localhost:3000/doctors')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (!data || !Array.isArray(data)) {
                throw new Error('Invalid data format received');
            }

            // Slice data based on calculated indices
            const doctorsToShow = data.slice(startIndex, endIndex);

            doctorsToShow.forEach(doctor => {
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
                            <button class="btn" onclick="redirectToBooking()">Book Appointment</button>
                        <button class="btn-2" onclick="confirmCancel()">Cancel Appointment</button>
                            
                            </div>
                    </div>
                `;

                container.appendChild(card);
            });

            // Update pagination buttons
            updatePaginationButtons(data.length);
        })
        .catch(error => {
            console.error('Error fetching doctors:', error);
        });
}

// Function to update pagination buttons based on total number of items
function updatePaginationButtons(totalItems) {
    const totalPages = Math.ceil(totalItems / cardsPerPage);
    const pageNumbersContainer = document.getElementById('page-numbers');
    pageNumbersContainer.innerHTML = ''; // Clear existing buttons

    for (let i = 1; i <= totalPages; i++) {
        const pageNumberButton = document.createElement('button');
        pageNumberButton.textContent = i;
        pageNumberButton.onclick = function () {
            currentPage = i;
            displayDoctors(currentPage);
        };
        if (i === currentPage) {
            pageNumberButton.classList.add('active');
        }
        pageNumbersContainer.appendChild(pageNumberButton);
    }

    // Enable/disable previous and next buttons based on current page
    document.getElementById('btn-prev').disabled = currentPage === 1;
    document.getElementById('btn-next').disabled = currentPage === totalPages;
}

// Function to go to previous page
function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        displayDoctors(currentPage);
    }
}

// Function to go to next page
function nextPage() {
    currentPage++;
    displayDoctors(currentPage);
}

// Initial display of doctors on page load
displayDoctors(currentPage);


let currentAnnouncementIndex = 0;
let announcements = [];
let prevTreatments = [];

function showAnnouncements() {
    const announcementContainer = document.querySelector('.announcement-container');
    announcementContainer.innerHTML = '';

    announcements.forEach((announcement, index) => {
        const card = document.createElement('div');
        card.classList.add('announcement-card');

        card.innerHTML = `
            <h3>${announcement.title}</h3>
            <p>${announcement.content}</p>
        `;

        announcementContainer.appendChild(card);
    });

    showCurrentAnnouncement();
}

function showCurrentAnnouncement() {
    const cards = document.querySelectorAll('.announcement-card');
    cards.forEach((card, index) => {
        if (index === currentAnnouncementIndex) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

function changeAnnouncement(n) {
    currentAnnouncementIndex += n;
    if (currentAnnouncementIndex < 0) {
        currentAnnouncementIndex = announcements.length - 1;
    }
    if (currentAnnouncementIndex >= announcements.length) {
        currentAnnouncementIndex = 0;
    }
    showCurrentAnnouncement();
}

setInterval(() => {
    changeAnnouncement(1);
}, 5000);


function fetchData() {
    const url = 'http://localhost:3000';
    Promise.all([
        fetch(`${url}/announcements`),
        fetch(`${url}/prev_treatments`)
    ])
        .then(responses => Promise.all(responses.map(response => response.json())))
        .then(data => {
            announcements = data[0];
            prevTreatments = data[1];

            showAnnouncements();
            showRecentTreatment();
        })
        .catch(error => console.error('Error fetching data:', error));
}

function showRecentTreatment() {
    const prevTreatmentsList = document.getElementById('prevTreatmentsList');
    prevTreatmentsList.innerHTML = '';

    for (let i = 0; i < Math.min(2, prevTreatments.length); i++) {
        const treatment = prevTreatments[i];
        const treatmentItem = document.createElement('li');
        treatmentItem.innerHTML = `
            <span>${formatDate(treatment.date)} - ${treatment.treatment} by ${treatment.doctor}</span>
            <p>Result: ${treatment.notes}</p>
            <br>
        `;
        prevTreatmentsList.appendChild(treatmentItem);
    }


    const moreTreatmentsItem = document.createElement('li');
    moreTreatmentsItem.appendChild(moreTreatmentsLink);
    prevTreatmentsList.appendChild(moreTreatmentsItem);
}



function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

document.addEventListener('DOMContentLoaded', fetchData);


//profile image dynamically load from db.json
document.addEventListener("DOMContentLoaded", function() {
    fetch('http://localhost:3000/patients/1')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.json();
        })
        .then(patient => {
            // Update profile image source dynamically
            const profileImg = document.getElementById('profile-img');
            if (profileImg) {
                profileImg.src = 'images/'+patient.profileImage || 'AMS/images/default-profile-img.jpg'; 
                profileImg.alt = patient.firstName + ' ' + patient.lastName; 
            } else {
                console.error('Profile image element not found.');
            }
        })
        .catch(error => {
            console.error('Error fetching patient data:', error);
        });
});
