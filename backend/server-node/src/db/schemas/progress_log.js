const { EntitySchema } = require('typeorm');

const ProgressLogSchema = new EntitySchema({
    name: 'ProgressLog',
    tableName: 'progress_log',
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
        started_at: {
            type: 'timestamp',
            nullable: false
        },
        type: {
            type: 'enum',
            enum: ['video_call', 'solo_learning'],
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
        }
    }
});

module.exports = ProgressLogSchema;
