document.addEventListener('DOMContentLoaded', function() {
    const formularioContainer = document.querySelector('.formulario-container');
    const formularioLogin = document.querySelector('.formulariologin');
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const loginLink = document.querySelector('.login-link');
    const registerLink = document.querySelector('.register-link');
    const iconClose = document.querySelector('.icon-close');
    const btnLoginPopup = document.querySelector('.btnlogin-popup');

    // Mostrar formulario al hacer clic en Login del navbar
    btnLoginPopup.addEventListener('click', () => {
        formularioContainer.classList.add('active');
    });

    // Cambiar a formulario de registro
    registerLink.addEventListener('click', (e) => {
        e.preventDefault();
        loginForm.style.transform = 'translateX(-100%)';
        registerForm.style.transform = 'translateX(0)';
    });

    // Cambiar a formulario de login
    loginLink.addEventListener('click', (e) => {
        e.preventDefault();
        loginForm.style.transform = 'translateX(0)';
        registerForm.style.transform = 'translateX(100%)';
    });

    // Cerrar formulario
    iconClose.addEventListener('click', () => {
        formularioContainer.classList.remove('active');
    });

    // Cerrar al hacer clic fuera del formulario
    formularioContainer.addEventListener('click', (e) => {
        if (e.target === formularioContainer) {
            formularioContainer.classList.remove('active');
        }
    });
});
