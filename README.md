I have created a chatbot using gemini ai

and then i containerized and Deployed using aws ec2 

For containerizing application use >>>> docker build -t <name> .
>>>>docker run -d -p 5000:5000 <name>

now push to the docker hub repository
>>>>docker push <name of repository>

then create an instance using aws ec2
and launch it and deploy it 
