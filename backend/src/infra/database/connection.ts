import pgp from 'pg-promise';

const requiredEnvVars = ['DATABASE_HOST', 'DATABASE_PORT', 'DATABASE_NAME', 'DATABASE_USER', 'DATABASE_PASSWORD'];
const missingVars = requiredEnvVars.filter(varName => !process.env[varName]);

if (missingVars.length > 0) {
    throw new Error(`Missing required environment variables: ${missingVars.join(', ')}`);
}

const connection = pgp()({
    host: process.env['DATABASE_HOST']!,
    port: parseInt(process.env['DATABASE_PORT']!),
    database: process.env['DATABASE_NAME']!,
    user: process.env['DATABASE_USER']!,
    password: process.env['DATABASE_PASSWORD']!
});

export default connection;