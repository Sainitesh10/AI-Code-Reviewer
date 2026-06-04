document.addEventListener('DOMContentLoaded', () => {
    const codeInput = document.getElementById('code-input');
    const languageSelect = document.getElementById('language-select');
    const reviewBtn = document.getElementById('review-btn');
    const resetBtn = document.getElementById('reset-btn');
    const btnText = reviewBtn.querySelector('.btn-text');
    const btnLoader = document.getElementById('btn-loader');
    
    const inputSection = document.querySelector('.input-section');
    const resultsSection = document.getElementById('results-section');
    const markdownOutput = document.getElementById('markdown-output');

    // Configure marked.js to use highlight.js for code blocks
    marked.setOptions({
        highlight: function(code, lang) {
            const language = hljs.getLanguage(lang) ? lang : 'plaintext';
            return hljs.highlight(code, { language }).value;
        },
        breaks: true
    });

    const toggleLoading = (isLoading) => {
        if (isLoading) {
            btnText.classList.add('hidden');
            btnLoader.classList.remove('hidden');
            reviewBtn.disabled = true;
            codeInput.disabled = true;
            languageSelect.disabled = true;
        } else {
            btnText.classList.remove('hidden');
            btnLoader.classList.add('hidden');
            reviewBtn.disabled = false;
            codeInput.disabled = false;
            languageSelect.disabled = false;
        }
    };

    reviewBtn.addEventListener('click', async () => {
        const code = codeInput.value.trim();
        const language = languageSelect.value;

        if (!code) {
            alert('Please paste some code to review.');
            return;
        }

        toggleLoading(true);

        try {
            // Pointing to the FastAPI backend running on the same host
            const response = await fetch('/api/review', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ code, language })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || 'An error occurred during analysis.');
            }

            // Render Markdown
            markdownOutput.innerHTML = marked.parse(data.review);
            
            // Switch views
            inputSection.classList.add('hidden');
            resultsSection.classList.remove('hidden');
            
        } catch (error) {
            alert(error.message);
        } finally {
            toggleLoading(false);
        }
    });

    resetBtn.addEventListener('click', () => {
        resultsSection.classList.add('hidden');
        inputSection.classList.remove('hidden');
        markdownOutput.innerHTML = '';
        // Optional: clear input or leave it for re-editing
        // codeInput.value = '';
    });
});
