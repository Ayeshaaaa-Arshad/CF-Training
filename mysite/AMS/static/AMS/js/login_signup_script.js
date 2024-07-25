document.addEventListener("DOMContentLoaded", function() {
    const loginLink = document.getElementById('login-link');
    const signupLink = document.getElementById('signup-link');
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');
    const popup = document.getElementById('popup');
    const popupMessage = document.getElementById('popupMessage');

    loginLink.addEventListener('click', function() {
        showForm('login');
    });

    signupLink.addEventListener('click', function() {
        showForm('signup');
    });

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;
        
        showPopupAndRedirect(`Successfully logged in as ${username}`, 'index.html');
    });

    signupForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('signupUsername').value;
      
        showPopupAndRedirect(`Successfully signed up as ${username}`, 'index.html');
    });

    function showForm(formType) {
        if (formType === 'login') {
            loginForm.style.display = 'block';
            signupForm.style.display = 'none';
            loginLink.classList.add('active');
            signupLink.classList.remove('active');
        } else if (formType === 'signup') {
            loginForm.style.display = 'none';
            signupForm.style.display = 'block';
            loginLink.classList.remove('active');
            signupLink.classList.add('active');
        }
    }

    function showPopupAndRedirect(message, destination) {
        popupMessage.textContent = message;
        popup.style.display = 'block';
        setTimeout(function() {
            closePopup();
            window.location.href = destination;
        }, 2000); 
    }

    function closePopup() {
        popup.style.display = 'none';
    }
});
