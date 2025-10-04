const { EntitySchema } = require('typeorm');

const GyoanWordsMapSchema = new EntitySchema({
    name: 'GyoanWordsMap',
    tableName: 'gyoan_words_map',
    columns: {
        id: {
            primary: true,
            type: 'int',
            generated: true
        },
        gyoan_id: {
            type: 'int',
            nullable: false
        },
        words_id: {
            type: 'int',
            nullable: false
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
        gyoan: {
            target: 'Gyoan',
            type: 'many-to-one',
            joinColumn: {
                name: 'gyoan_id',
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

module.exports = GyoanWordsMapSchema;
