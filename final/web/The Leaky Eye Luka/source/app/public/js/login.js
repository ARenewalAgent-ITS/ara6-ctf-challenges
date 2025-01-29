document.querySelector('form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorElement = document.getElementById('error-message');

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: email,
                password: password,
            }),
        });
        if(response.redirected){
            window.location.href = response.url;    
        }
        else if(response.status == 400 || response.status == 404 || response.status == 500) {
            const result = await response.json();
            errorElement.innerText = result.message || 'Login failed. Please try again.';
            errorElement.style.display = 'block';
            setTimeout(() => {
                errorElement.style.display = 'none';
            }, 5000);
        }
    } catch (err) {
        console.log(err);
        errorElement.innerText = 'An error occurred. Please try again.';
        errorElement.style.display = 'block';
        setTimeout(() => {
            errorElement.style.display = 'none';
        }, 3000);
    }
});
