# One Music

## Setup
Pre-requisite - [serverless](https://www.serverless.com/framework/docs/getting-started/)

    cd one-music/backend
    npm install


## Run
For local testing
    
    serverless wsgi serve  

    
## Deploy
Do aws configure before run. For deploying to lambda+api-gateway
    
    serverless deploy 
    
## Test
https://rx00516zgh.execute-api.us-west-2.amazonaws.com/dev/
https://one-music.netlify.app/