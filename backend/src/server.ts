import express from 'express';

const app = express();

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});

app.get('/', (_req, res) => {
    return res.status(200).json({
        code: 200,
        message: 'Server is running'
    })
});