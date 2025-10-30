document.addEventListener('DOMContentLoaded', function () {
    const faqQuestions = document.querySelectorAll('.faq-question');

    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const faqItem = question.parentElement;
            const faqAnswer = faqItem.querySelector('.faq-answer');

            // Toggle the active class on the faq-item
            faqItem.classList.toggle('active');

            // If the item is active, set the max-height to reveal the answer
            if (faqItem.classList.contains('active')) {
                faqAnswer.style.maxHeight = faqAnswer.scrollHeight + 'px';
                faqAnswer.style.padding = '15px 0'; /* Add padding when open */
            } else {
                faqAnswer.style.maxHeight = '0';
                faqAnswer.style.padding = '0'; /* Remove padding when closed */
            }
        });
    });
});
