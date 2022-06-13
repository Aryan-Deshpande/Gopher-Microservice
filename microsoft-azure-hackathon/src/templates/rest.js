const axios = require('axios');

async function keypress() {
    const response = await axios.post('https://api.openai.com/v1/completions', {
        "model": "text-davinci-002",
        "prompt": "hey there",
        "max_tokens": 5,
        "temperature": 1,
        "top_p": 1,
        "n": 1,
        "stream": false,
        "logprobs": null,
        "stop": "\n"},
        
        {"Authorization": "Bearer " + process.env.API_KEY}
        
    ).then( 
        res => document.getElementById("text").innerText = res.data
    );
    console.log(response);
}

keypress()

