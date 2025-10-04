const { EntitySchema } = require('typeorm');

const WordsSchema = new EntitySchema({
    name: 'Words',
    tableName: 'words',
    columns: {
        id: {
            primary: true,
            type: 'int',
            generated: true
        },
        gyoan_types: {
            type: 'simple-array',
            nullable: true
        },
        is_img: {
            type: 'boolean',
            default: false,
            nullable: false
        },
        is_sound: {
            type: 'boolean',
            default: false,
            nullable: false
        },
        is_user_gen: {
            type: 'boolean',
            default: false,
            nullable: false
        },
        created_by: {
            type: 'int',
            nullable: true
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
    },
    relations: {
        creator: {
            target: 'User',
            type: 'many-to-one',
            joinColumn: {
                name: 'created_by',
                referencedColumnName: 'id'
            },
            nullable: true
        }
    }
});

module.exports = WordsSchema;
