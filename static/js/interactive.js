const navBar = document.getElementById('navbar');
const navBtns = navBar.querySelectorAll('.navbtn');
console.log('navBtns:', navBtns);

// navBar.addEventListener('click', function(event){
//     event.preventDefault();
//     navBar.querySelector('.active')?.classList.remove('active'); //When whatever before ? Is null or undefined, whatever after ?. Won't be called
//     console.log('navBar.querySelector active', navBar.querySelector('.active'));
//     event.target.classList.add('active');
//     console.log('event target:', event.target);
// })

for (let i = 0; i < navBtns.length; i++){
    let navBtn = navBtns[i];
    navBtn.addEventListener('click', function(e){
        // e.preventDefault();
        console.log('navBtn:', navBtn);
        // navBtns.children.querySelector('.active').classList.remove('active');
        navBar.querySelector('.active')?.classList.remove('active');
        navBtn.classList.add('active');
    });
}