// function to add in star for favorite question

console.log("fuck this shit")

const favoriteQuestionLink = document.querySelector('#favorited')
favoriteQuestionLink.addEventListener('click', event => {
    event.preventDefault()
    const questionId = favoriteQuestionLink.dataset.questionId
    fetch('/core/' + questionId + '/favorite/', {
        method: 'POST',
        credentials: 'include'
    })
    .then(res => res.json())
    .then(data => {
        if (data.isFavorite) {
            favoriteQuestionLink.innerText = 'Unfavorite this recipe'
        } else {
            favoriteQuestionLink.innerText = 'favorite this recipe'
        }
    })
})


// function to add in star for favorite answer
const favoriteAnswerLink = document.querySelector('#favorited')
favoriteAnswerLink.addEventListener('click', event => {
    event.preventDefault()
    const answerId = favoriteAnswerLink.dataset.answerId
    fetch('/core/' + answerId + '/favorite/', {
        method: 'POST',
        credentials: 'include'
    })
    .then(res => res.json())
    .then(data => {
        if (data.isFavorite) {
            favoriteAnswerLink.innerText = 'Unfavorite this recipe'
        } else {
            favoriteAnswerLink.innerText = 'favorite this recipe'
        }
    })
})

// function to have answer added in on question page and not to take you to another page