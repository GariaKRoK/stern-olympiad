
function olympTimer() {
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
            timer.innerHTML =timer.innerHTML = `${t.hours} часов ${t.minutes} минут ${t.seconds} секунд`
            if (t.total <= 0) {
                clearInterval(timeinterval);
            }
        }
        updateClock();
        let timeInterval = setInterval(updateClock,1000)
    }
    initializeClock('olymp-timer', deadline);
}
olympTimer()



$('.question-slider').slick({
    infinite:true,
    slidesToShow: 1,
    slidesToScroll:1,
    prevArrow: $('.olymp-slider-prev'),
    nextArrow: $('.olymp-slider-next'),
    dots:false,
})

$('.olymp-slider-item').click(function () {
    let $this = $(this);
    $('.question-slider').slick('slickGoTo', $this.data('index'))
    $('.olymp-slider-item').removeClass('olymp-slider-item-active')
    $this.addClass('olymp-slider-item-active')
});



$('.olymp-slider-prev').click(function (){
    let list = $('.olymp-slider-item');
    let current = 0;
    for (let i = 0; i < list.length;i++) {
        if (list[i].classList.contains('olymp-slider-item-active')) {
            current = i;
        }
    }
    if (current === 0) {
        $($('.olymp-slider-item')[current]).removeClass('olymp-slider-item-active')
        current = list.length;
        $($('.olymp-slider-item')[current-1]).addClass('olymp-slider-item-active')
    } else {
        $($('.olymp-slider-item')[current]).removeClass('olymp-slider-item-active')
        $($('.olymp-slider-item')[current-1]).addClass('olymp-slider-item-active')

    }
})

$('.olymp-slider-next').click(function (){
    let list = $('.olymp-slider-item');
    let current = 0;
    for (let i = 0; i < list.length;i++) {
        if (list[i].classList.contains('olymp-slider-item-active')) {
            current = i;
        }
    }
    if (current === list.length - 1) {
        $($('.olymp-slider-item')[current]).removeClass('olymp-slider-item-active')
        current = 0;
        $($('.olymp-slider-item')[current]).addClass('olymp-slider-item-active')
    } else {

        $($('.olymp-slider-item')[current]).removeClass('olymp-slider-item-active')
        $($('.olymp-slider-item')[current+1]).addClass('olymp-slider-item-active')

    }
})