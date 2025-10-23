import axios from 'axios';

test('server is running', async () => {
    const response = await axios.get('http://localhost:3000');
    expect(response.data.code).toBe(200);
});