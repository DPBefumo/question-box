const favoriteQuestionLink = document.querySelector("#favorited")
favoriteQuestionLink.addEventListener("click", event => {
    event.preventDefault()
    const questionId = favoriteQuestionLink.dataset.questionId
    fetch('/core/' + questionId + '/favorite/', {
        method: 'POST',
        credentials: 'include'
    })
    .then(res => res.json())
    .then(data => {
        if (data.isFavorite) {
            favoriteQuestionLink.innerHTML = '&#9734'
        } else {
            favoriteQuestionLink.innerHTML = '&#11088;'
        }
    })
})

const markCorrectLink = document.querySelectorAll("#mark-correct");
for (let answer of markCorrectLink){answer.addEventListener("click", (event) => {
    event.preventDefault();
    const questionId = answer.dataset.questionId;
    const answerId = answer.dataset.answerId;
    fetch("/core/" + questionId + "/" + answerId + "/correct/", {
        method: "POST",
        credentials: "include",
    })
        .then((res) => res.json())
        .then((data) => { 
            if (data.markedCorrect) {answer.innerHTML = "&#9989";
        } else {
            answer.innerText = "Is this correct?"
        }
        })
})}