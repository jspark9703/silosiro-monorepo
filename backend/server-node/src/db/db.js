require('dotenv').config();
require('reflect-metadata');
const { DataSource } = require('typeorm');
const { 
    UserSchema, 
    WordsSchema, 
    UserWordsMapSchema, 
    UserMapSchema, 
    ProgressLogSchema, 
    GyoanSchema, 
    GyoanWordsMapSchema 
} = require('./schemas');

const sslOption = process.env.PGSSL === 'true' ? { rejectUnauthorized: false } : undefined;

const AppDataSource = new DataSource({
    type: 'postgres',
    host: process.env.PGHOST,
    port: process.env.PGPORT ? Number(process.env.PGPORT) : 5432,
    database: process.env.PGDATABASE,
    username: process.env.PGUSER,
    password: process.env.PGPASSWORD,
    ssl: sslOption,
    entities: [
        UserSchema,
        WordsSchema,
        UserWordsMapSchema,
        UserMapSchema,
        ProgressLogSchema,
        GyoanSchema,
        GyoanWordsMapSchema
    ],
    synchronize: false, // 프로덕션에서는 false로 설정
    logging: process.env.NODE_ENV === 'development'
});

// Initialize database connection
AppDataSource.initialize()
    .then(() => {
        console.log('[DB] TypeORM DataSource has been initialized successfully');
    })
    .catch((err) => {
        console.error('[DB] Error during DataSource initialization:', err);
    });

module.exports = { AppDataSource };


