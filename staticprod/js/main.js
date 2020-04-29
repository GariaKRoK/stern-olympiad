function modalReg() {
    // get important elements by id
    let activeModal = document.getElementById('modalWindowRegId');
    let buttonOpen = document.getElementById('reg-button-id');
    let buttonClose = document.getElementById('modalCloseButtonReg');
    let rulesBlock = document.getElementById('olymp-content-sign-id');
    // modal window open listener
    buttonOpen.addEventListener('click',function () {
        // add different styles to active modal window
        activeModal.style.display = 'block';
        buttonOpen.style.background = 'transparent';
        buttonOpen.style.color = 'transparent';
        rulesBlock.style.display = 'none';
        // modal window close listener
        buttonClose.addEventListener('click',function () {
            activeModal.style.display = 'none';
            rulesBlock.style.display = 'block';
            buttonOpen.style.background = '#399fb7';
            buttonOpen.style.color = '#fff';
        })
    })
}
modalReg();
// calling function
