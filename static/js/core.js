// function to add in star for favorite answer

const favoriteAnswerLink = document.querySelector('#favorite-answer')
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
            favoriteAnswerLink.innerHTML = ''
        } else {
            favoriteAnswerLink.innerHTML = ''
        }
    })
})

// function to have answer added in on question page and not to take you to another page