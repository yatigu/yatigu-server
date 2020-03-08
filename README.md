# yatigu-server


## DATABASE
```
alembic upgrade head
```
## API
### /info/stations/
get : 기차역 이름을 가져옴  

```
request
{}
```
status_code  
200 : ok  

### /info/tickets/
get : 기차표 정보를 받아옴
```
request
{
date = '20200220',
hour = '160000',
start = '서울',
end = '부산'
}
```
status_code  
200 : ok  
400 : key error


### /account/user/
post : 매크로 객체를 생성
```
request
{
phone = 핸드폰번호
pw = 코레일 비밀번호
source = 출발지
destination = 도착지
index = 검색했을때 몇번째표인지(인덱스 1부터시작)
year = 출발날짜
month = 출발날짜
day = 출발날짜
hour = 출발시간
}
```
200 : ok  
400 : key error  
429 : 이용자수 초과
