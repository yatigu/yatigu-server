'''
오로지 실행파일.
모든 설정은 세팅 폴더 안에서 관리 됨.
'''
from settings.settings import manager

if __name__ == '__main__':
    manager.run()
