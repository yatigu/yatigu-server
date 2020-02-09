# yatigu-server
# ip : 15.165.170.3:8000  

## API
### /info/stations
get : 기차역 이름을 가져옴  

```
request
{}
```
status_code  
200 : ok  

### /info/tickets
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
