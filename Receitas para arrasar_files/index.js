function createListeners() {
    let menucontainer = document.getElementById('mobileMenu')

    menucontainer.addEventListener('click', () => {
        let menubtn = document.querySelector('.fa-bars')
        let closebtn = document.querySelector('.fa-close')
        let menucontent = document.querySelector('.btnMenuContent')
        let animatemenu = anime({
            targets: menucontent,
            duration: 500,
            easing: 'easeOutSine',
            height: ['250px', '0px'],
            padding: '0px',
            autoplay: false
        })
        let animatemenurev = anime({
            targets: menucontent,
            duration: 500,
            easing: 'easeOutSine',
            height: ['0px', '250px'],
            padding: '20px',
            autoplay: false
        })
        if (menubtn.style.display === 'none') {
            closebtn.style.display = 'none';
            menubtn.style.display = 'block';
            animatemenu.play()
        } else {
            animatemenurev.play()
            closebtn.style.display = 'block';
            menubtn.style.display = 'none';
        }
    })

    
    for (let i = 1; i <= 6; i++) {
        const el = document.getElementById(`question-${i}`)
        const docele = document.querySelector(`#answer-${i}`)
        const docchild = document.querySelector(`#question-${i}-icon`)

        el.addEventListener("click", () => {
            if (docele.style.height === '0px') {
                anim1.play()
                rotaterev.play()
            } else {
                anim.play()
                rotate.play()
            }
        })

        let rotate = anime({
            targets: docchild,
            duration: 500,
            easing: 'easeOutSine',
            rotate: ['180', '0'],
            autoplay: false
        })

        let rotaterev = anime({
            targets: docchild,
            duration: 500,
            easing: 'easeOutSine',
            rotate: ['0', '180'],
            autoplay: false
        })

        let anim = anime({
            targets: docele,
            duration: 500,
            easing: 'easeOutSine',
            height: ['100%', '0px'],
            margin: ['20px', 0],
            autoplay: false
        })
        let anim1 = anime({
            targets: docele,
            height: ['0px', '100%'],
            margin: [0, '20px'],
            translateZ: 0,
            duration: 500,
            easing: 'easeOutSine',
            autoplay: false
        })
        anim.play()
    }
}



createListeners()