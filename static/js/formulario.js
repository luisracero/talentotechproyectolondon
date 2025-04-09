document.addEventListener('DOMContentLoaded', function () {
    const formularioContainer = document.querySelector('.formulario-container');
    const formularioLogin = document.querySelector('.formulariologin');
    const loginBox = document.querySelector('.form-box.login');
    const registerBox = document.querySelector('.form-box.registro');
    const loginForm = document.querySelector('#login-form form');
    const registerForm = document.querySelector('#register-form form');
    const loginLink = document.querySelector('.login-link');
    const registerLink = document.querySelector('.register-link');
    const iconClose = document.querySelector('.icon-close');
    const btnLoginPopup = document.querySelector('.btnlogin-popup');

    // Mostrar formulario al hacer clic en Login del navbar
    btnLoginPopup.addEventListener('click', () => {
        formularioContainer.classList.add('active');
        formularioContainer.classList.add('show-popup');
    });

    // Cambiar a formulario de registro (activar transición)
    registerLink.addEventListener('click', (e) => {
        e.preventDefault();
        formularioLogin.classList.add('active');
    });

    // Cambiar a formulario de login (desactivar transición)
    loginLink.addEventListener('click', (e) => {
        e.preventDefault();
        formularioLogin.classList.remove('active');

        const loginEmail = loginForm.querySelector('input[name="email"]');
        if (loginEmail) loginEmail.focus();
    });

    // Cerrar formulario
    iconClose.addEventListener('click', () => {
        formularioContainer.classList.remove('active', 'show-popup');
    });

    // Cerrar al hacer clic fuera del formulario
    formularioContainer.addEventListener('click', (e) => {
        if (e.target === formularioContainer) {
            formularioContainer.classList.remove('active', 'show-popup');
        }
    });

    // Mostrar automáticamente el login si hubo error (con Flask)
    if (window.location.href.includes('login_error=true')) {
        formularioContainer.classList.add('active', 'show-popup');
        formularioLogin.classList.remove('active');

        const emailInput = loginForm.querySelector('input[name="email"]');
        const passwordInput = loginForm.querySelector('input[name="password"]');
        if (emailInput) emailInput.value = '';
        if (passwordInput) passwordInput.value = '';

        const url = new URL(window.location);
        url.searchParams.delete("login_error");
        window.history.replaceState({}, document.title, url.pathname);
    }

    // LOGIN con fetch
    if (loginForm) {
        loginForm.addEventListener('submit', async function (e) {
            e.preventDefault();

            const email = loginForm.querySelector('input[name="email"]').value;
            const password = loginForm.querySelector('input[name="password"]').value;

            const response = await fetch('/api/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });

            const result = await response.json();

            if (result.status === 'ok') {
                window.location.href = '/';
            } else {
                mostrarAlerta(loginForm, result.msg, 'danger');
                loginForm.reset();
            }
        });
    }

    // REGISTRO con fetch
    if (registerForm) {
        registerForm.addEventListener('submit', async function (e) {
            e.preventDefault();

            const email = registerForm.querySelector('input[name="email"]').value;
            const password = registerForm.querySelector('input[name="password"]').value;

            const response = await fetch('/api/register', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });

            const result = await response.json();

            if (result.status === 'ok') {
                mostrarAlerta(registerForm, result.msg, 'success');
                registerForm.reset();

                // Volver a login automáticamente
                setTimeout(() => {
                    formularioLogin.classList.remove('active');
                    const loginEmail = loginForm.querySelector('input[name="email"]');
                    if (loginEmail) loginEmail.focus();
                }, 2000);
            } else {
                mostrarAlerta(registerForm, result.msg, 'danger');
            }
        });
    }

    // Función para mostrar mensajes flotantes (alertas)
    function mostrarAlerta(formulario, mensaje, tipo) {
        const alerta = document.createElement('div');
        alerta.className = `alert alert-${tipo} alert-dismissible fade show mt-2`;
        alerta.role = 'alert';
        alerta.innerHTML = `
            ${mensaje}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;

        const anterior = formulario.querySelector('.alert');
        if (anterior) anterior.remove();

        formulario.prepend(alerta);
    }
});
