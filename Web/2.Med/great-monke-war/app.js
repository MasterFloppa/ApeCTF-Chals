const express = require('express');
const app = express();
app.use(express.static('public'));

app.get('/', (req, res) => {    

    const language = req.headers['accept-language'];
    const requestDate = new Date(req.headers['date']);

    if(language=="ru" && requestDate >= new Date('2010-01-01') &&
    requestDate <= new Date('2017-12-31')){
        res.sendFile('there-you-go.html', { root: 'public' });
    }

    else if(language=="ru"){
        res.sendFile('too-late.html', { root: 'public' });
    }

    else res.sendFile('putin-check.html', { root: 'public' });
});

app.listen(5000, () => {
    console.log('Example app listening on port 5000!');
    }
);