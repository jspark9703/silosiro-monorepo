const { EntitySchema } = require('typeorm');

// TimestampMixin을 위한 기본 컬럼 정의
const TimestampMixin = {
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
};

module.exports = {
    TimestampMixin
};
