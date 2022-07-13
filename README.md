# EC2Trigger-Lambda
Start and stop EC2 instances through a Lambda function

Can be useful when interacting with EC2 instances from an external endpoint, like Discord or Telegram Bots

I wrote below an interaction example with **discordjs**
```js
async function start_ec2(text_channel, ec2_instance_name) {
    current_textchannel = text_channel;
    data = {   
        "trigger": "start",               //I want to start my instances
        "instances": [ec2_instance_name]  //List of EC2 instances
    }
    fetch(config.aws.lambdaUrl, {         //Lambda URL function, 
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    }).then(async (res) => {
        console.log("STATUS: " + res.status)
        if (res.status == 200) {
            await current_textchannel.send("START Request sent successfully")
        } else {
            await current_textchannel.send("START Request failed")
        }
    });  
}
```
To interact with an EC2 instance, your Lambda IAM role must have this Statement:
```json
{
  "Effect": "Allow",
  "Action": [
      "ec2:Start*",
      "ec2:Stop*"
  ],
  "Resource": "*"
}
