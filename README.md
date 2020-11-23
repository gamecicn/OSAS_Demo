# Online Sentiment Analysis System Demo

Sentiment analysis (also known as opinion mining or emotion AI) refers to natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information. Sentiment analysis is widely applied to the voice of the customer materials such as reviews and survey responses, online and social media, and healthcare materials for applications that range from marketing to customer service to clinical medicine. (Wikipedia)

## 1. Introduce

The on line sentiment analysis system is a cloud based sentiment analysis system. With the AWS cloud platform's support, this project demonstrates an austere but complete online sentiment analysis system structure. It provides two access methods for both humans and the program. AWS Lambda makes the system scalable according to workload.  Moreover, Grafana and RDS provide a flexible and fast way to build a user-friendly data dashboard which can be used as a monitor of the system status. It can be used as a prototype for a machine learning online system in the future. 


## 2. The system architecture 

The system is based on the AWS cloud and uses Comprehend to analyze the sentiment of input corpus. It can classifies corpus's sentiment into 3 classes: negative, neutral, and positive. People can access the system with two approaches: website for human access and REST API for program access. The static website is hosed on AWS S3 bucket, while the REST API is based on AWS Gateway. Of course, the static website relies on the REST API to adjust the input text's sentiment. In fact, the API Gateway is the unique interface for the system to receive the user's request. After receiving the request, the AWS Gateway would resend the message to AWS Lambda for future process. AWS Lambda, which can run code for virtually any type of application or back-end service, is the system's core scheduler. It would send the corpus within the client's requites to AWS Comprehend, a natural language processing (NLP) service with machine learning, for sentiment analysis and then return the result to clients through API Gateway.  Asides from that, the Lambda would store the results in database. In this demo, we use MySQL as the database to store the completed requests. With the database, we can visualize the requests with [Grafana](https://grafana.com/grafana/). Grafana runs on an EC2 instance. We use Grafana to display statistical chars of requests. In practice, these statistical reports would be very useful for future analysis.

![System Architectur](https://github.com/gamecicn/OSAS_Demo/blob/main/image/architecture.png)


## 3 Video

https://youtu.be/8BWzlhqQAg0

## 4 Presentation Document

[PPT is here](https://github.com/gamecicn/OSAS_Demo/blob/main/doc/Sentiment%20Analyzer.pptx)


## 5 Team Member 

aimanjawaid.haider@duke.edu, maobin.guo@duke.edu,  xinyi.pan@duke.edu, 


