import gradio as gr
import openai
import requests
from PIL import Image
import re

openai.api_key = "YOUR_API_KEY_HERE"
def get_images(topic):

    #print("------------ ", prompt) )

    response = openai.Image.create(
        prompt=topic,
        n=5,
        size= "256x256"
    )
    #print (response)

    res =[]
    n=len (response.data)
    for i in range(n):
        res.append(response.data[i].url)
    #print(res)
    image_url=res [0]
    response = requests.get(image_url)

    with open(r"C:\Users\DELL\OneDrive\Desktop\News-Letter-generation\\image1.jpg", "wb") as file:

        file.write(response.content)

        image_url=res [1]

        response = requests.get(image_url)



    with open(r"C:\Users\DELL\OneDrive\Desktop\News-Letter-generation\\image2.jpg", "wb") as file:



        file.write(response.content)

        image_url=res [2]

        response = requests.get(image_url)

    with open(r"C:\Users\DELL\OneDrive\Desktop\News-Letter-generation\\image3.jpg", "wb") as file: 
        file.write(response.content)

        image_url= res[3]
        response = requests.get(image_url)

    with open(r"C:\Users\DELL\OneDrive\Desktop\News-Letter-generation\\image4.jpg", "wb") as file:

        file.write(response.content)
        image_url=res [4]

        response = requests.get(image_url)

    with open(r"C:\Users\DELL\OneDrive\Desktop\News-Letter-generation\\image5.jpg", "wb") as file:

        file.write(response.content)


    
    return res



def get_completion (prompt):
    message = [{'role': 'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = message

)

    return response.choices[0].message.content



def insert_url(code, urls):

    pattern = r'<img\s+[^>]src\s=\s*["\'] ?([^"\'>]+)["\"]?[^>]*>'
    urls_iterator = iter(urls)
    modified_html = re.sub (pattern, lambda match: '<img src="{}">'.format(next(urls_iterator)), code)
    return modified_html

def fun (topic):
    prompt = f"""You are an AI bot give me 1 page html code for an newsletter on topic {topic} by  proper headings and formatting."""

    example = """<!DOCTYPE html>

<html>

<head>
    <title>Newsletter</title>

    <style>
        body {

            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
        }

        .container {

            max-width: 600px;
            margin: 0 auto;
            padding:0px 20px;
            background-color: #c4bebe;
            border: 1px solid #dddddd;

        }

        .header {

            text-align: center;
            /* height: 80px; */
            padding: 5px;
            margin-top: 8px;
            background-color: rgba(121, 10, 112, 0.733);
            margin-bottom:20px;

        }
        h1{
            color:white;
            
        }

        .content {
            margin-bottom: 20px;

        }

        .article {

            display: flex;

            margin-bottom: 20px;

            border-bottom: 1px solid #dddddd;

            padding-bottom: 20px;

        }

        img {

            border-radius: 20%;
           width: 170px;
            margin-right: 5%;
            margin-left: 5%;
            height: auto;
            margin-bottom: 10px;

        }

        .article h2 {

            font-size: 20px;
            margin-bottom: 10px;
        }

        .article p {

            font-size: 14px;
            line-height: 1.5;
        }

        .footer {

            text-align: center;

            font-size: 12px;

            color:black;

        }
    </style>

</head>

<body>

    <div class="container">

        <div class="header">

            <h1>Newsletter</h1>

        </div>

        <div class="content">

            <div class="article">

                <img src="image1.jpg" alt="Image 1">

                <div>

                    <h2>Breaking News: Air Pollution Crisis</h2>

                    an

                    population

                    <p>A recent study conducted by environmental experts reveals that air pollution levels have reached
                        all-time high in major cities. The hazardous air quality poses severe health risks to the

                        and has become a cause for concern.</p>

                </div>

            </div>

            <div class="article">

                <div>

                    <h2>Effects on Marine Life</h2>

                    <p>Scientists have discovered alarming evidence of pollution's devastating impact on marine life.

                        The

                        increasing pollution in oceans and water bodies is causing immense harm to aquatic ecosystems,
                        leading to the loss of various species and disruption of the delicate balance.</p>
                </div>

                <img src="image2.jpg" alt="Image 2">

            </div>

            <div class="article">

                <img src="image3.jpg" alt="Image 3">

                <div>

                    <h2>Combatting Pollution: Sustainable Solutions</h2>

                    <p>In the face of the pollution crisis, communities worldwide are embracing sustainable practices

                        and

                        innovations to reduce pollution. From implementing renewable energy sources to promoting

                        recycling

                        and waste management, these initiatives are crucial for creating a cleaner and healthier future

                        for

                        all.</p>

                </div>

            </div>

            <div class="article">

                <div>

                    <h2>Combatting Pollution: Sustainable Solutions</h2>

                    <p>In the face of the pollution crisis, communities worldwide are embracing sustainable practices

                        and

                        innovations to reduce pollution. From implementing renewable energy sources to promoting

                        recyclingand waste management, these initiatives are crucial for creating a cleaner and
                        healthier future

                        for

                        all.</p>

                </div>

                <img src="image4.jpg" alt="Image 3">

            </div>

        </div>

        <div class="footer">

            <p>&copy; 2023 Newsletter. All rights reserved.</p>

        </div>

    </div>
</body>

</html>"""
    oneshot = f""" Your task is to create a html code for newsletter of the '{topic}',it should exact format of {example},it should not return exactly the same html ,it shoud contain diffrent content ,but in image tag image names should be like image1.jpg,image2.jpg,image3.jpg,image4.jpg,image5.jpg and image radius 10 , and header of news letter should be {topic} """

    print (oneshot)
    temp = get_completion(oneshot)
    links = get_images (topic)
    print(links)

   
    print("#########################################################")
    print("translated text", temp)
    htmlcode=insert_url(temp,links)
    print("After", links)
    print (htmlcode)
    
    with open(r"C:\\Users\\DELL\\OneDrive\Desktop\\News-Letter-generation\\output.html", "w") as file:
        file.write(htmlcode)
    
    return htmlcode

    

demo=gr.Interface(
    fn = fun,
    inputs = ["text"],

    outputs = "text"
)
demo.launch(share=False)