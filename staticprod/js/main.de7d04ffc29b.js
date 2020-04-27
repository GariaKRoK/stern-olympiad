// function regModalWindow() {
//     let regButton = document.getElementById('reg-button-id');
//     let modalWindow = document.createElement('div');
//     let modalWindowContainer = document.createElement('div');
//     let modalWindowTitle = document.createElement('div');
//     let modalWindowTop = document.createElement('div');
//     let modalWindowTimes = document.createElement('i');
//     let modalWindowMiddle = document.createElement('div');
//     let modalWindowForm = document.createElement('form');
//     let modalFIO = document.createElement('input');
//     let modalPhone = document.createElement('input');
//     let modalMail = document.createElement('input');
//     let modalClass = document.createElement('input');
//     let modalPass = document.createElement('input');
//     let modalRePass = document.createElement('input');
//     let modalWindowButton = document.createElement('button');
//     let modalWindowBottom = document.createElement('div');
//
//
//
//     modalFIO.setAttribute('placeholder','Ф.И.О');
//     modalPhone.setAttribute('placeholder','+7(_ _ _)_ _ _ - _ _ _ - _ _');
//     modalMail.setAttribute('placeholder','Почта');
//     modalClass.setAttribute('placeholder','Класс');
//     modalPass.setAttribute('placeholder','Пароль');
//     modalRePass.setAttribute('placeholder','Повторите пароль');
//     modalWindowButton.setAttribute('type','submit');
//
//
//
//
//     modalWindow.className = 'modalWindow';
//     modalWindowContainer.className = 'modalWindowContainer';
//     modalWindowTop.className = 'modalWindowTop';
//     modalWindowTitle.className = 'modalWindowTitle';
//     modalWindowTitle.textContent = 'Регистрация';
//     modalWindowTimes.classList.add('fa');
//     modalWindowTimes.classList.add('fa-times');
//     modalWindowForm.className = 'modalWindowForm';
//     modalFIO.className = 'modalFormInput';
//     modalPhone.className = 'modalFormInput';
//     modalMail.className = 'modalFormInput';
//     modalPass.className = 'modalFormInput';
//     modalRePass.className = 'modalFormInput';
//     modalClass.classList.add('modalFormInput');
//     modalClass.classList.add('modalFormInputClass');
//     modalWindowBottom.className = 'modalWindowBottom';
//
//
//
//
//
//     modalWindowButton.className = 'modalFormButtonSubmit';
//     modalWindowButton.textContent = 'Подтвердить регистрацию и оплатить';
//
//
//
//     modalWindow.appendChild(modalWindowContainer);
//     modalWindowContainer.appendChild(modalWindowTop);
//     modalWindowTop.appendChild(modalWindowTitle);
//     modalWindowTop.appendChild(modalWindowTimes);
//
//     modalWindowContainer.appendChild(modalWindowMiddle);
//     modalWindowMiddle.appendChild(modalWindowForm);
//     modalWindowForm.appendChild(modalFIO);
//     modalWindowForm.appendChild(modalPhone);
//     modalWindowForm.appendChild(modalMail);
//     modalWindowForm.appendChild(modalPass);
//     modalWindowForm.appendChild(modalRePass);
//     modalWindowForm.appendChild(modalWindowBottom);
//     modalWindowBottom.appendChild(modalClass);
//     modalWindowBottom.appendChild(modalWindowButton);
//
//     if(screen.width > 100 && screen.width < 599) {
//         modalWindowTitle.style.fontSize = '14px';
//         modalWindowBottom.style.display = 'block';
//         modalWindowButton.style.fontSize = '12px';
//     }
//
//
//     regButton.addEventListener('click',function () {
//
//         document.body.appendChild(modalWindow);
//         modalWindowTimes.addEventListener('click',function () {
//             modalWindow.remove();
//         })
//     })
//
// }
//
//
//
//
// function signModalWindow() {
//     let regButton = document.getElementById('nav-button-link-id');
//     let modalWindow = document.createElement('div');
//     let modalWindowContainer = document.createElement('div');
//     let modalWindowTitle = document.createElement('div');
//     let modalWindowTop = document.createElement('div');
//     let modalWindowTimes = document.createElement('i');
//     let modalWindowMiddle = document.createElement('div');
//     let modalWindowForm = document.createElement('form');
//     let modalFIO = document.createElement('input');
//     let modalPhone = document.createElement('input');
//     let modalMail = document.createElement('input');
//     let modalClass = document.createElement('input');
//     let modalPass = document.createElement('input');
//     let modalRePass = document.createElement('input');
//     let modalWindowButton = document.createElement('button');
//     let modalWindowBottom = document.createElement('div');
//
//
//
//     modalFIO.setAttribute('placeholder','Ф.И.О');
//     modalPhone.setAttribute('placeholder','+7(_ _ _)_ _ _ - _ _ _ - _ _');
//     modalMail.setAttribute('placeholder','Почта');
//     modalClass.setAttribute('placeholder','Класс');
//     modalPass.setAttribute('placeholder','Пароль');
//     modalRePass.setAttribute('placeholder','Повторите пароль');
//     modalWindowButton.setAttribute('type','submit');
//
//
//
//
//     modalWindow.className = 'modalWindow';
//     modalWindowContainer.className = 'modalWindowContainer';
//     modalWindowTop.className = 'modalWindowTop';
//     modalWindowTitle.className = 'modalWindowTitle';
//     modalWindowTitle.textContent = 'Авторизация';
//     modalWindowTimes.classList.add('fa');
//     modalWindowTimes.classList.add('fa-times');
//     modalWindowForm.className = 'modalWindowForm';
//     modalFIO.className = 'modalFormInput';
//     modalPhone.className = 'modalFormInput';
//     modalMail.className = 'modalFormInput';
//     modalPass.className = 'modalFormInput';
//     modalRePass.className = 'modalFormInput';
//     modalClass.classList.add('modalFormInput');
//     modalClass.classList.add('modalFormInputClass');
//     modalWindowBottom.className = 'modalWindowBottom';
//
//
//
//
//
//     modalWindowButton.className = 'modalFormButtonSubmit';
//     modalWindowButton.textContent = 'Авторизоваться';
//
//
//
//     modalWindow.appendChild(modalWindowContainer);
//     modalWindowContainer.appendChild(modalWindowTop);
//     modalWindowTop.appendChild(modalWindowTitle);
//     modalWindowTop.appendChild(modalWindowTimes);
//
//     modalWindowContainer.appendChild(modalWindowMiddle);
//     modalWindowMiddle.appendChild(modalWindowForm);
//     modalWindowForm.appendChild(modalMail);
//     modalWindowForm.appendChild(modalPass);
//     modalWindowForm.appendChild(modalWindowBottom);
//     modalWindowBottom.appendChild(modalWindowButton);
//
//     if(screen.width > 100 && screen.width < 599) {
//         modalWindowTitle.style.fontSize = '14px';
//         modalWindowBottom.style.display = 'block';
//         modalWindowButton.style.fontSize = '12px';
//     }
//
//     regButton.addEventListener('click',function () {
//         document.body.appendChild(modalWindow);
//         modalWindowTimes.addEventListener('click',function () {
//             modalWindow.remove();
//         })
//     })
// }
//
//
//
//
// regModalWindow();
// signModalWindow();

function modalReg() {
    let activeModal = document.getElementById('modalWindowRegId');
    let buttonOpen = document.getElementById('reg-button-id');
    let buttonClose = document.getElementById('modalCloseButtonReg');
    let rulesBlock = document.getElementById('olymp-content-sign-id');

    buttonOpen.addEventListener('click',function () {
        activeModal.style.display = 'block';
        buttonOpen.style.background = 'transparent';
        buttonOpen.style.color = 'transparent';
        rulesBlock.style.display = 'none';
        buttonClose.addEventListener('click',function () {
            activeModal.style.display = 'none';
            rulesBlock.style.display = 'block';
            buttonOpen.style.background = '#399fb7';
            buttonOpen.style.color = '#fff';
        })
    })


}
modalReg();


//
// function modalAuth() {
//     let activeModalReg = document.getElementById('modalWindowAuthId');
//     let buttonModalReg = document.getElementById('nav-button-link-id');
//     let buttonTimes = document.getElementById('modalCloseButtonAuth');
//     buttonModalReg.addEventListener('click',function () {
//         activeModalReg.style.display = 'block';
//         buttonTimes.addEventListener('click',function () {
//             activeModalReg.style.display = 'none';
//         })
//
//     })
// }
// modalAuth();