# One Music

##Setup
Pre-requisites: serverless

    cd one-music
    npm install

##Run
    #for local testing
    serverless wsgi serve 
    
## Deploy
Do aws configure before run

    # for deploying to lambda+api-gateway
    serverless deploy 
    