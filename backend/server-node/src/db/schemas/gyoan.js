const { EntitySchema } = require('typeorm');

const GyoanSchema = new EntitySchema({
    name: 'Gyoan',
    tableName: 'gyoan',
    columns: {
        id: {
            primary: true,
            type: 'int',
            generated: true
        },
        title: {
            type: 'varchar',
            length: 200,
            nullable: false
        },
        type: {
            type: 'enum',
            enum: ['img_word', 'read', 'write', 'motion'],
            nullable: false
        },
        data: {
            type: 'jsonb',
            nullable: true
        },
        default_words: {
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

module.exports = GyoanSchema;
