const { EntitySchema } = require('typeorm');

const UserMapSchema = new EntitySchema({
    name: 'UserMap',
    tableName: 'user_map',
    columns: {
        id: {
            primary: true,
            type: 'int',
            generated: true
        },
        user1_id: {
            type: 'int',
            nullable: false
        },
        user2_id: {
            type: 'int',
            nullable: false
        },
        relation: {
            type: 'varchar',
            length: 50,
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
        user1: {
            target: 'User',
            type: 'many-to-one',
            joinColumn: {
                name: 'user1_id',
                referencedColumnName: 'id'
            },
            nullable: false
        },
        user2: {
            target: 'User',
            type: 'many-to-one',
            joinColumn: {
                name: 'user2_id',
                referencedColumnName: 'id'
            },
            nullable: false
        }
    }
});

module.exports = UserMapSchema;
