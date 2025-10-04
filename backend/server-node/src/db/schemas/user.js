const { EntitySchema } = require('typeorm');

const UserSchema = new EntitySchema({
    name: 'User',
    tableName: 'users',
    columns: {
        id: {
            primary: true,
            type: 'int',
            generated: true
        },
        user_id: {
            type: 'varchar',
            length: 64,
            unique: true,
            nullable: false
        },
        password: {
            type: 'varchar',
            length: 128,
            nullable: false
        },
        type: {
            type: 'enum',
            enum: ['patient', 'caregiver', 'therapist'],
            nullable: false
        },
        data: {
            type: 'jsonb',
            nullable: true
        },
        created_at: {
            type: 'timestamp',
            createDate: true,
            nullable: false
        },
        updated_at: {
            type: 'timestamp',
            updateDate: true,
            nullable: false
        }
    }
});

module.exports = UserSchema;