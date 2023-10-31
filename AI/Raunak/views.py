from django.shortcuts import render
from django.http import HttpResponse

def my_intro(request):
    html_content = '''

    <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div>
            <div>
        <h1>Raunak Batra</h1>
        <br/>
        <p>Contact:
        <a href="mailto:raunakbatra2003@gmail.com">raunakbatra2003@gmail.com</a>
        </p>
        <p>Github:
            <a href="https://github.com/raunakcode03">github.com/raunakcode03</a>
        </p>
        <p> Linkedin:
            <a href="https://www.linkedin.com/in/raunak-batra-240ba2202">raunakbatra/Linkedin</a>

        </p>

            </div>
            <section> 
            <h2>BIO</h2>
            <p>
                I am a passionate and results-driven Front-End Developer and Software Engineer with a strong background in crafting exceptional user
                 experiences and building robust software solutions. With a deep appreciation for the intersection of design and technology, I thrive on translating
                  creative concepts into functional, user-friendly applications. I am committed to staying up-to-date with the latest industry trends and technologies to deliver cutting-edge solutions.
            </p>
            </section>
           

            <SECTion>
                <h2>Education</h2>
                <p>
                    <ul>
                        <li><h3 style="margin: 0%;">Noida Institute Of Engineering And Technology</h3>    
                         Computer Science Engineering with Specialized in Artificial Intelligence(2021-2025)</li>
                        <li><h3>Modern School Noida</h3></li>
                    </ul>
                </p>
            </SECTion>


            <section>
        <h2>Experience</h2>
            <p>
                <ul>
                    <li><h3 style="margin: 0%;">Rectangle One</h3>
                     Graphic Designer(2022-)  
                     <ul>
                        <li>Presentation Design</li>
                        <li>Poster Design</li>
                        <li>Research </li>
                     </ul>
                </li>
                    <li><h3 style="margin: 0%;">GirlScript Summer of Code</h3>
                    Contributor(May 2022-August 2023)</li>
                    <ul>
                        <li>Open Source Contribution</li>
                        <li>Learn How to use Github repositories and how things work in Github</li>
                    </ul>
                <ul/>
            </p>
    
            </section>

            <section>
                <h2>Skills</h2>
                <p>
                    <ul>
                        <li>Java</li>
                        <li>Python</li>
                        <li>Html</li>
                        <li>CSS</li>
                        <li>SQL</li>
                    </ul>
                </p>
            </section>

            <section>
                <h2>Projects</h2>
                <p>
                    <ul>
                        <li><h3 style="margin: 0%;">Movie Recommend Sytsem</h3>
                            Made a Machine learning model in which we try to recommend a movie according to give datasets on Movie . We use Python Langauge
                            and Sckitlearn for the Model and use Streamlit which is PythonBased Web deployment model to deploy my model in form of website
                        </li>
                        <li>
                        <h3 style="margin: 0%;">ChatBot</h3>
                        By using Google Dialogflow we made easy Chatbot for Food ordering app which help in order 
                        and giving feedbacks regarding Food.
                        </li>
                    </ul>
                </p>
            </section>

            <footer>
                <p> &#169; 2023 Raunak Batra. All Rights Reserved</p>
            </footer>

            

    </div>
   


</body>
</html>

'''

    return HttpResponse(html_content)


def my_work(request):
    return HttpResponse("<a href='/my_intro/'>My Intro</a><br><a href='/assignment1/'>Assignment 1</a>")

def assignment1(request):
    return HttpResponse("I have not done Assignment 1.")
