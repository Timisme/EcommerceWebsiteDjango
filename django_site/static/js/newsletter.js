const newsletterBtn = document.querySelector('.newsletter-btn')
const newsletterInput = document.querySelector('.newsletter-input')
// console.log(newsletterBtn)
newsletterBtn.addEventListener('click', async function(e){
    e.preventDefault();
    let email = newsletterInput.value;
    let url = '/api/newsletter/';

    await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'email': email
        }),
    })
    .then((res) => { return res.json() })
    .then((data) => { console.log(data) })
})