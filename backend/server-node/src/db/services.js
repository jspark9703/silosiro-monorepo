const { AppDataSource } = require('./db');
const { Repository } = require('typeorm');

// TypeORM을 사용한 데이터베이스 작업 예제

class UserService {
    constructor() {
        this.userRepository = AppDataSource.getRepository('User');
    }

    // 사용자 생성
    async createUser(userData) {
        const user = this.userRepository.create(userData);
        return await this.userRepository.save(user);
    }

    // 사용자 ID로 조회
    async findUserById(id) {
        return await this.userRepository.findOne({ where: { id } });
    }

    // 사용자 ID로 조회 (user_id 필드)
    async findUserByUserId(userId) {
        return await this.userRepository.findOne({ where: { user_id: userId } });
    }

    // 모든 사용자 조회
    async findAllUsers() {
        return await this.userRepository.find();
    }

    // 사용자 업데이트
    async updateUser(id, updateData) {
        await this.userRepository.update(id, updateData);
        return await this.findUserById(id);
    }

    // 사용자 삭제
    async deleteUser(id) {
        return await this.userRepository.delete(id);
    }
}

class WordsService {
    constructor() {
        this.wordsRepository = AppDataSource.getRepository('Words');
    }

    // 단어 생성
    async createWords(wordsData) {
        const words = this.wordsRepository.create(wordsData);
        return await this.wordsRepository.save(words);
    }

    // 단어 조회
    async findWordsById(id) {
        return await this.wordsRepository.findOne({ 
            where: { id },
            relations: ['creator']
        });
    }

    // 사용자가 생성한 단어들 조회
    async findWordsByCreator(createdBy) {
        return await this.wordsRepository.find({ 
            where: { created_by: createdBy }
        });
    }

    // 이미지가 있는 단어들 조회
    async findWordsWithImages() {
        return await this.wordsRepository.find({ 
            where: { is_img: true }
        });
    }
}

class UserWordsMapService {
    constructor() {
        this.userWordsMapRepository = AppDataSource.getRepository('UserWordsMap');
    }

    // 사용자-단어 매핑 생성
    async createUserWordsMap(userId, wordsId, data = null) {
        const userWordsMap = this.userWordsMapRepository.create({
            user_id: userId,
            words_id: wordsId,
            data
        });
        return await this.userWordsMapRepository.save(userWordsMap);
    }

    // 사용자의 단어 매핑 조회
    async findUserWordsMapsByUserId(userId) {
        return await this.userWordsMapRepository.find({
            where: { user_id: userId },
            relations: ['user', 'words']
        });
    }
}

class ProgressLogService {
    constructor() {
        this.progressLogRepository = AppDataSource.getRepository('ProgressLog');
    }

    // 진행 로그 생성
    async createProgressLog(userId, startedAt, type, data = null) {
        const progressLog = this.progressLogRepository.create({
            user_id: userId,
            started_at: startedAt,
            type,
            data
        });
        return await this.progressLogRepository.save(progressLog);
    }

    // 사용자의 진행 로그 조회
    async findProgressLogsByUserId(userId) {
        return await this.progressLogRepository.find({
            where: { user_id: userId },
            relations: ['user'],
            order: { started_at: 'DESC' }
        });
    }
}

module.exports = {
    UserService,
    WordsService,
    UserWordsMapService,
    ProgressLogService
};
