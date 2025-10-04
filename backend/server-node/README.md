# silosiro-monorepo 사용 가이드

## 브랜치 구조
각 서비스는 별도의 브랜치로 관리됩니다.
- `server-node` : Node.js 백엔드
- `server-py`   : Python 백엔드
- `front`       : 프론트엔드

## 작업 및 PR 프로세스
1. 각 서비스별 브랜치에서 작업합니다.
2. 작업 완료 후 Pull Request(PR)을 생성합니다.

## 배포
- 배포는 **Docker**를 사용합니다.
