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
$('#payment-read-more').click(function (){
    $('#modal-payment').addClass('modal-payment-active')
})
$('#modal-payment-close').click(function (){
    $('#modal-payment').removeClass('modal-payment-active')
})
$('.sign-modal-Buttons').click(function () {
    $('#signModal').addClass('sign-modal-active')
    $('#signModalBg').addClass('sign-modal-bg-active')
})
$('#sign-modal-close').click(function (){
    $('#signModal').removeClass('sign-modal-active')
    $('#signModalBg').removeClass('sign-modal-bg-active')
})
