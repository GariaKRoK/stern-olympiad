
function takeUrl() {
    let id68Box = document.getElementById('id68QuestionId');
    let queText = 'Вдоль прямой аллеи стоят четыре будки – голубая, оранжевая, бирюзовая и фиолетовая (в указанном порядке). Бульдог живет не в фиолетовой будке. А соседи таксы –корги и ретривер. Кто где живет, если рядом с ретривером нет бульдога?'
    let queTextId = document.getElementById('test-counter-id').textContent;
    console.log(queTextId)
    // let id68 = url.includes(68);
       if(queText == queTextId) {
            id68Box.style.display = 'block'; 
        }

}
takeUrl();


