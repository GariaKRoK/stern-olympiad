$('#start-modal-button').click(function (){
    $('.start-modal').addClass('start-modal-active')
})
$('#start-modal-close').click(function (){
    $('.start-modal').removeClass('start-modal-active')
})
$('.vk').hover(function () {
    let el = $(this)
    el.attr('src', 'assets/images/social-icon-vk-hovered.svg')
}, function () {
    let el = $(this)
    el.attr('src', 'assets/images/social-icon-vk.svg')
})
$('.instagram').hover(function () {
    let el = $(this)
    el.attr('src', 'assets/images/social-icon-instagram-hovered.svg')
}, function () {
    let el = $(this)
    el.attr('src', 'assets/images/social-icon-instagram.svg')
})
