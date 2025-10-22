import express from 'express';
const app = express();
const PORT = process.env['PORT'] || 3000;
app.get('/', (_req, res) => {
    res.json({ message: 'Backend API is running!' });
});
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
//# sourceMappingURL=index.js.map