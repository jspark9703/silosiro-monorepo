const { EntitySchema } = require('typeorm');

const UserWordsMapSchema = new EntitySchema({
    name: 'UserWordsMap',
    tableName: 'user_words_map',
    columns: {
        id: {
            primary: true,
            type: 'int',
            generated: true
        },
        user_id: {
            type: 'int',
            nullable: false
        },
        words_id: {
            type: 'int',
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
    },
    relations: {
        user: {
            target: 'User',
            type: 'many-to-one',
            joinColumn: {
                name: 'user_id',
                referencedColumnName: 'id'
            },
            nullable: false
        },
        words: {
            target: 'Words',
            type: 'many-to-one',
            joinColumn: {
                name: 'words_id',
                referencedColumnName: 'id'
            },
            nullable: false
        }
    }
});

module.exports = UserWordsMapSchema;
