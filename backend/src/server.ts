import 'dotenv/config';
import express from 'express';
import connection from './infra/database/connection.ts';

const app = express();

app.use(express.json());

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});

app.get('/', (_req, res) => {
    return res.status(200).json({
        code: 200,
        message: 'Server is running'
    })
});

app.post('/users', async (req, res) => {
    const sql = 'insert into library.users (name, password, email, type) values ($1, $2, $3, $4)';
    try{
        console.log(req.body);
        await connection.query(sql, [req.body.name, req.body.password, req.body.email, req.body.type]);
    } catch (error) {
        console.error(error);
        return res.status(500).json({
            code: 500,
            message: 'Internal server error'
        });
    }
    return res.status(200).json({
        code: 200,
        message: 'User created successfully'
    });
})