$('#start-modal-button').click(function (){
    $('.start-modal').addClass('start-modal-active')
})
$('#start-modal-close').click(function (){
    $('.start-modal').removeClass('start-modal-active')
})

$('#popular-problems').click(function (){
    $('#popular-problems-modal').addClass('popular-problems-modal-active')
    // $('#popular-problems-modal-content').addClass('wow flipInX')
})
$('#popular-problems-modal-close').click(function (){
    $('#popular-problems-modal').removeClass('popular-problems-modal-active')
    // $('#popular-problems-modal-content').removeClass('wow flipInX')
})
$('.vk').hover(function () {
    let el = $(this)
    el.attr('src', '/static/images/social-icon-vk-hovered.svg')
}, function () {
    let el = $(this)
    el.attr('src', '/static/images/social-icon-vk.svg')
})
$('.instagram').hover(function () {
    let el = $(this)
    el.attr('src', '/static/images/social-icon-instagram-hovered.svg')
}, function () {
    let el = $(this)
    el.attr('src', '/static/images/social-icon-instagram.svg')
})

$('.vk-white').hover(function () {
    let el = $(this)
    el.attr('src', '/static/images/social-icon-vk-hovered.svg')
}, function () {
    let el = $(this)
    el.attr('src', '/static/images/social-icon-vk-white.svg')
})
$('.instagram-white').hover(function () {
    let el = $(this)
    el.attr('src', '/static/images/social-icon-instagram-hovered.svg')
}, function () {
    let el = $(this)
    el.attr('src', '/static/images/social-icon-instagram-white.svg')
})



$('#signUpSelector').click(function (){
    $('#signInSelector').removeClass('active')
    $(this).addClass('active')
    $('#signInForm').css({'left':'-1000%','transition':'.3s linear all'})
    $('#signUpForm').css({'left':'0','transition':'.3s linear all'})
})

$('#signInSelector').click(function (){
    $('#signUpSelector').removeClass('active')
    $(this).addClass('active')
    $('#signUpForm').css({'left':'-1000%','transition':'.3s linear all'})
    $('#signInForm').css({'left':'0','transition':'.3s linear all'})
})




setTimeout(function (){
    $('#preloader').remove()
},4000)
function timer() {
    let deadline = '2021-08-30'
        function getTimeRemaining(endtime) {
            let t = Date.parse(endtime) - Date.parse(new Date())
            let seconds = Math.floor((t / 1000) % 60)
            let minutes = Math.floor((t / 1000 / 60) % 60)
            let hours = Math.floor((t / (1000 * 60 * 60)) % 24);
            let days = Math.floor(t / (1000 * 60 * 60 * 24));
            return {
                'total': t,
                'days': days,
                'hours': hours,
                'minutes': minutes,
                'seconds': seconds
            };
        }

    function initializeClock(id, endtime) {
        let timer = document.getElementById(id);
        function updateClock() {
            let t = getTimeRemaining(endtime);
            timer.innerHTML =timer.innerHTML = `${t.days}дн. ${t.hours}ч. ${t.minutes}мин.`
            if (t.total <= 0) {
                clearInterval(timeinterval);
            }
        }
        updateClock();
        let timeInterval = setInterval(updateClock,1000)
    }
    initializeClock('timer', deadline);
}

timer();


